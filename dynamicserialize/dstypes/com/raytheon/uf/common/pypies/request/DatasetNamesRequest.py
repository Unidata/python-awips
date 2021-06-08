

class DatasetNamesRequest(object):

    def __init__(self):
        self.group = None
        self.filename = None

    def getGroup(self):
        return self.group

    def setGroup(self, group):
        self.group = group

    def getFilename(self):
        return self.filename

    def setFilename(self, filename):
        self.filename = filename
