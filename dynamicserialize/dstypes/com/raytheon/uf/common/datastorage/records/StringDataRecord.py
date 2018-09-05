
# File auto-generated against equivalent DynamicSerialize Java class
# and then modified by njensen

class StringDataRecord(object):

    def __init__(self):
        self.stringData = None
        self.maxLength = None
        self.name = None
        self.dimension = None
        self.sizes = None
        self.maxSizes = None
        self.props = None
        self.minIndex = None
        self.group = None
        self.dataAttributes = None
        self.fillValue = None
        self.maxChunkSize = None
        self.numpyData = None

    def getStringData(self):
        return self.stringData

    def setStringData(self, stringData):
        self.stringData = stringData

    def getMaxLength(self):
        return self.maxLength

    def setMaxLength(self, maxLength):
        self.maxLength = maxLength

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getDimension(self):
        return self.dimension

    def setDimension(self, dimension):
        self.dimension = dimension

    def getSizes(self):
        return self.sizes

    def setSizes(self, sizes):
        self.sizes = sizes

    def getMaxSizes(self):
        return self.maxSizes

    def setMaxSizes(self, maxSizes):
        self.maxSizes = maxSizes

    def getProps(self):
        return self.props

    def setProps(self, props):
        self.props = props

    def getMinIndex(self):
        return self.minIndex

    def setMinIndex(self, minIndex):
        self.minIndex = minIndex

    def getGroup(self):
        return self.group

    def setGroup(self, group):
        self.group = group

    def getDataAttributes(self):
        return self.dataAttributes

    def setDataAttributes(self, dataAttributes):
        self.dataAttributes = dataAttributes

    def getFillValue(self):
        return self.fillValue

    def setFillValue(self, fillValue):
        self.fillValue = fillValue

    def getMaxChunkSize(self):
        return self.maxChunkSize

    def setMaxChunkSize(self, maxChunkSize):
        self.maxChunkSize = maxChunkSize

    def retrieveDataObject(self):
        if not self.numpyData:
            import numpy
            from h5py import h5t
            if self.maxLength:
                dtype = h5t.py_create('S' + str(self.maxLength))
            else:
                from pypies.impl.H5pyDataStore import vlen_str_type as dtype
            #dtype.set_strpad(h5t.STR_NULLTERM)
            numpyData = numpy.asarray(self.getStringData(), dtype)
        return numpyData

    def putDataObject(self, obj):
        self.setStringData(obj)
