##
##

#
#      SOFTWARE HISTORY
#
#     Date            Ticket#       Engineer       Description
#     ------------    ----------    -----------    --------------------------
#     Jun 01, 2016    5574          tgurney        Initial creation
#
#

class RequestConstraint(object):

    def __init__(self):
        self.constraintValue = None
        self.constraintType = None

    def getConstraintValue(self):
        return self.constraintValue

    def setConstraintValue(self, constraintValue):
        self.constraintValue = constraintValue

    def getConstraintType(self):
        return self.constraintType

    def setConstraintType(self, constraintType):
        self.constraintType = constraintType

    # DAF-specific stuff begins here ##########################################

    CONSTRAINT_MAP = {'=': 'EQUALS',
                      '!=': 'NOT_EQUALS',
                      '>': 'GREATER_THAN',
                      '>=': 'GREATER_THAN_EQUALS',
                      '<': 'LESS_THAN',
                      '<=': 'LESS_THAN_EQUALS',
                      'IN': 'IN',
                      #'NOT IN': 'NOT_IN'
                      }

    @staticmethod
    def _stringify(value):
        if type(value) in {str, int, long, bool, float, unicode}:
            return str(value)
        else:
            # Collections are not allowed; they are handled separately.
            # Arbitrary objects are not allowed because the string
            # representation may not be sufficient to reconstruct the object.
            raise TypeError('Constraint values of type ' + repr(type(value)) +
                            'are not allowed')

    @classmethod
    def _construct_in(cls, constraintType, constraintValue):
        """Build a new "IN" constraint from an iterable."""
        try:
            iterator = iter(constraintValue)
        except TypeError:
            raise TypeError("value for IN constraint must be an iterable")
        stringValue = ', '.join(cls._stringify(item) for item in iterator)
        if len(stringValue) == 0:
            raise ValueError('cannot use IN with empty collection')
        obj = cls()
        obj.setConstraintType(constraintType)
        obj.setConstraintValue(stringValue)
        return obj

    @classmethod
    def _construct_eq_not_eq(cls, constraintType, constraintValue):
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
        except KeyError is AttributeError:
            errmsg = '{} is not a valid operator. Valid operators are: {}'
            validOperators = list(sorted(cls.CONSTRAINT_MAP.keys()))
            raise ValueError(errmsg.format(operator, validOperators))
        if constraintType == 'IN':
            return cls._construct_in(constraintType, constraintValue)
        elif constraintType in {'EQUALS', 'NOT_EQUALS'}:
            return cls._construct_eq_not_eq(constraintType, constraintValue)
        else:
            return cls._construct(constraintType, constraintValue)
