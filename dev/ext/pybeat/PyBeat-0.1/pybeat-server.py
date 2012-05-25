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
    print "PyBeat Streaming Server v%s" % pybeat.__version__
    print "(c) Copyright 2008 by %s" % pybeat.__author__
    print

    if len(sys.argv) < 3:

        print "usage: %s <music root> [ <server-ip:server-port> | updatedb ]" % sys.argv[0]
        print
        print "%s /mnt/music updatedb" % sys.argv[0]
        print "  - update the local database from /mnt/music"
        print
        print "%s /mnt/music 127.0.0.1:8001" % sys.argv[0]
        print "  - spawn the streaming server at localhost:8001, serving music"
        print "    from /mnt/music"
        print
        print "%s /mnt/music 0.0.0.0:8001" % sys.argv[0]
        print "  - spawn the streaming server at every interface on port 8001,"
        print "    serving music from /mnt/music"
        print
        
        sys.exit(-1)

    server_root = sys.argv[1]
    if server_root[-1] == '/':
        server_root = server_root[:-1]

    if sys.argv[2] == "updatedb":
        print "Updating local database."
        pybeat.server.update_database(server_root)
        sys.exit(0)

    interface, port = sys.argv[2].split(':')
    port = int(port)

    server = pybeat.server.setup_server(server_root, interface, port)

    try:
        server.serve_forever()
    finally:
        server.server_close()


