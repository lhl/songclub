#!/usr/bin/env python

"""
see: 
/home/lhl/www/8feed/htdocs/samsara/samsara.py
http://docs.python.org/lib/module-sqlite3.html
"""


### CONFIG ###
db = '/home/lhl/www/music/db.sqlite3'
folders = (
  '/home/locker/chrome/Download',
)
logfile = '/home/lhl/www/music/filer/log'


### IMPORT LIBRARIES ###
try:
  import md5, os, sqlite3, sys, time
  import TagLib
except ImportError, e:
  raise SystemExit, e


def main():
  # Open Log File
  f = open(logfile, 'w') 

  # Connect to DB
  conn = slqlite3.connect(db)
  c = conn.cursor()

  while 1: 
    # Get Last Update

    # Look For Changes since Last Update
    # Recursive Scan

    # Put Files into Storage
    # If Audio, Use TagLib

    # Update DB w/ Last Update
   
    f.write('%s\n' % time.ctime(time.time())) 
    f.flush() 
    time.sleep(10) 


if __name__ == "__main__":
  # do the UNIX double-fork magic, see Stevens' "Advanced 
  # Programming in the UNIX Environment" for details (ISBN 0201563177)
  try: 
    pid = os.fork() 
    if pid > 0:
      # exit first parent
      sys.exit(0) 
  except OSError, e: 
    print >>sys.stderr, "fork #1 failed: %d (%s)" % (e.errno, e.strerror) 
    sys.exit(1)

  # decouple from parent environment
  os.chdir("/") 
  os.setsid() 
  os.umask(0) 

  # do second fork
  try: 
    pid = os.fork() 
    if pid > 0:
      # exit from second parent, print eventual PID before
      print "Daemon PID %d" % pid 
      sys.exit(0) 
  except OSError, e: 
    print >>sys.stderr, "fork #2 failed: %d (%s)" % (e.errno, e.strerror) 
    sys.exit(1) 

  # start the daemon main loop
  main()
