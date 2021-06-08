

class CreateDatasetRequest(object):

    def __init__(self):
        self.record = None
        self.filename = None

    def getRecord(self):
        return self.record

    def setRecord(self, record):
        self.record = record

    def getFilename(self):
        return self.filename

    def setFilename(self, filename):
        self.filename = filename
