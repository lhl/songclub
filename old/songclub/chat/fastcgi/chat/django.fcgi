#!/usr/bin/python
import os, sys
#sys.path.insert(0, THE_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] = "django_chat.settings"
from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
