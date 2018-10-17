from dynamicserialize.dstypes.com.raytheon.uf.common.datastorage.records import AbstractDataRecord


class ByteDataRecord(AbstractDataRecord):

    def __init__(self):
        super(ByteDataRecord, self).__init__()
        self.byteData = None

    def getByteData(self):
        return self.byteData

    def setByteData(self, byteData):
        self.byteData = byteData

    def retrieveDataObject(self):
        return self.getByteData()

    def putDataObject(self, obj):
        self.setByteData(obj)
