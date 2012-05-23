#!/usr/bin/python

# This file is part of PyBeat.

# PyBeat is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# PyBeat is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with PyBeat.  If not, see <http://www.gnu.org/licenses/>.

import sys
import pybeat

if __name__ == '__main__':

    print
    print "PyBeat Streaming Client v%s" % pybeat.__version__
    print "(c) Copyright 2008 by %s" % pybeat.__author__
    print

    if len(sys.argv) < 2:

        print "usage: %s <server-ip:server-port> [updatedb | local-port]" % sys.argv[0]
        print
        print "%s home.example.org:8000 updatedb" % sys.argv[0]
        print "  - update the database from the server at home.example.org:8000"
        print
        print "%s home.example.org:8000" % sys.argv[0]
        print "  - connect to the server at home.example.org:8000 and expose the"
        print "    client at http://localhost:8000/index/ (port 8000 is the default."
        print 
        print "%s home.example.org:8000 8888" % sys.argv[0]
        print "  - connect to the server at home.example.org:8000 and expose the"
        print "    client at http://localhost:8888/index/"
        print
        
        sys.exit(-1)

    server = sys.argv[1].split(":")
    client_port = 8000

    if len(sys.argv) > 2:

        if sys.argv[2] == "updatedb":
            print "Updating local database."
            pybeat.client.update_database(server)
            sys.exit(0)

        client_port = int(sys.argv[2])

    print "Connecting to server %s:%s" % tuple(server)
    print "Spawning web interface at http://localhost:%s/index/" % client_port
    print 
    
    client = pybeat.client.setup_client(
        client=("localhost", client_port),
        server=server
    )

    try:
        client.serve_forever()
    finally:
        client.server_close()


