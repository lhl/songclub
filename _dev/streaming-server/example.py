#!/usr/bin/env python
'''

TODOs:

See: 
http://chrisaiv.com/post/2307142854/streaming-mp3s-using-html-css-jquery-and
http://classicalkusc.org/stream/listen2.html

jQuery UI

RPC via memcache:
- commands (next track, prev track)
  - command to play a new track
- tracklisting  
  - stream random file if not

next track


# The code I want...
http://stackoverflow.com/questions/5303445/creating-multiple-audio-streams-of-an-icecast2-server-using-python-shout

Threading or multiprocess
---
Single thread generated for each channel

Streaming - multiple streams, multithreaded
http://docs.python.org/library/threading.html
http://docs.python.org/library/queue.html?highlight=queue.queue#Queue.Queue
http://www.ibm.com/developerworks/aix/library/au-threadingpython/
http://www.artfulcode.net/articles/multi-threading-python/
http://www.tutorialspoint.com/python/python_multithreading.htm

'''

# usage: ./example.py /path/to/file1 /path/to/file2 ...
import shout
import sys
import string
import time

import thread
import threading

def channel(threadname, loc):
  s = shout.Shout()
  # print "Using libshout version %s" % shout.version()

  global threadcount, activethreads

  # s.host = 'localhost'
  # s.port = 8000
  # s.user = 'source'
  s.password = "hackme"
  s.mount = "/pyshout" + str(loc) + ".mp3"
  s.protocol = 'http'
  s.format = 'mp3'
  # s.format = 'vorbis' | 'mp3'
  # s.protocol = 'http' | 'xaudiocast' | 'icy'
  # s.name = ''
  # s.genre = ''
  # s.url = ''
  # s.public = 0 | 1
  # s.audio_info = { 'key': 'val', ... }
  #  (keys are shout.SHOUT_AI_BITRATE, shout.SHOUT_AI_SAMPLERATE,
  #   shout.SHOUT_AI_CHANNELS, shout.SHOUT_AI_QUALITY)

  s.open()

  total = 0
  st = time.time()

  fa = '1.mp3'

  # for fa in sys.argv[1:]:
  print "opening file %s" % fa
  f = open(fa, 'r')
  s.set_metadata({'song': fa})

  nbuf = f.read(4096)
  while 1:
    buf = nbuf
    nbuf = f.read(4096)
    total = total + len(buf)
    if len(buf) == 0:
      break
    s.send(buf)
    s.sync()
  f.close()
      
  et = time.time()
  br = total*0.008/(et-st)
  print "Sent %d bytes in %d seconds (%f kbps)" % (total, et-st, br)

  print s.close()
  thread.interrupt_main()


if __name__ == '__main__':
  threadcount=0
  activethreads = 2

  thread.start_new_thread(channel, ('Thread1', 1))
  # thread.start_new_thread(channel, ('Thread2', 2))

  while activethreads > 0:
    pass
