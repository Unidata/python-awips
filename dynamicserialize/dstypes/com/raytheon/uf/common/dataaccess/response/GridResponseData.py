#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    06/04/13         #2023        dgilling       Initial Creation.
#
#

from dynamicserialize.dstypes.com.raytheon.uf.common.dataaccess.response import AbstractResponseData
import six


class GridResponseData(AbstractResponseData):

    def __init__(self):
        super(GridResponseData, self).__init__()
        self.parameter = None
        self.unit = None
        self.gridData = None

    def getParameter(self):
        if six.PY2:
            return self.parameter
        if self.parameter is not None:
            return self.parameter.decode('utf-8')
        return self.parameter

    def setParameter(self, parameter):
        self.parameter = parameter

    def getUnit(self):
        if six.PY2:
            return self.unit
        if self.unit is not None:
            return self.unit.decode('utf-8')
        return self.unit

    def setUnit(self, unit):
        self.unit = unit

    def getGridData(self):
        return self.gridData

    def setGridData(self, gridData):
        self.gridData = gridData
