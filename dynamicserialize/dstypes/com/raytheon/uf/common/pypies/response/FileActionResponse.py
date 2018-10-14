

class FileActionResponse(object):

    def __init__(self):
        self.successfulFiles = None
        self.failedFiles = None

    def getSuccessfulFiles(self):
        return self.successfulFiles

    def setSuccessfulFiles(self, successfulFiles):
        self.successfulFiles = successfulFiles

    def getFailedFiles(self):
        return self.failedFiles

    def setFailedFiles(self, failedFiles):
        self.failedFiles = failedFiles
