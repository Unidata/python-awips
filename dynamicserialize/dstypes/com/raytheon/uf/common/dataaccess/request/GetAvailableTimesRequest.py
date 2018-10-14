#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    05/28/13         #2023        dgilling       Initial Creation.
#    03/03/14         #2673        bsteffen       Add ability to query only ref times.
#
#

from dynamicserialize.dstypes.com.raytheon.uf.common.dataaccess.request import AbstractDataAccessRequest


class GetAvailableTimesRequest(AbstractDataAccessRequest):

    def __init__(self):
        super(GetAvailableTimesRequest, self).__init__()
        self.refTimeOnly = False

    def getRefTimeOnly(self):
        return self.refTimeOnly

    def setRefTimeOnly(self, refTimeOnly):
        self.refTimeOnly = refTimeOnly
