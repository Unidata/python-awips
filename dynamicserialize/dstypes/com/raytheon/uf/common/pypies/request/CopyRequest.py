

class CopyRequest(object):

    def __init__(self):
        self.repack = None
        self.repackCompression = None
        self.outputDir = None
        self.minMillisSinceLastChange = None
        self.maxMillisSinceLastChange = None
        self.filename = None

    def getRepack(self):
        return self.repack

    def setRepack(self, repack):
        self.repack = repack

    def getRepackCompression(self):
        return self.repackCompression

    def setRepackCompression(self, repackCompression):
        self.repackCompression = repackCompression

    def getOutputDir(self):
        return self.outputDir

    def setOutputDir(self, outputDir):
        self.outputDir = outputDir

    def getMinMillisSinceLastChange(self):
        return self.minMillisSinceLastChange

    def setMinMillisSinceLastChange(self, minMillisSinceLastChange):
        self.minMillisSinceLastChange = minMillisSinceLastChange

    def getMaxMillisSinceLastChange(self):
        return self.maxMillisSinceLastChange

    def setMaxMillisSinceLastChange(self, maxMillisSinceLastChange):
        self.maxMillisSinceLastChange = maxMillisSinceLastChange

    def getFilename(self):
        return self.filename

    def setFilename(self, filename):
        self.filename = filename
