#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    xx/xx/??                      dgilling       Initial Creation.
#    03/13/13         1759         dgilling       Add software history header.
#    05/13/15         4427         dgilling       Add siteIdOverride field.
#
#

from dynamicserialize.dstypes.com.raytheon.uf.common.dataplugin.gfe.request import AbstractGfeRequest
from dynamicserialize.dstypes.com.raytheon.uf.common.message import WsId


class ExecuteIfpNetCDFGridRequest(AbstractGfeRequest):

    def __init__(self, outputFilename=None, parmList=[], databaseID=None,
                 startTime=None, endTime=None, mask=None, geoInfo=False,
                 compressFile=False, configFileName=None, compressFileFactor=0,
                 trim=False, krunch=False, userID=None, logFileName=None, siteIdOverride=None):
        super(ExecuteIfpNetCDFGridRequest, self).__init__()
        self.outputFilename = outputFilename
        self.parmList = parmList
        self.databaseID = databaseID
        self.startTime = startTime
        self.endTime = endTime
        self.mask = mask
        self.geoInfo = geoInfo
        self.compressFile = compressFile
        self.configFileName = configFileName
        self.compressFileFactor = compressFileFactor
        self.trim = trim
        self.krunch = krunch
        self.userID = userID
        self.logFileName = logFileName
        self.siteIdOverride = siteIdOverride
        if self.userID is not None:
            self.workstationID = WsId(progName='ifpnetCDF', userName=self.userID)
        if self.databaseID is not None:
            self.siteID = self.databaseID.getSiteId()

    def __cstr__(self):
        retVal = "workstationID: " + str(self.workstationID) + ", "
        retVal += "siteID: " + str(self.siteID) + ", "
        retVal += "outputFilename: " + str(self.outputFilename) + ", "
        retVal += "parmList: " + str(self.parmList) + ", "
        retVal += "databaseID: " + str(self.databaseID) + ", "
        retVal += "startTime: " + str(self.startTime) + ", "
        retVal += "endTime: " + str(self.endTime) + ", "
        retVal += "mask: " + str(self.mask) + ", "
        retVal += "geoInfo: " + str(self.geoInfo) + ", "
        retVal += "compressFile: " + str(self.compressFile) + ", "
        retVal += "configFileName: " + str(self.configFileName) + ", "
        retVal += "compressFileFactor: " + str(self.compressFileFactor) + ", "
        retVal += "trim: " + str(self.trim) + ", "
        retVal += "krunch: " + str(self.krunch) + ", "
        retVal += "userID: " + str(self.userID) + ", "
        retVal += "logFileName: " + str(self.logFileName) + ", "
        retVal += "siteIdOverride: " + str(self.siteIdOverride)
        return retVal

    def __str__(self):
        return "ExecuteIfpNetCDFGridRequest[" + self.__cstr__() + "]"

    def __repr__(self):
        return "ExecuteIfpNetCDFGridRequest(" + self.__cstr__() + ")"

    def getOutputFilename(self):
        return self.outputFilename

    def setOutputFilename(self, outputFilename):
        self.outputFilename = outputFilename

    def getParmList(self):
        return self.parmList

    def setParmList(self, parmList):
        self.parmList = parmList

    def getDatabaseID(self):
        return self.databaseID

    def setDatabaseID(self, databaseID):
        self.databaseID = databaseID

    def getStartTime(self):
        return self.startTime

    def setStartTime(self, startTime):
        self.startTime = startTime

    def getEndTime(self):
        return self.endTime

    def setEndTime(self, endTime):
        self.endTime = endTime

    def getMask(self):
        return self.mask

    def setMask(self, mask):
        self.mask = mask

    def getGeoInfo(self):
        return self.geoInfo

    def setGeoInfo(self, geoInfo):
        self.geoInfo = geoInfo

    def getCompressFile(self):
        return self.compressFile

    def setCompressFile(self, compressFile):
        self.compressFile = compressFile

    def getConfigFileName(self):
        return self.configFileName

    def setConfigFileName(self, configFileName):
        self.configFileName = configFileName

    def getCompressFileFactor(self):
        return self.compressFileFactor

    def setCompressFileFactor(self, compressFileFactor):
        self.compressFileFactor = compressFileFactor

    def getTrim(self):
        return self.trim

    def setTrim(self, trim):
        self.trim = trim

    def getKrunch(self):
        return self.krunch

    def setKrunch(self, krunch):
        self.krunch = krunch

    def getUserID(self):
        return self.userID

    def setUserID(self, userID):
        self.userID = userID

    def getLogFileName(self):
        return self.logFileName

    def setLogFileName(self, logFileName):
        self.logFileName = logFileName

    def getSiteIdOverride(self):
        return self.siteIdOverride

    def setSiteIdOverride(self, siteIdOverride):
        self.siteIdOverride = siteIdOverride
