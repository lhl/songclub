from pyunit import unittest
from twisted.python import roots
import types

class RootsTest(unittest.TestCase):
    def testCollection(self):
        collection = roots.Collection()
        collection.putEntity("x", 'test')
        self.failUnlessEqual(collection.getStaticEntity("x"),
                             'test')
        collection.delEntity("x")
        self.failUnlessEqual(collection.getStaticEntity('x'),
                             None)


    def testConstrained(self):
        class const(roots.Constrained):
            def nameConstraint(self, name):
                return (name == 'x')
        c = const()
        self.failUnlessEqual(c.putEntity('x', 'test'), None)
        self.failUnlessRaises(roots.ConstraintViolation,
                              c.putEntity, 'y', 'test')


    def testHomogenous(self):
        h = roots.Homogenous()
        h.entityType = types.IntType
        h.putEntity('a', 1)
        self.failUnlessEqual(h.getStaticEntity('a'),1 )
        self.failUnlessRaises(roots.ConstraintViolation,
                              h.putEntity, 'x', 'y')

