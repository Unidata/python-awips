#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    07/23/14         #3185        njensen        Initial Creation.
#    07/30/14         #3185        njensen        Renamed valid to optional
#
#

from dynamicserialize.dstypes.com.raytheon.uf.common.dataaccess.request import AbstractIdentifierRequest


class GetOptionalIdentifiersRequest(AbstractIdentifierRequest):

    def __init__(self):
        super(GetOptionalIdentifiersRequest, self).__init__()
