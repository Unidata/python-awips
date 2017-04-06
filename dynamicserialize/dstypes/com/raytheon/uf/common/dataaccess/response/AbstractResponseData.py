##
##

# File auto-generated against equivalent DynamicSerialize Java class

import abc
from six import with_metaclass


class AbstractResponseData(with_metaclass(abc.ABCMeta, object)):
    @abc.abstractmethod
    def __init__(self):
        self.time = None
        self.level = None
        self.locationName = None
        self.attributes = None

    def getTime(self):
        return self.time

    def setTime(self, time):
        self.time = time

    def getLevel(self):
        return self.level

    def setLevel(self, level):
        self.level = level

    def getLocationName(self):
        return self.locationName

    def setLocationName(self, locationName):
        self.locationName = locationName

    def getAttributes(self):
        return self.attributes

    def setAttributes(self, attributes):
        self.attributes = attributes

