
# Twisted, the Framework of Your Internet
# Copyright (C) 2001 Matthew W. Lefkowitz
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

"""
Test cases for twisted.reality module.
"""

from pyunit import unittest

from twisted.reality import error
from twisted.reality import reality
from twisted.reality import thing
from twisted.reality import player
from twisted.reality import room

class ContainmentTestCase(unittest.TestCase):
    def setUp(self):
        r = self.reality = reality.Reality()
        self.ball =   thing.Thing("ball", r)
        self.box =    thing.Thing("box", r)
        self.table =  thing.Thing("table", r)
        self.slab =   thing.Thing("slab", r)
        self.bob =    player.Player("bob", r)
        self.room =   room.Room("room", r)
        self.area =   room.Room("area", r)

    def tearDown(self):
        for x in 'ball', 'table', 'slab', 'bob', 'room':
            getattr(self, x).destroy()
            delattr(self, x)


    def testBasicContainment(self):
        self.ball.location = self.room
        print "CONTAINMENT:", self.room._Thing__index.data
        assert self.room.find('ball') is self.ball
        assert self.ball.location is self.room,\
               "Ball was located " + str(self.ball.location)
        assert self.ball.place is self.room,\
               "Ball was placed " + str(self.ball.place)
        del self.ball.location
        try:
            self.room.find('ball')
        except error.CantFind: pass
        else:
            assert 0, "This should have failed!"
        assert self.ball.location is None, "location attribute didn't go None"
        assert self.ball.place is None, "place didn't go None"


    def testComponentContainment(self):
        self.ball.location = self.table
        self.ball.component = 1
        self.table.location = self.room
        assert self.ball.location is self.table
        assert self.ball.place is self.table
        assert self.table.find('ball') is self.ball
        self.failUnlessRaises(error.Failure, self.ball.move, destination=self.room, actor=self.bob)
        self.ball.component = 0
        self.ball.location = self.room
        assert self.room.find('ball') is self.ball
        try:
            self.table.find("ball")
        except:
            pass
        else:
            assert 0, "reference cruft left on 'table'."


    def testMultiContainment(self):
        self.table.grab(self.ball)
        self.room.grab(self.ball)
        assert self.room.find('ball') is self.ball
        assert self.table.find('ball') is self.ball
        assert self.ball.location is None
        self.table.toss(self.ball)
        self.room.toss(self.ball)
        self.ball.location = self.slab
        assert self.slab.find('ball') is self.ball
        for x in (self.room, self.table):
            self.failUnlessRaises(error.CantFind, x.find, 'ball')

    def testSurfaceContainment(self):
        self.table.surface = 1
        self.ball.location = self.table
        self.table.location = self.room
        assert self.ball.location is self.table,\
               "location is "+repr(self.ball.location)
        assert self.ball.place is self.room, (
            "place is "+repr(self.ball.place)+ ", locations is " +
            repr(self.ball.locations))
        del self.table.location
        del self.ball.location

        ## Mixing it up a little bit -- applying the surface bit at
        ## the end instead of the beginning.
        self.ball.location = self.table
        self.table.location = self.room
        self.table.surface = 1
        assert self.ball.location is self.table,\
               "location is "+repr(self.ball.location)
        assert self.ball.place is self.room,\
               "place is "+repr(self.ball.place)

        self.table.surface = 0

    def testMultiSurfaceContainment(self):
        ## adding yet more complexity -- 2 levels deep.
        self.table.location = self.room
        self.ball.location = self.slab
        self.slab.location = self.table
        self.slab.surface = 1
        self.table.surface = 1
        assert self.ball.location is self.slab,\
               "location is "+repr(self.ball.location)
        assert self.ball.place is self.room,\
               "place is "+repr(self.ball.place)
        assert self.room.find('ball') is self.ball,\
               "couldn't find ball"
        self.table.surface = 0
        try:
            self.room.find('ball')
            assert 0, "shouldn't be able to find ball."
        except error.CantFind:
            pass
        self.box.surface = 1
        self.ball.location = self.box
        self.box.location = self.slab

    def testPathologicalContainment(self):
        self.table.location = self.room
        self.box.location = self.table
        self.box.surface = 1
        self.table.surface = 1
        # since everything's made a surface and all events are propogated,
        # performance is factorial here, so this `large' number doesn't have to
        # be very large :)
        # in practice, this number should never be bigger than 4.
        largeNumber = 15
        things = []
        for i in range(largeNumber):
            thng = thing.Thing("thing"+str(i))
            thng.surface = 1
            things.append(thng)

        things[0].location = self.box

        for i in range(len(things)):
            thng = things[i]
            if i:
                thng.location = things[i-1]
        assert things[largeNumber-1] == self.room.find('thing' + str(largeNumber-1)),\
               "thing not found"

        for thng in things:
            thng.destroy()

testCases = [ContainmentTestCase]
