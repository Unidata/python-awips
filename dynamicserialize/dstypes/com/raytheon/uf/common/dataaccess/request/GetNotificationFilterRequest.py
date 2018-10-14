#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    05/26/16        2416          rjpeter        Initial Creation.
#
#

from dynamicserialize.dstypes.com.raytheon.uf.common.dataaccess.request import AbstractDataAccessRequest


class GetNotificationFilterRequest(AbstractDataAccessRequest):

    def __init__(self):
        super(GetNotificationFilterRequest, self).__init__()
