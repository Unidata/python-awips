

class DeleteRequest(object):

    def __init__(self):
        self.datasets = None
        self.groups = None
        self.filename = None

    def getDatasets(self):
        return self.datasets

    def setDatasets(self, datasets):
        self.datasets = datasets

    def getGroups(self):
        return self.groups

    def setGroups(self, groups):
        self.groups = groups

    def getFilename(self):
        return self.filename

    def setFilename(self, filename):
        self.filename = filename
