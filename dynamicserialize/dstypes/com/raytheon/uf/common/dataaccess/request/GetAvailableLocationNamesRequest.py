#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    05/28/13         #2023        dgilling       Initial Creation.
#
#

from dynamicserialize.dstypes.com.raytheon.uf.common.dataaccess.request import AbstractDataAccessRequest


class GetAvailableLocationNamesRequest(AbstractDataAccessRequest):

    def __init__(self):
        super(GetAvailableLocationNamesRequest, self).__init__()
