#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    05/28/13         #2023        dgilling       Initial Creation.
#
#

from six import with_metaclass
import abc


class AbstractDataAccessRequest(with_metaclass(abc.ABCMeta, object)):
    def __init__(self):
        self.requestParameters = None

    def getRequestParameters(self):
        return self.requestParameters

    def setRequestParameters(self, requestParameters):
        self.requestParameters = requestParameters

