

class RetrieveResponse(object):

    def __init__(self):
        self.records = None

    def getRecords(self):
        return self.records

    def setRecords(self, records):
        self.records = records
