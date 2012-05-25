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

import zlib
import pickle
import os
import mimetypes
import urllib

from SimpleXMLRPCServer import SimpleXMLRPCServer
from xmlrpclib import Binary

from pybeat.common import CHUNK_SIZE

class PyBeatServer(object):

    def __init__(self, server_root):
        self.root = server_root

    def get_database(self):

        if not os.path.exists("/tmp/pybeat-server.data"):
            update_database()

        return Binary(file("/tmp/pybeat-server.data").read())

    def read_chunk(self, filename, offset):

        filename = urllib.unquote(filename)

        print "Reading chunk from %s with offset %s" % (filename, offset)
        f = file(os.path.join(self.root, filename), "rb")
        f.seek(offset)
        return Binary(f.read(CHUNK_SIZE))

    def fileinfo(self, filename):

        filename = urllib.unquote(filename)
        
        path = os.path.join(self.root, filename)
        
        if os.path.exists(path):

            return {
                'exists': True,
                'content-type': mimetypes.guess_type(path)[0],
                'content-length': os.path.getsize(path),
            }

        else:
            
            return {'exists': False}

def setup_server(server_root, hostname, port):

    server = SimpleXMLRPCServer((hostname, port))
    server.register_introspection_functions()
    server.register_instance(PyBeatServer(server_root))

    return server

def update_database(server_root):
    file('/tmp/pybeat-server.data', 'wb').write(
        zlib.compress(pickle.dumps(list(os.walk(server_root))))
    )


