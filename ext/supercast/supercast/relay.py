# relay.py:  Facilities for relaying and re-encoding streams
# Copyright 2001 by Matthew W. Campbell.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

import FCNTL, errno, fcntl, os, os.path, supercast, sys
from twisted.internet import process, tcp
from twisted.internet.main import CONNECTION_LOST
from twisted.protocols import basic

class TCPRelay(basic.LineReceiver, supercast.TCPClient):
    def __init__(self, source, host, port, password):
        self.source = source
        self.host = host
        self.port = port
        self.password = password
        self.finished = 0
        self.setupComplete = 0
        self.register()

    def streamStarted(self):
        self.finished = 0

        if not self.connected:
            self.connect()

    def connect(self):
        self.needAuthorization = 1
        self.transport = tcp.Client(self.host, self.port, self)

    def restart(self, failed):
        self.source.removeClient(self)
        args = (self.source, self.host, self.port, self.password)

        if failed:
            supercast.sched.later(5, TCPRelay, args)
        else:
            apply(TCPRelay, args)

    def connectionFailed(self):
        print "Relay connection to %s:%s failed" % (self.host, self.port)
        self.restart(1)

    def connectionLost(self):
        print "Relay connection to %s:%s closed" % (self.host, self.port)

        if self.authTimeout:
            supercast.sched.cancel(self.authTimeout)

        del self.authTimeout
        self.restart(not self.finished)

    def authorizationTimedOut(self):
        print "Relay authorization on %s:%s timed out" % (self.host, self.port)
        self.transport.loseConnection()

    def connectionMade(self):
        self.sendLine(self.password)
        self.authTimeout = supercast.sched.later(5, self.authorizationTimedOut)

    def lineReceived(self, line):
        if self.needAuthorization:
            self.needAuthorization = 0
            supercast.sched.cancel(self.authTimeout)
            self.authTimeout = None

            if line[:2] == "OK":
                self.setRawMode()

                for key in self.source.streamInfo.keys():
                    self.sendLine("icy-%s:%s" % (key,
                                                 self.source.streamInfo[key]))

                self.sendLine("")
                self.setupComplete = 1
                self.ready()
                print "Relay connection to %s:%s established" % (self.host, self.port)
            else:
                print "Relay authorization on %s:%s failed" % (self.host, self.port)
                self.finish()

    def rawDataReceived(self, data):
        pass

    def streamFinished(self):
        self.finished = 1

        if self.connected and not self.setupComplete:
            # Don't even try to go any further until the next stream starts.
            self.finish()
        else:
            supercast.TCPClient.streamFinished(self)

    def finish(self):
        self.finished = 1
        supercast.TCPClient.finish(self)

class ReencodingRelay(supercast.Client, process.Process):
    def __init__(self, source, dest, bitRate, mode, sampleRate):
        self.source = source
        self.dest = dest
        self.bitRate = bitRate
        self.mode = mode
        self.sampleRate = sampleRate
        self.finished = 0
        args = ["lame", "-b", bitRate, "-m" + mode, "--resample", sampleRate,
                "--mp3input", "-", "-"]
        process.Process.__init__(self, "lame", args, os.environ, None)
        fcntl.fcntl(self.stdin, FCNTL.F_SETFL, os.O_NONBLOCK)
        self.register()
        self.writer.registerProducer(self, 1)
        self.ready()

    def streamStarted(self):
        self.streamInfo = self.source.streamInfo.copy()
        self.streamInfo["br"] = self.bitRate
        self.dest.sourceConnected(self)

    def streamFinished(self):
        # This should restart LAME so it's ready for the next stream.
        self.source.removeClient(self)
        self.writer.stopConsuming()

    def handleError(self, err):
        print "LAME output:", err

    def doRead(self):
        try:
            output = self.stdout.read(self.bufferSize)
        except IOError, ioe:
            if ioe.args[0] == errno.EAGAIN:
                return
            else:
                return CONNECTION_LOST
        if not output:
            return CONNECTION_LOST
        self.handleChunk(output)

    def handleChunk(self, data):
        self.dest.streamDataReceived(data)

    def write(self, data):
        if self.producing:
            process.Process.write(self, data)

    def finish(self):
        self.finished = 1
        self.source.removeClient(self)
        self.writer.stopConsuming()

    def timedOut(self):
        # Assume for now that LAME will never hang.
        pass

    def connectionLost(self):
        self.source.removeClient(self)
        self.writer.producer = None
        self.dest.sourceLost()
        process.Process.connectionLost(self)

        if not self.finished:
            ReencodingRelay(self.source, self.dest, self.bitRate, self.mode,
                             self.sampleRate)
