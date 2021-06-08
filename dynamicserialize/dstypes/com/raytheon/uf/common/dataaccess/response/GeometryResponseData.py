#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    06/04/13         #2023        dgilling       Initial Creation.
#    01/06/14         #2537        bsteffen       Store geometry index instead of WKT.
#    06/30/15         #4569        nabowle        Rename *WKT* to *WKB*.
#
#

from dynamicserialize.dstypes.com.raytheon.uf.common.dataaccess.response import AbstractResponseData


class GeometryResponseData(AbstractResponseData):

    def __init__(self):
        super(GeometryResponseData, self).__init__()
        self.dataMap = None
        self.geometryWKBindex = None

    def getDataMap(self):
        return self.dataMap

    def setDataMap(self, dataMap):
        self.dataMap = dataMap

    def getGeometryWKBindex(self):
        return self.geometryWKBindex

    def setGeometryWKBindex(self, geometryWKBindex):
        self.geometryWKBindex = geometryWKBindex
