

class GroupsRequest(object):

    def __init__(self):
        self.groups = None
        self.request = None
        self.filename = None

    def getGroups(self):
        return self.groups

    def setGroups(self, groups):
        self.groups = groups

    def getRequest(self):
        return self.request

    def setRequest(self, request):
        self.request = request

    def getFilename(self):
        return self.filename

    def setFilename(self, filename):
        self.filename = filename
