
# Twisted, the Framework of Your Internet
# Copyright (C) 2001 Matthew W. Lefkowitz
# 
# This library is free software; you can redistribute it and/or
# modify it under the terms of version 2.1 of the GNU Lesser General Public
# License as published by the Free Software Foundation.
# 
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA


import sys

# Twisted Imports
from twisted.protocols import protocol

# Sibling Imports
import abstract
from main import CONNECTION_LOST, CONNECTION_DONE

_stdio_in_use = 0

class StandardIO(abstract.FileDescriptor, protocol.Transport):
    """I can connect Standard IO to a twisted.protocol.

    I act as a selectable for sys.stdin, and provide a write method that writes
    to stdout.
    """
    def __init__(self, protocol):
        """Create me with a protocol.

        This will fail if a StandardIO has already been instantiated.
        """
        global _stdio_in_use
        assert not _stdio_in_use, "Standard IO already in use."
        _stdio_in_use = 1
        self.fileno = sys.stdin.fileno
        self.protocol = protocol
        self.protocol.makeConnection(self)
        self.startReading()

    def write(self, data):
        """Write some data to standard output.
        """
        sys.stdout.write(data)
        # This is an asynchronous framework, but stdout *really* ought to be
        # flushable in a reasonable amount of time.
        sys.stdout.flush()
        
    def doRead(self):
        """Some data's readable from standard input.
        """
        # assume line-buffered.
        line = sys.stdin.readline()
        if line == '':
            return CONNECTION_LOST
        self.protocol.dataReceived(line)

    def connectionLost(self):
        """The connection was lost.
        """
        self.protocol.connectionLost()
