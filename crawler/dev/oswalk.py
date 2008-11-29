#!/usr/bin/python 

import os

dir = '/locker/music/_misc'
for root, dirs, files in os.walk(dir):
  for f in files:
    print f
