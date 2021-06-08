from dynamicserialize.dstypes.com.raytheon.uf.common.datastorage.records import AbstractDataRecord


class IntegerDataRecord(AbstractDataRecord):

    def __init__(self):
        super(IntegerDataRecord, self).__init__()
        self.intData = None

    def getIntData(self):
        return self.intData

    def setIntData(self, intData):
        self.intData = intData

    def retrieveDataObject(self):
        return self.getIntData()

    def putDataObject(self, obj):
        self.setIntData(obj)
