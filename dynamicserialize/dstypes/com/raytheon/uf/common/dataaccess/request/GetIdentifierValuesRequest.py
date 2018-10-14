#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    04/15/2016      5379          tgurney        Initial creation
#
#

from dynamicserialize.dstypes.com.raytheon.uf.common.dataaccess.request import AbstractDataAccessRequest


class GetIdentifierValuesRequest(AbstractDataAccessRequest):

    def __init__(self):
        super(GetIdentifierValuesRequest, self).__init__()
        self.identifierKey = None

    def getIdentifierKey(self):
        return self.identifierKey

    def setIdentifierKey(self, identifierKey):
        self.identifierKey = identifierKey
