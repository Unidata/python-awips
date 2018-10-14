#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    07/23/14         #3185        njensen        Initial Creation.
#
#

from dynamicserialize.dstypes.com.raytheon.uf.common.dataaccess.request import AbstractIdentifierRequest


class GetRequiredIdentifiersRequest(AbstractIdentifierRequest):

    def __init__(self):
        super(GetRequiredIdentifiersRequest, self).__init__()
