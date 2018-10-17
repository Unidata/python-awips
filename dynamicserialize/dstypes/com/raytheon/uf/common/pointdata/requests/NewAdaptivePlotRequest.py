

class NewAdaptivePlotRequest(object):

    def __init__(self):
        self.fileContents = None
        self.fileName = None
        self.bundleName = None
        self.description = None

    def getFileContents(self):
        return self.fileContents

    def setFileContents(self, fileContents):
        self.fileContents = fileContents

    def getFileName(self):
        return self.fileName

    def setFileName(self, fileName):
        self.fileName = fileName

    def getBundleName(self):
        return self.bundleName

    def setBundleName(self, bundleName):
        self.bundleName = bundleName

    def getDescription(self):
        return self.description

    def setDescription(self, description):
        self.description = description
