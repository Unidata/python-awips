

class DeleteFilesRequest(object):

    def __init__(self):
        self.datesToDelete = None

    def getDatesToDelete(self):
        return self.datesToDelete

    def setDatesToDelete(self, datesToDelete):
        self.datesToDelete = datesToDelete

    def getFilename(self):
        return self.filename

    def setFilename(self, filename):
        self.filename = filename
