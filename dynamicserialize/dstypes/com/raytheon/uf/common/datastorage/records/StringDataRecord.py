from dynamicserialize.dstypes.com.raytheon.uf.common.datastorage.records import AbstractDataRecord


class StringDataRecord(AbstractDataRecord):

    def __init__(self):
        super(StringDataRecord, self).__init__()
        self.stringData = None
        self.maxLength = None
        self.numpyData = None

    def getStringData(self):
        return self.stringData

    def setStringData(self, stringData):
        self.stringData = stringData

    def getMaxLength(self):
        return self.maxLength

    def setMaxLength(self, maxLength):
        self.maxLength = maxLength

    def retrieveDataObject(self):
        if not self.numpyData:
            import numpy
            from h5py import h5t
            if self.maxLength:
                dtype = h5t.py_create('S' + str(self.maxLength))
            else:
                from pypies.impl.H5pyDataStore import vlen_str_type as dtype
            # dtype.set_strpad(h5t.STR_NULLTERM)
            return numpy.asarray(self.getStringData(), dtype)
        return self.numpyData

    def putDataObject(self, obj):
        self.setStringData(obj)
