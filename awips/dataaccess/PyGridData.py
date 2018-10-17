#
# Implements IGridData for use by native Python clients to the Data Access
# Framework.
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    06/03/13         #2023        dgilling      Initial Creation.
#    10/13/16         #5916        bsteffen      Correct grid shape, allow lat/lon
#    11/10/16         #5900        bsteffen      Correct grid shape
#                                                to be requested by a delegate
#
#

import numpy
import warnings
import six

from awips.dataaccess import IGridData
from awips.dataaccess import PyData

NO_UNIT_CONVERT_WARNING = """
The ability to unit convert grid data is not currently available in this version of the Data Access Framework.
"""


class PyGridData(IGridData, PyData.PyData):

    def __init__(self, gridDataRecord, nx, ny, latLonGrid=None, latLonDelegate=None):
        PyData.PyData.__init__(self, gridDataRecord)
        nx = nx
        ny = ny
        self.__parameter = gridDataRecord.getParameter()
        self.__unit = gridDataRecord.getUnit()
        self.__gridData = numpy.reshape(numpy.array(gridDataRecord.getGridData()), (ny, nx))
        self.__latLonGrid = latLonGrid
        self.__latLonDelegate = latLonDelegate

    def getParameter(self):
        return self.__parameter

    def getUnit(self):
        if six.PY2:
            return self.__unit
        if self.__unit is not None and not isinstance(self.__unit, str):
            return self.__unit.decode('utf-8')
        return self.__unit

    def getRawData(self, unit=None):
        # TODO: Find a proper python library that deals will with numpy and
        # javax.measure style unit strings and hook it in to this method to
        # allow end-users to perform unit conversion for grid data.
        if unit is not None:
            warnings.warn(NO_UNIT_CONVERT_WARNING, stacklevel=2)
        return self.__gridData

    def getLatLonCoords(self):
        if self.__latLonGrid is not None:
            return self.__latLonGrid
        elif self.__latLonDelegate is not None:
            return self.__latLonDelegate()
        return self.__latLonGrid
