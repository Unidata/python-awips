
# File auto-generated against equivalent DynamicSerialize Java class
#
#      SOFTWARE HISTORY
#
#     Date            Ticket#       Engineer       Description
#     ------------    ----------    -----------    --------------------------
#     Apr 11, 2023    2033903       mapeters       Generated

class FileUpdatedMessage(object):

    def __init__(self):
        self.timeStamp = None
        self.fileName = None
        self.changeType = None
        self.context = None
        self.checkSum = None

    def getTimeStamp(self):
        return self.timeStamp

    def setTimeStamp(self, timeStamp):
        self.timeStamp = timeStamp

    def getFileName(self):
        return self.fileName

    def setFileName(self, fileName):
        self.fileName = fileName

    def getChangeType(self):
        return self.changeType

    def setChangeType(self, changeType):
        self.changeType = changeType

    def getContext(self):
        return self.context

    def setContext(self, context):
        self.context = context

    def getCheckSum(self):
        return self.checkSum

    def setCheckSum(self, checkSum):
        self.checkSum = checkSum

