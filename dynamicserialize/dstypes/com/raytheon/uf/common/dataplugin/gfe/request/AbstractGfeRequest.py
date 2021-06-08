import abc
from six import with_metaclass


class AbstractGfeRequest(with_metaclass(abc.ABCMeta, object)):
    @abc.abstractmethod
    def __init__(self):
        self.siteID = None
        self.workstationID = None

    def getSiteID(self):
        return self.siteID

    def setSiteID(self, siteID):
        self.siteID = siteID

    def getWorkstationID(self):
        return self.workstationID

    def setWorkstationID(self, workstationID):
        self.workstationID = workstationID
