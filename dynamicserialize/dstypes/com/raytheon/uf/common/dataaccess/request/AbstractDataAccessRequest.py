##
##

# File auto-generated against equivalent DynamicSerialize Java class
# and then modified post-generation to make it a abstract base class.
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    05/28/13         #2023        dgilling       Initial Creation.
#
#

import abc


class AbstractDataAccessRequest(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.requestParameters = None

    def getRequestParameters(self):
        return self.requestParameters

    def setRequestParameters(self, requestParameters):
        self.requestParameters = requestParameters

