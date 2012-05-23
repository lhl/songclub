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

import BaseHTTPServer
import xmlrpclib
import pickle
import zlib
import urllib
import os

from SocketServer import ThreadingMixIn

from pybeat.common import CHUNK_SIZE

class PyBeatHTTPServer(ThreadingMixIn, BaseHTTPServer.HTTPServer):
    pass

class PyBeatRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    try:
        media_database = pickle.load(file("/tmp/pybeat-client.data"))
    except IOError:
        media_database = []

    def _pybeat_read(self):

        print "Sending request for", self._pybeat_path, "with offset", self._pybeat_read_size
        
        chunk = self._xmlrpc_proxy.read_chunk(urllib.quote(self._pybeat_path), self._pybeat_read_size)
        chunk = str(chunk)

        self._pybeat_buffer += chunk
        self._pybeat_read_size += len(chunk)
        self._pybeat_buffer_size += len(chunk)

    def _pybeat_get_chunk(self):

        chunk, self._pybeat_buffer = \
            self._pybeat_buffer[:CHUNK_SIZE], self._pybeat_buffer[CHUNK_SIZE:]

        self._pybeat_buffer_size -= len(chunk)

        return chunk

    def do_GET(self):

        # chop off the initial /
        self._pybeat_path = urllib.unquote(self.path)[1:]

        # handle the web index
        if self._pybeat_path.startswith('index/'):
            PyBeatIndexHandler(self)
            return

        # check for playlist
        if self._pybeat_path.endswith('.m3u'):
            PyBeatPlaylistHandler(self)
            return
        
        # now we can assume that this must be a request for a
        # media file, let's look it up

        fileinfo = self._xmlrpc_proxy.fileinfo(urllib.quote(self._pybeat_path))

        # if the file does not exist on our remote hos,
        # display a 404 error page

        if not fileinfo['exists']:
            self.send_response(404)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write("<h1>404</h1>")
            return
            
        # the file does exist, so let's prepare to stream it
            
        self.send_response(200)
        self.send_header("Content-Type", fileinfo['content-type'])
        self.send_header("Content-Length", fileinfo['content-length'])
        self.end_headers()

        # prepare the buffer
        self._pybeat_buffer = ""
        self._pybeat_buffer_size = 0
        self._pybeat_read_size = 0

        # pre-buffer two chunks
        for n in range(2):
            self._pybeat_read()
        
        while True:

            # write a chunk to the socket
            self.wfile.write(self._pybeat_get_chunk())

            if self._pybeat_read_size == fileinfo['content-length']:

                # everything has been read from the server

                if self._pybeat_buffer_size == 0:

                    # everything has been served to the client
                    return

                else:
                    
                    # there is more in the buffer, take another iteration
                    continue

            else:

                # if we are running out of buffer, read some more
                if self._pybeat_buffer_size < CHUNK_SIZE:
                    self._pybeat_read()
            

class PyBeatPlaylistHandler(object):

    def __init__(self, request):
        self.request = request
        self.handle_request()

    def handle_request(self):

        path = self.request.path[:-4]

        path = urllib.unquote(path)

        if path == "/everything":

            # generate a playlist for everything
            playlist = self.directory_playlist('/')

        else:

            # we need to know whether this is a directory or a file

            # find the server root 
            prefix = self.request.media_database[0][0]

            for mpath, dirs, files in self.request.media_database:

                if os.path.join(prefix, path[1:]) == mpath:
                    playlist = self.directory_playlist(path)
                    break
                
            else:

                # we did not find a directory, so this must be a file
                playlist = self.file_playlist(path)

        # generate response

        self.request.send_response(200)
        self.request.send_header("Content-Type", "audio/x-mpegurl")
        self.request.end_headers()

        self.request.wfile.write("#EXTM3U\n" + playlist)

    def directory_playlist(self, path):

        playlist = ""

        if path[-1] != '/':
            path += '/'

        # find the server root 
        prefix = self.request.media_database[0][0]

        for mpath, dirs, files in self.request.media_database:

            if mpath.startswith(os.path.join(prefix, path[1:])):
                playlist += self.directory_playlist(mpath.replace(prefix, ""))

            if mpath == os.path.join(prefix, path[1:])[:-1]:
                for f in files:
                    playlist += self.file_playlist(os.path.join(path, f))

        return playlist

    def file_playlist(self, path):

        abspath = "http://%s:%s%s" % (
            self.request._pybeat_client[0],
            self.request._pybeat_client[1],
            urllib.quote(path))

        return "#EXTINF:-1,%s\n%s\n" % (os.path.basename(path), abspath)

class PyBeatIndexHandler(object):

    def __init__(self, request):
        self.request = request
        self.handle_request()
        
    def handle_request(self):

        # chop off /index/
        path = self.request.path[7:]

        # remove url encoding
        path = urllib.unquote(path)

        # find the server root 
        prefix = self.request.media_database[0][0]

        for mpath, dirs, files in self.request.media_database:

            if os.path.join(prefix, path)[:-1] == mpath:
                self.produce_filelist(mpath, dirs, files)
                return

    def produce_filelist(self, path, dirs, files):

        output = "<h2>" + path + "</h2>"

        output += "<ul>"

        if self.request.path != "/index/":
            output += '<li><a href="../">Parent directory</a></li>' 
            playlist_file = self.request.path[6:-1]
        else:
            playlist_file = "/everything"
            
        output += '<li><a href="%s.m3u">Play this directory</a></li>' % playlist_file

        output += "</ul>"

        if dirs:
            dirs.sort()
            output += "<ul><li>%s</li></ul>" % \
                "</li><li>".join([self.directory_formatter(d) for d in dirs])

        if files:
            files.sort() 
            output += "<ul><li>%s</li></ul>" % \
                "</li><li>".join([self.file_formatter(f) for f in files])

        self.produce_output(output)

    def directory_formatter(self, directory):
        return '<a href="%s/">%s</a> [<a href="%s.m3u">Play all</a>]' % \
               (directory, directory, self.request.path[6:] + directory)

    def file_formatter(self, file):
        return '<a href="%s.m3u">%s</a>' % (self.request.path[6:] + file, file)

    def produce_output(self, output):

        self.request.send_response(200)
        self.request.send_header("Content-Type", "text/html")
        self.request.end_headers()

        self.request.wfile.write("<html><head><title>PyBeat Streaming Client</title></head>" +
                                 "<body><h1>PyBeat Streaming Client</h1><hr>" + output + "</body></html")
        

def update_database(server):

    # connect to the database
    s = xmlrpclib.Server("http://%s:%s" % tuple(server))

    # fetch database and decompress
    db = zlib.decompress(str(s.get_database()))

    # write database to file
    file("/tmp/pybeat-client.data", "wb").write(db)

def setup_client(client, server):

    # configure the request handler with access to the
    # client tuple (to construct absolute urls in playlists)
    # and a XML-RPC server proxy for all requests
    
    handler = PyBeatRequestHandler
    handler._pybeat_client = client
    handler._xmlrpc_proxy = xmlrpclib.Server("http://%s:%s" % tuple(server))

    # finally, create the server and return

    server = PyBeatHTTPServer(client, handler)
    return server

    

