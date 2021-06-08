

class LocalizationContext(object):

    def __init__(self):
        self.localizationType = None
        self.localizationLevel = None
        self.contextName = None

    def getLocalizationType(self):
        return self.localizationType

    def setLocalizationType(self, localizationType):
        self.localizationType = localizationType

    def getLocalizationLevel(self):
        return self.localizationLevel

    def setLocalizationLevel(self, localizationLevel):
        self.localizationLevel = localizationLevel

    def getContextName(self):
        return self.contextName

    def setContextName(self, contextName):
        self.contextName = contextName

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        delimitedString = str(self.localizationType).lower() + "." + str(self.localizationLevel).lower()
        if self.contextName is not None and self.contextName != "":
            delimitedString += "." + self.contextName
        return delimitedString
