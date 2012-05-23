# supercast.py:  Core Supercast functionality
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

import cPickle, os.path, string, time
from twisted.internet import main, process, tcp
from twisted.protocols import basic, http, protocol, telnet
import mysched, stats

VERSION = "1.0.3"

class Client:
    def register(self, source=None):
        if source:
            self.source = source

        self.source.addClient(self)
        self.producing = 0

        if self.source.streamActive:
            self.streamStarted()

    def ready(self):
        self.producing = 1

    def pauseProducing(self):
        self.producing = 0

    def stopProducing(self):
        self.source.removeClient(self)

    def resumeProducing(self):
        self.producing = 1

    def streamStarted(self):
        pass

class TCPClient(Client):
    def ready(self):
        self.transport.registerProducer(self, 1)
        Client.ready(self)

    def write(self, data):
        if self.producing:
            self.transport.write(data)

    def streamFinished(self):
        if self.source.autoLoseClients:
            self.finish()
        else:
            sched.later(60, self.maybeFinish)

    def finish(self):
        self.stopProducing()

        if self.connected:
            self.transport.stopConsuming()

    def maybeFinish(self):
        if not self.source.streamActive:
            self.finish()

class HTTPRequest(http.HTTP, TCPClient):
    def __init__(self):
        self.source = None
        http.HTTP.__init__(self)

    def startResponse(self, status, msg=None):
        if msg is None:
            msg = http.responses[status]

        self.sendStatus(status, msg)
        self.sendHeader("Server", "Supercast/%s" % VERSION)

    def error(self, status, msg=None):
        self.startResponse(status)
        self.endHeaders()
        self.transport.loseConnection()

    def startStream(self):
        if self.factory.streamActive:
            if self.factory.clientCount >= self.factory.maxClients:
                self.error(500, "Too Many Clients")
                return

            self.startResponse(200)
            self.sendHeader("Content-Type", "audio/mpeg")

            if self.factory.icyStreamInfo:
                streamInfo = self.factory.icyStreamInfo
            else:
                streamInfo = self.factory.streamInfo

            for key in streamInfo.keys():
                self.sendHeader("icy-" + key, streamInfo[key])

            self.endHeaders()
            self.register(self.factory)
            self.ready()
            self.bytesSent = 0
            self.factory.clientCount = self.factory.clientCount + 1
            self.factory.totalClients = self.factory.totalClients + 1

            if self.factory.clientCount > self.factory.peakClients:
                self.factory.peakClients = self.factory.clientCount

            self.lastUpdateTime = time.time()
            self.statsUpdateTask = sched.later(60, HTTPRequest.updateStats, self)
            print "Client connected (UA: %s)" % self.received["user-agent"]
        else:
            self.error(404)

    def updateStats(self, loop=1):
        self.factory.totalKB = self.factory.totalKB + (self.bytesSent / 1024.0)
        self.bytesSent = 0
        connectTime = time.time() - self.lastUpdateTime
        self.factory.totalConnectTime = \
            self.factory.totalConnectTime + connectTime
        self.lastUpdateTime = time.time()

        if loop:
            self.statsUpdateTask = sched.later(60, HTTPRequest.updateStats, self)

    def write(self, data):
        if self.producing:
            self.bytesSent = self.bytesSent + len(data)
            self.transport.write(data)

    def requestReceived(self, command, path, version, junk):
        if command != "GET":
            self.error(400)
            return

        if path[:1] != '/':
            path = '/' + path

        if not self.received.has_key("user-agent"):
            self.received["user-agent"] = "unknown"

        if HTTPRequest.requestHandlers.has_key(path):
            HTTPRequest.requestHandlers[path](self)
        else:
            self.error(404)

    def connectionLost(self):
        if self.source:
            self.factory.clientCount = self.factory.clientCount - 1
            print "Client disconnected"
            self.updateStats(0)
            sched.cancel(self.statsUpdateTask)
            del self.statsUpdateTask

    def startHTML(self, title, status=200):
        self.startResponse(200)
        self.sendHeader("Content-Type", "text/html")
        self.endHeaders()
        self.transport.write(\
"""<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="en">
<head>
<title>%s</title>
</head>
<body>
<h1>%s</h1>
""" % (title, title))

    def endHTML(self):
        self.transport.write(\
"""</body>
</html>
""")
        self.transport.loseConnection()

    def statusPage(self):
        self.startHTML("Server Status")

        if self.factory.totalClients > 0:
            avgConnectTime = stats.formatTime(self.factory.totalConnectTime / self.factory.totalClients)
        else:
            avgConnectTime = "unknown"

        if self.factory.streamActive:
            self.transport.write(\
"""<p>The stream is online with <B>%d of %d listeners (%d unique)</B>.</p>
""" % (self.factory.clientCount, self.factory.maxClients, self.factory.calcUniqueClients()))
        else:
            self.transport.write(\
"""<p>The stream is offline.</p>
""")

        self.transport.write("<dl>\n")

        if self.factory.streamActive:
            self.transport.write("""<dt>Stream Title:</dt>
<dd>%s</dd>
<dt>Stream Genre:</dt>
<dd>%s</dd>
""" % (self.factory.streamInfo["name"], self.factory.streamInfo["genre"]))

        self.transport.write("""<dt>Listener Peak:</dt>
<dd>%d</dd>
<dt>Total Data Sent:</dt>
<dd>%s</dd>
<dt>Total TIme Spent Listening:</dt>
<dd>%s</dd>
<dt>Average Time Spent Listening:</dt>
<dd>%s</dd>
</dl>
""" % (self.factory.peakClients, stats.formatKB(self.factory.totalKB), stats.formatTime(self.factory.totalConnectTime), avgConnectTime))

        self.endHTML()

    requestHandlers = {"/": startStream, "/index.html": statusPage}

class Broadcaster:
    def __init__(self):
        self.streamActive = 0
        self.streamClients = []
        self.autoLoseClients = 1
        self.icyStreamInfo = None

    def setSourceTimeout(self):
        self.sourceTimeout = sched.later(30, self.source.timedOut)

    def sourceConnected(self, source):
        self.streamActive = 1
        self.streamInfo = source.streamInfo
        self.source = source
        self.setSourceTimeout()
        clients = self.streamClients

        for client in clients:
            client.streamStarted()

    def sourceLost(self):
        if not self.streamActive:
            return

        self.streamActive = 0
        sched.cancel(self.sourceTimeout)
        del self.streamInfo, self.sourceTimeout, self.source
        # Must duplicate the list so clients can remove themselves in their
        # finish methods immediately.
        clients = self.streamClients[:]

        for client in clients:
            client.streamFinished()

    def streamDataReceived(self, data):
        sched.cancel(self.sourceTimeout)
        self.setSourceTimeout()
        clients = self.streamClients

        for client in clients:
            client.write(data)

    def addClient(self, client):
        if client not in self.streamClients:
            self.streamClients.append(client)

    def removeClient(self, client):
        if client in self.streamClients:
            self.streamClients.remove(client)

class HTTPServer(Broadcaster, protocol.Factory):
    protocol = HTTPRequest

    def __init__(self, port):
        Broadcaster.__init__(self)
        self.port = port
        self.maxClients = 32
        self.clientCount = 0
        self.totalClients = 0
        self.peakClients = 0
        self.totalKB = 0.0
        self.totalConnectTime = 0.0

    def calcUniqueClients(self):
        hosts = []

        for client in self.streamClients:
            # Make sure this is a connection from a listener and not a
            # relay.
            if hasattr(client, "factory"):
                if client.transport.hostname not in hosts:
                    hosts.append(client.transport.hostname)

        return len(hosts)

class Source(basic.LineReceiver):
    delimiter = "\n"

    def __init__(self, dest, password, titleFile=None):
        self.dest = dest
        self.password = password
        self.titleFile = titleFile
        self.streaming = 0

    def connectionMade(self):
        if self.dest.streamActive:
            self.transport.loseConnection()
        else:
            self.needPassword = 1

    def lineReceived(self, line):
        # If someone else has started streaming, don't go any further.
        if self.dest.streamActive:
            self.transport.loseConnection()
            return

        line = string.replace(line, "\r", "")

        if self.needPassword:
            if line == self.password:
                self.sendLine("OK2\r")
                self.sendLine("icy-caps:11\r")
                self.sendLine("")
                self.needPassword = 0
                self.streamInfo = {}
            else:
                self.sendLine("Invalid password")
                self.transport.loseConnection()
        elif line == "":
            self.writeTitle(self.streamInfo["name"])
            self.setRawMode()
            self.dest.sourceConnected(self)
            self.streaming = 1
            print "Source connected"
        else:
            i = string.index(line, ':')
            name = string.lower(line[:i])
            value = line[i + 1:]
            name = string.replace(name, "icy-", "")

            if name in ("name", "genre", "url", "br"):
                self.streamInfo[name] = value

    def rawDataReceived(self, data):
        self.dest.streamDataReceived(data)

    def connectionLost(self):
        if self.streaming:
            self.dest.sourceLost()
            self.streaming = 0
            self.writeTitle("Off the Air")
            print "Source disconnected"

    def writeTitle(self, text):
        if self.titleFile:
            f = open(self.titleFile + ".tmp", "w")
            f.write(text + "\n")
            f.close()
            os.rename(self.titleFile + ".tmp", self.titleFile)

    def timedOut(self):
        self.transport.loseConnection()

class SourceFactory(protocol.Factory):
    def __init__(self, dest, password, titleFile=None):
        self.dest = dest
        self.password = password
        self.titleFile = titleFile

    def buildProtocol(self, conn):
        p = Source(self.dest, self.password, self.titleFile)
        p.factory = self
        return p

sched = mysched.Scheduler()
