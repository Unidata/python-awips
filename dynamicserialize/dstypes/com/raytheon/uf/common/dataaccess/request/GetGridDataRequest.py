##
##

# File auto-generated against equivalent DynamicSerialize Java class
# and then modified post-generation to make it sub class
# AbstractDataAccessRequest.
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    05/28/13         #2023        dgilling       Initial Creation.
#
#


from dynamicserialize.dstypes.com.raytheon.uf.common.dataaccess.request import AbstractDataAccessRequest

class GetGridDataRequest(AbstractDataAccessRequest):

    def __init__(self):
        super(GetGridDataRequest, self).__init__()
        self.requestedTimes = None
        self.requestedPeriod = None

    def getRequestedTimes(self):
        return self.requestedTimes

    def setRequestedTimes(self, requestedTimes):
        self.requestedTimes = requestedTimes

    def getRequestedPeriod(self):
        return self.requestedPeriod

    def setRequestedPeriod(self, requestedPeriod):
        self.requestedPeriod = requestedPeriod
