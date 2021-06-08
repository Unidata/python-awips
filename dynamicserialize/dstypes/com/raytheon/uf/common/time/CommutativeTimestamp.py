#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    06/23/2016      #5696         rjpeter        Initial creation.
#

from dynamicserialize.dstypes.java.sql import Timestamp


class CommutativeTimestamp(Timestamp):

    def __init__(self, timeInMillis=None):
        super(CommutativeTimestamp, self).__init__(timeInMillis)
