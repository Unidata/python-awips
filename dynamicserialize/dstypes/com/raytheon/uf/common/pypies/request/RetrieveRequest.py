

class RetrieveRequest(object):

    def __init__(self):
        self.group = None
        self.dataset = None
        self.request = None
        self.filename = None

    def getGroup(self):
        return self.group

    def setGroup(self, group):
        self.group = group

    def getDataset(self):
        return self.dataset

    def setDataset(self, dataset):
        self.dataset = dataset

    def getRequest(self):
        return self.request

    def setRequest(self, request):
        self.request = request

    def getFilename(self):
        return self.filename

    def setFilename(self, filename):
        self.filename = filename
