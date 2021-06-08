from dynamicserialize.dstypes.com.raytheon.uf.common.datastorage.records import AbstractDataRecord


class LongDataRecord(AbstractDataRecord):

    def __init__(self):
        super(LongDataRecord, self).__init__()
        self.longData = None

    def getLongData(self):
        return self.longData

    def setLongData(self, longData):
        self.longData = longData

    def retrieveDataObject(self):
        return self.getLongData()

    def putDataObject(self, obj):
        self.setLongData(obj)
