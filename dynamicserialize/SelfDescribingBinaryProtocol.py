#
# Partially compatible AWIPS-II Thrift Binary Protocol
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    11/11/09                      chammack        Initial Creation.
#    06/09/10                      njensen            Added float, list methods
#    Apr 24, 2015    4425          nabowle         Add F64List support.
#
#

import struct
import numpy
from thrift.protocol.TProtocol import *
from thrift.protocol.TBinaryProtocol import *

FLOAT = 64

intList = numpy.dtype(numpy.int32).newbyteorder('>')
floatList = numpy.dtype(numpy.float32).newbyteorder('>')
longList = numpy.dtype(numpy.int64).newbyteorder('>')
shortList = numpy.dtype(numpy.int16).newbyteorder('>')
byteList = numpy.dtype(numpy.int8).newbyteorder('>')
doubleList = numpy.dtype(numpy.float64).newbyteorder('>')


class SelfDescribingBinaryProtocol(TBinaryProtocol):

    def readFieldBegin(self):
        ftype = self.readByte()
        if ftype == TType.STOP:
            return None, ftype, 0
        name = self.readString()
        fid = self.readI16()
        return name, ftype, fid

    def readStructBegin(self):
        return self.readString()

    def writeStructBegin(self, name):
        self.writeString(name)

    def writeFieldBegin(self, name, ftype, fid):
        self.writeByte(ftype)
        self.writeString(name)
        self.writeI16(fid)

    def readFloat(self):
        d = self.readI32()
        dAsBytes = struct.pack('i', d)
        f = struct.unpack('f', dAsBytes)
        return f[0]

    def writeFloat(self, f):
        dAsBytes = struct.pack('f', f)
        i = struct.unpack('i', dAsBytes)
        self.writeI32(i[0])

    def readI32List(self, sz):
        buff = self.trans.readAll(4*sz)
        val = numpy.frombuffer(buff, dtype=intList, count=sz)
        return val

    def readF32List(self, sz):
        buff = self.trans.readAll(4*sz)
        val = numpy.frombuffer(buff, dtype=floatList, count=sz)
        return val

    def readF64List(self, sz):
        buff = self.trans.readAll(8*sz)
        val = numpy.frombuffer(buff, dtype=doubleList, count=sz)
        return val

    def readI64List(self, sz):
        buff = self.trans.readAll(8*sz)
        val = numpy.frombuffer(buff, dtype=longList, count=sz)
        return val

    def readI16List(self, sz):
        buff = self.trans.readAll(2*sz)
        val = numpy.frombuffer(buff, dtype=shortList, count=sz)
        return val

    def readI8List(self, sz):
        buff = self.trans.readAll(sz)
        val = numpy.frombuffer(buff, dtype=byteList, count=sz)
        return val

    def writeI32List(self, buff):
        b = numpy.asarray(buff, intList)
        self.trans.write(numpy.getbuffer(b))

    def writeF32List(self, buff):
        b = numpy.asarray(buff, floatList)
        self.trans.write(numpy.getbuffer(b))

    def writeF64List(self, buff):
        b = numpy.asarray(buff, doubleList)
        self.trans.write(numpy.getbuffer(b))

    def writeI64List(self, buff):
        b = numpy.asarray(buff, longList)
        self.trans.write(numpy.getbuffer(b))

    def writeI16List(self, buff):
        b = numpy.asarray(buff, shortList)
        self.trans.write(numpy.getbuffer(b))

    def writeI8List(self, buff):
        b = numpy.asarray(buff, byteList)
        self.trans.write(numpy.getbuffer(b))
