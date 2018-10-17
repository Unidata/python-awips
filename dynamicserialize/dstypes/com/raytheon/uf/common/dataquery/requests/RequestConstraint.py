#
#      SOFTWARE HISTORY
#
#     Date            Ticket#       Engineer       Description
#     ------------    ----------    -----------    --------------------------
#     Jun 01, 2016    5574          tgurney        Initial creation
#     Jun 27, 2016    5725          tgurney        Add NOT IN
#     Jul 22, 2016    2416          tgurney        Add evaluate()
#     Oct 05, 2018                  mjames@ucar    Python 3 types
#
#

import re
import six
from dynamicserialize.dstypes.com.raytheon.uf.common.time import DataTime


class RequestConstraint(object):

    TOLERANCE = 0.0001

    IN_PATTERN = re.compile(',\s?')

    def __init__(self):
        self.constraintValue = None
        self.constraintType = None

    def getConstraintValue(self):
        return self.constraintValue

    def setConstraintValue(self, constraintValue):
        if hasattr(self, '_evalValue'):
            del self._evalValue
        self.constraintValue = constraintValue

    def getConstraintType(self):
        return self.constraintType

    def setConstraintType(self, constraintType):
        if hasattr(self, '_evalValue'):
            del self._evalValue
        self.constraintType = constraintType

    def evaluate(self, value):
        if not hasattr(self, '_evalValue'):
            self._setupEvalValue()

        if self.constraintType == 'EQUALS':
            return self._evalEquals(value)
        elif self.constraintType == 'NOT_EQUALS':
            return not self._evalEquals(value)
        elif self.constraintType == 'GREATER_THAN':
            return self._evalGreaterThan(value)
        elif self.constraintType == 'GREATER_THAN_EQUALS':
            return self._evalGreaterThanEquals(value)
        elif self.constraintType == 'LESS_THAN':
            return self._evalLessThan(value)
        elif self.constraintType == 'LESS_THAN_EQUALS':
            return self._evalLessThanEquals(value)
        elif self.constraintType == 'BETWEEN':
            return self._evalBetween(value)
        elif self.constraintType == 'IN':
            return self._evalIn(value)
        elif self.constraintType == 'NOT_IN':
            return not self._evalIn(value)
        elif self.constraintType == 'LIKE':
            return self._evalLike(value)
        # setupConstraintType already adds correct flags for ilike
        # on regex pattern
        elif self.constraintType == 'ILIKE':
            return self._evalLike(value)
        elif self.constraintType == 'ISNULL':
            return self._evalIsNull(value)
        elif self.constraintType == 'ISNOTNULL':
            return not self._evalIsNull(value)
        else:
            errmsg = '{} is not a valid constraint type.'
            raise ValueError(errmsg.format(self.constraintType))

    def _makeRegex(self, pattern, flags):
        """Make a pattern using % wildcard into a regex"""
        pattern = re.escape(pattern)
        pattern = pattern.replace('\\%', '.*')
        pattern = pattern.replace('\\_', '.')
        pattern = pattern + '$'
        return re.compile(pattern, flags)

    def _setupEvalValue(self):
        if self.constraintType == 'BETWEEN':
            self._evalValue = self.constraintValue.split('--')
            self._evalValue[0] = self._adjustValueType(self._evalValue[0])
            self._evalValue[1] = self._adjustValueType(self._evalValue[1])
        elif self.constraintType in ('IN', 'NOT_IN'):
            splitValue = self.IN_PATTERN.split(self.constraintValue)
            self._evalValue = {
                self._adjustValueType(value)
                for value in splitValue
                }
            # if collection now contains multiple types we have to force
            # everything to string instead
            initialType = next(iter(self._evalValue)).__class__
            for item in self._evalValue:
                if item.__class__ is not initialType:
                    self._evalValue = {str(value) for value in splitValue}
                    break
        elif self.constraintType == 'LIKE':
            self._evalValue = self._makeRegex(self.constraintValue, re.DOTALL)
        elif self.constraintType == 'ILIKE':
            self._evalValue = self._makeRegex(self.constraintValue, re.IGNORECASE | re.DOTALL)
        elif self.constraintValue is None:
            self._evalValue = None
        else:
            self._evalValue = self._adjustValueType(self.constraintValue)

    def _adjustValueType(self, value):
        """
        Try to take part of a constraint value, encoded as a string, and
        return it as its 'true type'.

        _adjustValueType('3.0') -> 3.0
        _adjustValueType('3') -> 3.0
        _adjustValueType('a string') -> 'a string'
        """
        try:
            return float(value)
        except ValueError:
            pass
        try:
            return DataTime(value)
        except ValueError:
            pass
        return value

    def _matchType(self, value, otherValue):
        """
        Return value coerced to be the same type as otherValue. If this is
        not possible, just return value unmodified.
        """
        if not isinstance(value, otherValue.__class__):
            try:
                return otherValue.__class__(value)
            except ValueError:
                pass
        return value

    def _evalEquals(self, value):
        value = self._matchType(value, self._evalValue)
        if isinstance(value, float):
            return abs(float(self._evalValue) - value) < self.TOLERANCE
        return value == self._evalValue

    def _evalGreaterThan(self, value):
        value = self._matchType(value, self._evalValue)
        return value > self._evalValue

    def _evalGreaterThanEquals(self, value):
        value = self._matchType(value, self._evalValue)
        return value >= self._evalValue

    def _evalLessThan(self, value):
        value = self._matchType(value, self._evalValue)
        return value < self._evalValue

    def _evalLessThanEquals(self, value):
        value = self._matchType(value, self._evalValue)
        return value <= self._evalValue

    def _evalBetween(self, value):
        value = self._matchType(value, self._evalValue[0])
        return self._evalValue[0] <= value <= self._evalValue[1]

    def _evalIn(self, value):
        anEvalValue = next(iter(self._evalValue))
        if isinstance(anEvalValue, float):
            for otherValue in self._evalValue:
                try:
                    if abs(otherValue - float(value)) < self.TOLERANCE:
                        return True
                except ValueError:
                    pass
            return False
        value = self._matchType(value, anEvalValue)
        return value in self._evalValue

    def _evalLike(self, value):
        value = self._matchType(value, self._evalValue)
        if self.constraintValue == '%':
            return True
        return self._evalValue.match(value) is not None

    def _evalIsNull(self, value):
        return value is None or value == 'null'

    # DAF-specific stuff begins here ##########################################

    CONSTRAINT_MAP = {'=': 'EQUALS',
                      '!=': 'NOT_EQUALS',
                      '>': 'GREATER_THAN',
                      '>=': 'GREATER_THAN_EQUALS',
                      '<': 'LESS_THAN',
                      '<=': 'LESS_THAN_EQUALS',
                      'IN': 'IN',
                      'NOT IN': 'NOT_IN'
                      }

    @staticmethod
    def _stringify(value):
        if six.PY2:
            if isinstance(value, (str, int, long, bool, float, unicode)):
                return str(value)
            else:
                # Collections are not allowed; they are handled separately.
                # Arbitrary objects are not allowed because the string
                # representation may not be sufficient to reconstruct the object.
                raise TypeError('Constraint values of type ' + repr(type(value)) +
                                'are not allowed')
        else:
            if isinstance(value, (str, int, bool, float)):
                return str(value)
            else:
                # Collections are not allowed; they are handled separately.
                # Arbitrary objects are not allowed because the string
                # representation may not be sufficient to reconstruct the object.
                raise TypeError('Constraint values of type ' + repr(type(value)) +
                                'are not allowed')

    @classmethod
    def _constructIn(cls, constraintType, constraintValue):
        """Build a new "IN" or "NOT IN" constraint from an iterable."""
        try:
            iterator = iter(constraintValue)
        except TypeError:
            raise TypeError("value for IN / NOT IN constraint must be an iterable")
        stringValue = ', '.join(cls._stringify(item) for item in iterator)
        if not stringValue:
            raise ValueError('cannot use IN / NOT IN with empty collection')
        obj = cls()
        obj.setConstraintType(constraintType)
        obj.setConstraintValue(stringValue)
        return obj

    @classmethod
    def _constructEq(cls, constraintType, constraintValue):
        """Build a new = or != constraint. Handle None specially by making an
        "is null" or "is not null" instead.
        """
        obj = cls()
        if constraintValue is None:
            if constraintType == 'EQUALS':
                obj.setConstraintType('ISNULL')
            elif constraintType == 'NOT_EQUALS':
                obj.setConstraintType('ISNOTNULL')
        else:
            obj = cls._construct(constraintType, constraintValue)
        return obj

    @classmethod
    def _construct(cls, constraintType, constraintValue):
        """Build a new constraint."""
        stringValue = cls._stringify(constraintValue)
        obj = cls()
        obj.setConstraintType(constraintType)
        obj.setConstraintValue(stringValue)
        return obj

    @classmethod
    def new(cls, operator, constraintValue):
        """Build a new RequestConstraint."""
        try:
            constraintType = cls.CONSTRAINT_MAP[operator.upper()]
        except KeyError:
            errmsg = '{} is not a valid operator. Valid operators are: {}'
            validOperators = list(sorted(cls.CONSTRAINT_MAP.keys()))
            raise ValueError(errmsg.format(operator, validOperators))
        if constraintType in ('IN', 'NOT_IN'):
            return cls._constructIn(constraintType, constraintValue)
        elif constraintType in {'EQUALS', 'NOT_EQUALS'}:
            return cls._constructEq(constraintType, constraintValue)
        return cls._construct(constraintType, constraintValue)
