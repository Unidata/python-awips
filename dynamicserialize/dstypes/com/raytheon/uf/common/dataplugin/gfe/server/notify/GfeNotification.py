#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    10/07/2014       3684         randerso       Manually updated to add sourceID
#

import abc
from six import with_metaclass


class GfeNotification(with_metaclass(abc.ABCMeta, object)):
    @abc.abstractmethod
    def __init__(self):
        self.siteID = None
        self.sourceID = None

    def getSiteID(self):
        return self.siteID

    def setSiteID(self, siteID):
        self.siteID = siteID

    def getSourceID(self):
        return self.sourceID

    def setSourceID(self, sourceID):
        self.sourceID = sourceID
