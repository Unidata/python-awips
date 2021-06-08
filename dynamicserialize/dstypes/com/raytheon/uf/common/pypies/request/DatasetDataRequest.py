

class DatasetDataRequest(object):

    def __init__(self):
        self.datasetGroupPath = None
        self.request = None
        self.filename = None

    def getDatasetGroupPath(self):
        return self.datasetGroupPath

    def setDatasetGroupPath(self, datasetGroupPath):
        self.datasetGroupPath = datasetGroupPath

    def getRequest(self):
        return self.request

    def setRequest(self, request):
        self.request = request

    def getFilename(self):
        return self.filename

    def setFilename(self, filename):
        self.filename = filename
