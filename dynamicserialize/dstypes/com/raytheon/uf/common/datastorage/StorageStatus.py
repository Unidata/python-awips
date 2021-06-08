

class StorageStatus(object):

    def __init__(self):
        self.operationPerformed = None
        self.indexOfAppend = None

    def getOperationPerformed(self):
        return self.operationPerformed

    def setOperationPerformed(self, operationPerformed):
        self.operationPerformed = operationPerformed

    def getIndexOfAppend(self):
        return self.indexOfAppend

    def setIndexOfAppend(self, indexOfAppend):
        self.indexOfAppend = indexOfAppend
