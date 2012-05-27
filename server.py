#!/usr/bin/env python

import datetime
import json
from   pprint import pprint
import os
import subprocess
import sys
import time
import tornado.auth
import tornado.autoreload
import tornado.httpclient
import tornado.gen
import tornado.ioloop
from   tornado.options import define, options
import tornado.web
import traceback
import urllib2
import urlparse

# Handlers
import handlers
from handlers.auth import *
from handlers.search import *

# DEBUG
if sys.stdout.isatty():
  debug = 1
else:
  debug = 0


# App
class Application(tornado.web.Application):
  def __init__(self):
    handlers = [
      # auth
      (r'/login', AuthLoginHandler),

      # search proxy
      (r'/search/(.+)', SearchHandler),
    ]

    settings = { 
      'static_path': os.path.join(os.path.dirname(__file__), 'www'),
      'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
      'cookie_secret': 'd12eee33d182a00d3824b1ba0a9e513b5145cb59',
      'login_url': '/login',
      'debug': True # Template Reloading
    }

    tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == '__main__':
  Application().listen(9999, 'localhost')
  ioloop = tornado.ioloop.IOLoop.instance()
  tornado.autoreload.start(io_loop=ioloop)
  ioloop.start()
