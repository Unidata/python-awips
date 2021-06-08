#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    04/28/2015      4027          randerso       Added optional construction parameter to set the time
#    06/26/2015      4480          dgilling       Implement __eq__ and __hash__.
#

from time import gmtime, strftime


class Date(object):

    def __init__(self, timeInMillis=None):
        self.time = timeInMillis

    def getTime(self):
        return self.time

    def setTime(self, timeInMillis):
        self.time = timeInMillis

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return strftime("%b %d %y %H:%M:%S GMT", gmtime(self.time/1000.0))

    def __eq__(self, other):
        return self.time == other.time

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.time)
