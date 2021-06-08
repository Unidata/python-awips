from dynamicserialize.dstypes.com.raytheon.uf.common.datastorage.records import AbstractDataRecord


class ShortDataRecord(AbstractDataRecord):

    def __init__(self):
        super(ShortDataRecord, self).__init__()
        self.shortData = None

    def getShortData(self):
        return self.shortData

    def setShortData(self, shortData):
        self.shortData = shortData

    def retrieveDataObject(self):
        return self.getShortData()

    def putDataObject(self, obj):
        self.setShortData(obj)
