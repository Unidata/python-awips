#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    07/23/14         #3185        njensen        Initial Creation.
#
#

from dynamicserialize.dstypes.com.raytheon.uf.common.dataaccess.request import AbstractDataAccessRequest


class GetAvailableLevelsRequest(AbstractDataAccessRequest):

    def __init__(self):
        super(GetAvailableLevelsRequest, self).__init__()
