

class SuccessfulExecution(object):

    def __init__(self):
        self.response = None
        self.updatedData = None

    def getResponse(self):
        return self.response

    def setResponse(self, response):
        self.response = response

    def getUpdatedData(self):
        return self.updatedData

    def setUpdatedData(self, updatedData):
        self.updatedData = updatedData
