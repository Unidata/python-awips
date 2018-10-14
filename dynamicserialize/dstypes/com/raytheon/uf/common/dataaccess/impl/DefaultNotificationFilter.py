#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    06/03/16        2416          rjpeter        Initial Creation.
#    08/01/16        2416          tgurney        Implement accept()
#
#

from awips.dataaccess import INotificationFilter
import sys

if sys.version_info.major == 2:
    from itertools import izip
    # shadowing built-in zip
    zip = izip


class DefaultNotificationFilter(INotificationFilter):

    def __init__(self):
        self.constraints = None

    def getConstraints(self):
        return self.constraints

    def setConstraints(self, constraints):
        self.constraints = constraints

    def accept(self, dataUri):
        tokens = dataUri.split('/')[1:]
        if len(self.constraints) != len(tokens):
            return False
        for constraint, token in zip(self.constraints, tokens):
            if not constraint.evaluate(token):
                return False
        return True
