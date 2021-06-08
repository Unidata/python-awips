

class ListUtilityResponse(object):

    def __init__(self):
        self.entries = None
        self.context = None
        self.pathName = None
        self.errorText = None

    def getEntries(self):
        return self.entries

    def setEntries(self, entries):
        self.entries = entries

    def getContext(self):
        return self.context

    def setContext(self, context):
        self.context = context

    def getPathName(self):
        return self.pathName

    def setPathName(self, pathName):
        self.pathName = pathName

    def getErrorText(self):
        return self.errorText

    def setErrorText(self, errorText):
        self.errorText = errorText

    def __str__(self):
        if self.errorText is None:
            return str(self.entries)
        else:
            return "Error retrieving file listing for " + self.pathName + ": " + \
                    self.errorText
