##
##

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
#
#

from awips.dataaccess import IGeometryData
from awips.dataaccess import PyData

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
        return list(self.__dataMap.keys())

    def getString(self, param):
        value = self.__dataMap[param][0]
        return str(value)

    def getNumber(self, param):
        value = self.__dataMap[param][0]
        t = self.getType(param)
        if t == 'INT' or t == 'SHORT':
            return int(value)
        elif t == 'LONG':
            return int(value)
        elif t == 'FLOAT':
            return float(value)
        elif t == 'DOUBLE':
            return float(value)
        else:
            raise TypeError("Data for parameter " + param + " is not a numeric type.")

    def getUnit(self, param):
        return self.__dataMap[param][2]

    def getType(self, param):
        return self.__dataMap[param][1]
