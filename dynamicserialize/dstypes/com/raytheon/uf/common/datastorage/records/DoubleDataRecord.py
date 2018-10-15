from dynamicserialize.dstypes.com.raytheon.uf.common.datastorage.records import AbstractDataRecord


class DoubleDataRecord(AbstractDataRecord):

    def __init__(self):
        super(DoubleDataRecord, self).__init__()
        self.doubleData = None

    def getDoubleData(self):
        return self.doubleData

    def setDoubleData(self, doubleData):
        self.doubleData = doubleData

    def retrieveDataObject(self):
        return self.getDoubleData()

    def putDataObject(self, obj):
        self.setDoubleData(obj)
