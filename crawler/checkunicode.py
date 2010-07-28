#!/usr/bin/python

import chardet
from time import strftime

# Dump fulllist.txt w/ 'cd /locker/music; find . > fulllist.txt'

for line in open("/locker/music/fulllist.txt"):
  try:
    x = unicode(line)
  except:
    print "Trying chardet on:", line
    try:
      encoding = chardet.detect(line)['encoding']
      print "chardet detects: " + encoding
      x = unicode(line, encoding)
    except UnicodeDecodeError:
      print "chardet failed!"
