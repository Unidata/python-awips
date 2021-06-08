

class StoreRequest(object):

    def __init__(self):
        self.op = None
        self.records = None
        self.filename = None

    def getOp(self):
        return self.op

    def setOp(self, op):
        self.op = op

    def getRecords(self):
        return self.records

    def setRecords(self, records):
        self.records = records

    def getFilename(self):
        return self.filename

    def setFilename(self, filename):
        self.filename = filename
