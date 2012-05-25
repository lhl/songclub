# mysched.py:  A simpler delayed callback scheduler for Twisted
# Copyright 2001 by Matthew W. Campbell.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of version 2.1 of the GNU Lesser General Public
# License as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

import bisect, time, traceback
from twisted.python import log

class Scheduler:
    def __init__(self):
        self.tasks = []

    def later(self, delay, func, args=()):
        task = (time.time() + delay, func, args)
        bisect.insort(self.tasks, task)
        return task

    def cancel(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def timeout(self):
        if self.tasks:
            return max(self.tasks[0][0] - time.time(), 0.0)
        else:
            return None

    def runUntilCurrent(self):
        while self.tasks and time.time() >= self.tasks[0][0]:
            task = self.tasks.pop(0)

            try:
                apply(task[1], task[2])
            except:
                traceback.print_exc(file=log.logfile)
