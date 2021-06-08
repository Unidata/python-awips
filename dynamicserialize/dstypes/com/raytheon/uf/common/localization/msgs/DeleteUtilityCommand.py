

class DeleteUtilityCommand(object):

    def __init__(self):
        self.filename = None
        self.context = None
        self.myContextName = None

    def getFilename(self):
        return self.filename

    def setFilename(self, filename):
        self.filename = filename

    def getContext(self):
        return self.context

    def setContext(self, context):
        self.context = context

    def getMyContextName(self):
        return self.myContextName

    def setMyContextName(self, contextName):
        self.myContextName = str(contextName)
