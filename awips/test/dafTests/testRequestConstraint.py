#
# Unit tests for Python implementation of RequestConstraint
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    07/22/16        2416          tgurney        Initial creation
#
#

from dynamicserialize.dstypes.com.raytheon.uf.common.dataquery.requests import RequestConstraint

import unittest


class RequestConstraintTestCase(unittest.TestCase):

    def _newRequestConstraint(self, constraintType, constraintValue):
        constraint = RequestConstraint()
        constraint.constraintType = constraintType
        constraint.constraintValue = constraintValue
        return constraint

    def testEvaluateEquals(self):
        new = RequestConstraint.new
        self.assertTrue(new('=', 3).evaluate(3))
        self.assertTrue(new('=', 3).evaluate('3'))
        self.assertTrue(new('=', '3').evaluate(3))
        self.assertTrue(new('=', 12345).evaluate(12345))
        self.assertTrue(new('=', 'a').evaluate('a'))
        self.assertTrue(new('=', 'a').evaluate(u'a'))
        self.assertTrue(new('=', 1.0001).evaluate(2.0 - 0.999999))
        self.assertTrue(new('=', 1.00001).evaluate(1))
        self.assertFalse(new('=', 'a').evaluate(['a']))
        self.assertFalse(new('=', 'a').evaluate(['b']))
        self.assertFalse(new('=', 3).evaluate(4))
        self.assertFalse(new('=', 4).evaluate(3))
        self.assertFalse(new('=', 'a').evaluate('z'))

    def testEvaluateNotEquals(self):
        new = RequestConstraint.new
        self.assertTrue(new('!=', 'a').evaluate(['a']))
        self.assertTrue(new('!=', 'a').evaluate(['b']))
        self.assertTrue(new('!=', 3).evaluate(4))
        self.assertTrue(new('!=', 4).evaluate(3))
        self.assertTrue(new('!=', 'a').evaluate('z'))
        self.assertFalse(new('!=', 3).evaluate('3'))
        self.assertFalse(new('!=', '3').evaluate(3))
        self.assertFalse(new('!=', 3).evaluate(3))
        self.assertFalse(new('!=', 12345).evaluate(12345))
        self.assertFalse(new('!=', 'a').evaluate('a'))
        self.assertFalse(new('!=', 'a').evaluate(u'a'))
        self.assertFalse(new('!=', 1.0001).evaluate(2.0 - 0.9999))

    def testEvaluateGreaterThan(self):
        new = RequestConstraint.new
        self.assertTrue(new('>', 1.0001).evaluate(1.0002))
        self.assertTrue(new('>', 'a').evaluate('b'))
        self.assertTrue(new('>', 3).evaluate(4))
        self.assertFalse(new('>', 20).evaluate(3))
        self.assertFalse(new('>', 12345).evaluate(12345))
        self.assertFalse(new('>', 'a').evaluate('a'))
        self.assertFalse(new('>', 'z').evaluate('a'))
        self.assertFalse(new('>', 4).evaluate(3))

    def testEvaluateGreaterThanEquals(self):
        new = RequestConstraint.new
        self.assertTrue(new('>=', 3).evaluate(3))
        self.assertTrue(new('>=', 12345).evaluate(12345))
        self.assertTrue(new('>=', 'a').evaluate('a'))
        self.assertTrue(new('>=', 1.0001).evaluate(1.0002))
        self.assertTrue(new('>=', 'a').evaluate('b'))
        self.assertTrue(new('>=', 3).evaluate(20))
        self.assertFalse(new('>=', 1.0001).evaluate(1.0))
        self.assertFalse(new('>=', 'z').evaluate('a'))
        self.assertFalse(new('>=', 40).evaluate(3))

    def testEvaluateLessThan(self):
        new = RequestConstraint.new
        self.assertTrue(new('<', 'z').evaluate('a'))
        self.assertTrue(new('<', 30).evaluate(4))
        self.assertFalse(new('<', 3).evaluate(3))
        self.assertFalse(new('<', 12345).evaluate(12345))
        self.assertFalse(new('<', 'a').evaluate('a'))
        self.assertFalse(new('<', 1.0001).evaluate(1.0002))
        self.assertFalse(new('<', 'a').evaluate('b'))
        self.assertFalse(new('<', 3).evaluate(40))

    def testEvaluateLessThanEquals(self):
        new = RequestConstraint.new
        self.assertTrue(new('<=', 'z').evaluate('a'))
        self.assertTrue(new('<=', 20).evaluate(3))
        self.assertTrue(new('<=', 3).evaluate(3))
        self.assertTrue(new('<=', 12345).evaluate(12345))
        self.assertTrue(new('<=', 'a').evaluate('a'))
        self.assertFalse(new('<=', 1.0001).evaluate(1.0002))
        self.assertFalse(new('<=', 'a').evaluate('b'))
        self.assertFalse(new('<=', 4).evaluate(30))

    def testEvaluateIsNull(self):
        new = RequestConstraint.new
        self.assertTrue(new('=', None).evaluate(None))
        self.assertTrue(new('=', None).evaluate('null'))
        self.assertFalse(new('=', None).evaluate(()))
        self.assertFalse(new('=', None).evaluate(0))
        self.assertFalse(new('=', None).evaluate(False))

    def testEvaluateIsNotNull(self):
        new = RequestConstraint.new
        self.assertTrue(new('!=', None).evaluate(()))
        self.assertTrue(new('!=', None).evaluate(0))
        self.assertTrue(new('!=', None).evaluate(False))
        self.assertFalse(new('!=', None).evaluate(None))
        self.assertFalse(new('!=', None).evaluate('null'))

    def testEvaluateIn(self):
        new = RequestConstraint.new
        self.assertTrue(new('in', [3]).evaluate(3))
        self.assertTrue(new('in', ['a', 'b', 3]).evaluate(3))
        self.assertTrue(new('in', 'a').evaluate('a'))
        self.assertTrue(new('in', [3, 4, 5]).evaluate('5'))
        self.assertTrue(new('in', [1.0001, 2, 3]).evaluate(2.0 - 0.9999))
        self.assertFalse(new('in', ['a', 'b', 'c']).evaluate('d'))
        self.assertFalse(new('in', 'a').evaluate('b'))

    def testEvaluateNotIn(self):
        new = RequestConstraint.new
        self.assertTrue(new('not in', ['a', 'b', 'c']).evaluate('d'))
        self.assertTrue(new('not in', [3, 4, 5]).evaluate(6))
        self.assertTrue(new('not in', 'a').evaluate('b'))
        self.assertFalse(new('not in', [3]).evaluate(3))
        self.assertFalse(new('not in', ['a', 'b', 3]).evaluate(3))
        self.assertFalse(new('not in', 'a').evaluate('a'))
        self.assertFalse(new('not in', [1.0001, 2, 3]).evaluate(2.0 - 0.9999))

    def testEvaluateBetween(self):
        # cannot make "between" with RequestConstraint.new()
        new = self._newRequestConstraint
        self.assertTrue(new('BETWEEN', '1--1').evaluate(1))
        self.assertTrue(new('BETWEEN', '1--10').evaluate(1))
        self.assertTrue(new('BETWEEN', '1--10').evaluate(5))
        self.assertTrue(new('BETWEEN', '1--10').evaluate(10))
        self.assertTrue(new('BETWEEN', '1.0--1.1').evaluate(1.0))
        self.assertTrue(new('BETWEEN', '1.0--1.1').evaluate(1.05))
        self.assertTrue(new('BETWEEN', '1.0--1.1').evaluate(1.1))
        self.assertTrue(new('BETWEEN', 'a--x').evaluate('a'))
        self.assertTrue(new('BETWEEN', 'a--x').evaluate('j'))
        self.assertTrue(new('BETWEEN', 'a--x').evaluate('x'))
        self.assertFalse(new('BETWEEN', '1--1').evaluate(2))
        self.assertFalse(new('BETWEEN', '1--2').evaluate(10))
        self.assertFalse(new('BETWEEN', '1--10').evaluate(0))
        self.assertFalse(new('BETWEEN', '1--10').evaluate(11))
        self.assertFalse(new('BETWEEN', '1.0--1.1').evaluate(0.99))
        self.assertFalse(new('BETWEEN', '1.0--1.1').evaluate(1.11))
        self.assertFalse(new('BETWEEN', 'a--x').evaluate(' '))
        self.assertFalse(new('BETWEEN', 'a--x').evaluate('z'))

