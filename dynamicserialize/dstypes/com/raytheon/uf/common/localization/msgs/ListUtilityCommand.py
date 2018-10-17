

class ListUtilityCommand(object):

    def __init__(self):
        self.subDirectory = None
        self.recursive = None
        self.filesOnly = None
        self.localizedSite = None
        self.context = None

    def getSubDirectory(self):
        return self.subDirectory

    def setSubDirectory(self, subDirectory):
        self.subDirectory = subDirectory

    def getRecursive(self):
        return self.recursive

    def setRecursive(self, recursive):
        self.recursive = recursive

    def getFilesOnly(self):
        return self.filesOnly

    def setFilesOnly(self, filesOnly):
        self.filesOnly = filesOnly

    def getLocalizedSite(self):
        return self.localizedSite

    def setLocalizedSite(self, localizedSite):
        self.localizedSite = localizedSite

    def getContext(self):
        return self.context

    def setContext(self, context):
        self.context = context
