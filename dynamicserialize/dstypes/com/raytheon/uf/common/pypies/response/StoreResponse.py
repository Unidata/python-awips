

class StoreResponse(object):

    def __init__(self):
        self.status = None
        self.exceptions = None
        self.failedRecords = None

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

    def getExceptions(self):
        return self.exceptions

    def setExceptions(self, exceptions):
        self.exceptions = exceptions

    def getFailedRecords(self):
        return self.failedRecords

    def setFailedRecords(self, failedRecords):
        self.failedRecords = failedRecords
