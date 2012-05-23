#!/usr/bin/env python

import sys, time
from daemon import Daemon

class Scanner(Daemon):
	def run(self):
		while True:
			time.sleep(1)

if __name__ == "__main__":
	daemon = Scanner('/tmp/daemon-example.pid')
	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			daemon.start()
		elif 'stop' == sys.argv[1]:
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			daemon.restart()
		else:
			print "Unknown command"
			sys.exit(2)
		sys.exit(0)
	else:
		print "usage: %s start|stop|restart" % sys.argv[0]
		sys.exit(2)

'''
IPC via named pipe?: http://blog.interviewstreet.com/2011/02/ipc-mechanisms-named-pipes/
Need threads to do non-blocking I/O: http://www.doughellmann.com/PyMOTW/threading/
Daemon Thread: http://stackoverflow.com/questions/1411860/what-difference-it-makes-when-i-set-python-thread-as-a-deamon
http://stackoverflow.com/questions/4330111/python-thread-daemon-property
Async: http://stackoverflow.com/questions/375427/non-blocking-read-on-a-stream-in-python
Alarms: http://stackoverflow.com/questions/4892623/avoid-hang-when-writing-to-named-pipe-which-disappears-and-comes-back
'''
