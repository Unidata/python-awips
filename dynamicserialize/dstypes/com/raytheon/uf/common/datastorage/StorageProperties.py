

class StorageProperties(object):

    def __init__(self):
        self.compression = None
        self.chunked = None

    def getCompression(self):
        return self.compression

    def setCompression(self, compression):
        self.compression = compression

    def getChunked(self):
        return self.chunked

    def setChunked(self, chunked):
        self.chunked = chunked
