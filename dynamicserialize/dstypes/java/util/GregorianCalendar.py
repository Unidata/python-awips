#
# Custom python class representing a java.util.GregorianCalendar.
#
# This is a stripped-down version of the class that only supports
# minimal methods for serialization.
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    09/29/10                      wldougher     Initial Creation.
#


class GregorianCalendar(object):

    def __init__(self):
        self.time = None

    # Methods from the real class that we typically use
    @staticmethod
    def getInstance():
        return GregorianCalendar()

    def getTimeInMillis(self):
        return self.time

    def setTimeInMillis(self, timeInMillis):
        self.time = timeInMillis
