#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    ??/??/??                      xxxxxxxx       Initial Creation.
#    06/24/15        4480          dgilling       implement based on Date class.
#    Jun 23, 2016    5696          rjpeter        Make String version match java.
#

from dynamicserialize.dstypes.java.util import Date
from time import gmtime, strftime


class Timestamp(Date):

    def __init__(self, time=None):
        super(Timestamp, self).__init__(time)

    def __repr__(self):
        return strftime("%Y-%m-%d %H:%M:%S.", gmtime(self.time/1000.0)) + \
               '{:03d}'.format(self.time % 1000)
