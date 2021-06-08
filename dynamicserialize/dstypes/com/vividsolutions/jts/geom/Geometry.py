# This class is a dummy implementation of the
# com.vividsolutions.jts.geom.Geometry class. It was simply created to allow
# serialization/deserialization of GridLocation objects. This should be
# reimplemented if useful work needs to be performed against serialized
# Geometry objects.


class Geometry(object):

    def __init__(self):
        self.binaryData = None

    def getBinaryData(self):
        return self.binaryData

    def setBinaryData(self, data):
        self.binaryData = data
