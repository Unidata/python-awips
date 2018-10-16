#
# Compressed version of a DataRecord.
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    12/02/16        5992          bsteffen       Initial Creation.
#    06/26/17        6341          rjpeter        Optimize decompress
#

import numpy
import zlib


class CompressedDataRecord(object):

    def __init__(self):
        self.type = None
        self.uncompressedData = None
        self.compressedData = None
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

    def getType(self):
        return self.type

    def setType(self, recordtype):
        self.type = recordtype

    def getCompressedData(self):
        return self.compressedData

    def setCompressedData(self, compressedData):
        self.compressedData = compressedData

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

    def determineStorageType(self):
        if self.type == "BYTE":
            return numpy.byte
        elif self.type == "SHORT":
            return numpy.short
        elif self.type == "INT":
            return numpy.int32
        elif self.type == "LONG":
            return numpy.int64
        elif self.type == "FLOAT":
            return numpy.float32
        elif self.type == "DOUBLE":
            return numpy.float64
        else:
            raise TypeError("Unexpected compressed type " + str(self.type))

    # utilize zlib directly to take advantage of passing in initial size of the
    # decompress buffer, which prevents repeated allocation of a growing buffer
    # for each chunk
    def decompress(self):
        datatype = numpy.dtype(self.determineStorageType()).newbyteorder('>')
        compressedBuffer = numpy.getbuffer(self.compressedData)
        self.compressedData = None
        uncompressedSize = datatype.itemsize
        for s in self.sizes:
            uncompressedSize *= s

        # zlib.MAX_WBITS | 16, add 16 to window bits to support gzip header/trailer
        # http://www.zlib.net/manual.html#Advanced
        decompressedBuffer = zlib.decompress(compressedBuffer, zlib.MAX_WBITS | 16, uncompressedSize)
        self.uncompressedData = numpy.frombuffer(decompressedBuffer, datatype)

    def retrieveDataObject(self):
        if self.uncompressedData is None:
            self.decompress()
        return self.uncompressedData

    def putDataObject(self, obj):
        self.compressedData = None
        self.uncompressedData = obj

    prepareStore = decompress
