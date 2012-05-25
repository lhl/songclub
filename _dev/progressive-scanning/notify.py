#!/usr/bin/env python

import pyinotify
'''
Docs:
https://github.com/seb-m/pyinotify/wiki/Tutorial
'''

wm = pyinotify.WatchManager()
mask = pyinotify.IN_CREATE | pyinotify.IN_DELETE | pyinotify.IN_MOVED_FROM | pyinotify.IN_MOVED_TO


class EventHandler(pyinotify.ProcessEvent):
  def process_IN_CREATE(self, event):
    print "Creating:", event.pathname

  def process_IN_DELETE(self, event):
    print "Removing:", event.pathname

#log.setLevel(10)
notifier = pyinotify.ThreadedNotifier(wm, EventHandler())
notifier.start()

wdd = wm.add_watch('/www/songclub', mask, rec=True)
wm.rm_watch(wdd.values())

notifier.stop()



'''
Moving a file in:
<Event dir=False mask=0x100 maskname=IN_CREATE name=foo path=. pathname=/locker/_muffins/locker/www/songclub/foo wd=1 >

Rename:
<Event cookie=22201607 dir=False mask=0x40 maskname=IN_MOVED_FROM name=foo path=. pathname=/locker/_muffins/locker/www/songclub/foo wd=1 >
<Event cookie=22201607 dir=False mask=0x80 maskname=IN_MOVED_TO name=foo2 path=. pathname=/locker/_muffins/locker/www/songclub/foo2 src_pathname=foo wd=1 >
'''
