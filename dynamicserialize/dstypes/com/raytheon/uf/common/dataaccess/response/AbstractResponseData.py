import abc
import six


class AbstractResponseData(six.with_metaclass(abc.ABCMeta, object)):
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
        if six.PY2:
            return self.locationName
        if self.locationName is not None:
            return self.locationName.decode('utf-8')
        return self.locationName

    def setLocationName(self, locationName):
        self.locationName = locationName

    def getAttributes(self):
        return self.attributes

    def setAttributes(self, attributes):
        self.attributes = attributes

