##
##

# File auto-generated against equivalent DynamicSerialize Java class
# and then modified post-generation to use AbstractResponseData.
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    06/04/13         #2023        dgilling       Initial Creation.
#
#


from dynamicserialize.dstypes.com.raytheon.uf.common.dataaccess.response import AbstractResponseData

class GridResponseData(AbstractResponseData):

    def __init__(self):
        super(GridResponseData, self).__init__()
        self.parameter = None
        self.unit = None
        self.gridData = None

    def getParameter(self):
        return self.parameter

    def setParameter(self, parameter):
        self.parameter = parameter

    def getUnit(self):
        return self.unit

    def setUnit(self, unit):
        self.unit = unit

    def getGridData(self):
        return self.gridData

    def setGridData(self, gridData):
        self.gridData = gridData
