#!/usr/bin/env python

import random
import shout
import sys
import time
import threading
import threadpool

def main():
  # Max Workers
  pool = threadpool.ThreadPool(4)

  # When creating a bunch of stuff
  streams = ['1.mp3', '2.mp3', '3.mp3', '4.mp3']
  requests = threadpool.makeRequests(stream_music, streams, done_callback, handle_exception)

  # Make Requests
  for req in requests:
    pool.putRequest(req)
    print "Work request #%s added." % req.requestID
  # or [main.putRequest(req) for req in requests]

  # Run them
  while True:
    try:
      time.sleep(0.5)
      pool.poll()
      print "(active worker threads: %i)" % (threading.activeCount()-1, )
    except KeyboardInterrupt:
      print "**** Interrupted!"
      break
    except NoResultsPending:
      print "**** No pending results."
    except NoWorkersAvailable:
      print "**** Out of workers."

  # Cleanup
  if pool.dismissedWorkers:
    print "Joining all dismissed worker threads..."
    main.joinAllDismissedWorkers()



def stream_music(song):
  s = shout.Shout()
  s.password = "don'thackme"
  s.mount = "/pyshout/" + song
  s.protocol = 'http'
  s.format = 'mp3'

  try:
    s.open()
  except:
    wait = 1 + (3 * random.random())
    time.sleep(wait)
    s.open()

  total = 0
  st = time.time()

  while True:
    print "opening file %s" % song
    f = open(song, 'r')
    s.set_metadata({'song': song})

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

  s.close()
  return song


def done_callback(request, s):
  print "**** Result from request #%s: %r" % (request.requestID, s)


def handle_exception(request, exc_info):
  if not isinstance(exc_info, tuple):
    # Something is seriously wrong...
    print request
    print exc_info
    raise SystemExit
  print "**** Exception occured in request #%s: %s" % (request.requestID, exc_info)


if __name__ == '__main__':
  main()
