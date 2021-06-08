

class DeleteUtilityResponse(object):

    def __init__(self):
        self.context = None
        self.pathName = None
        self.errorText = None
        self.timeStamp = None

    def getContext(self):
        return self.context

    def setContext(self, context):
        self.context = context

    def getPathName(self):
        return self.pathName

    def setPathName(self, pathName):
        self.pathName = pathName

    def getErrorText(self):
        return self.errorText

    def setErrorText(self, errorText):
        self.errorText = errorText

    def getTimeStamp(self):
        return self.timeStamp

    def setTimeStamp(self, timeStamp):
        self.timeStamp = timeStamp

    def getFormattedErrorMessage(self):
        return "Error deleting " + self.getContextRelativePath() + ": " + self.getErrorText()

    def getContextRelativePath(self):
        return str(self.getContext()) + "/" + self.getPathName()
