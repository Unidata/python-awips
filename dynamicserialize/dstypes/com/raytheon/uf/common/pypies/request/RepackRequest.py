

class RepackRequest(object):

    def __init__(self):
        self.compression = None
        self.filename = None

    def getCompression(self):
        return self.compression

    def setCompression(self, compression):
        self.compression = compression

    def getFilename(self):
        return self.filename

    def setFilename(self, filename):
        self.filename = filename
