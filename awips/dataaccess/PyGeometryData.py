#
# Implements IGeometryData for use by native Python clients to the Data Access
# Framework.
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    06/03/13                      dgilling       Initial Creation.
#    01/06/14        2537          bsteffen       Share geometry WKT.
#    03/19/14        2882          dgilling       Raise an exception when getNumber()
#                                                 is called for data that is not a
#                                                 numeric Type.
#    06/09/16        5574          mapeters       Handle 'SHORT' type in getNumber().
#    10/05/18                      mjames@ucar    Encode/decode string, number val, and type
#
#

from awips.dataaccess import IGeometryData
from awips.dataaccess import PyData
import six


class PyGeometryData(IGeometryData, PyData.PyData):

    def __init__(self, geoDataRecord, geometry):
        PyData.PyData.__init__(self, geoDataRecord)
        self.__geometry = geometry
        self.__dataMap = {}
        tempDataMap = geoDataRecord.getDataMap()
        for key, value in list(tempDataMap.items()):
            self.__dataMap[key] = (value[0], value[1], value[2])

    def getGeometry(self):
        return self.__geometry

    def getParameters(self):
        if six.PY2:
            return list(self.__dataMap.keys())
        else:
            return [x.decode('utf-8') for x in list(self.__dataMap.keys())]

    def getString(self, param):
        if six.PY2:
            return self.__dataMap[param][0]
        value = self.__dataMap[param.encode('utf-8')][0]
        if isinstance(value, bytes):
            return str(value.decode('utf-8'))
        return str(value)

    def getNumber(self, param):
        t = self.getType(param)
        if six.PY2:
            value = self.__dataMap[param][0]
        else:
            value = self.__dataMap[param.encode('utf-8')][0]
        if t == 'INT' or t == 'SHORT' or t == 'LONG':
            return int(value)
        elif t == 'FLOAT':
            return float(value)
        elif t == 'DOUBLE':
            return float(value)
        else:
            raise TypeError("Data for parameter " + param + " is not a numeric type.")

    def getUnit(self, param):
        if six.PY2:
            return self.__dataMap[param][2]
        unit = self.__dataMap[param.encode('utf-8')][2]
        if unit is not None:
            return unit.decode('utf-8')
        return unit

    def getType(self, param):
        if six.PY2:
            return self.__dataMap[param][1]
        datatype = self.__dataMap[param.encode('utf-8')][1]
        if datatype is not None:
            return datatype.decode('utf-8')
        return datatype
