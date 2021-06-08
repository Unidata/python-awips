from dynamicserialize.dstypes.com.raytheon.uf.common.datastorage.records import AbstractDataRecord


class FloatDataRecord(AbstractDataRecord):

    def __init__(self):
        super(FloatDataRecord, self).__init__()
        self.floatData = None

    def getFloatData(self):
        return self.floatData

    def setFloatData(self, floatData):
        self.floatData = floatData

    def retrieveDataObject(self):
        return self.getFloatData()

    def putDataObject(self, obj):
        self.setFloatData(obj)
