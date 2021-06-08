# Jul 27, 2015 4654     skorolev     Added filters


class AlertVizRequest(object):

    def __init__(self):
        self.message = None
        self.machine = None
        self.priority = None
        self.sourceKey = None
        self.category = None
        self.audioFile = None
        self.filters = None

    def getMessage(self):
        return self.message

    def setMessage(self, message):
        self.message = message

    def getMachine(self):
        return self.machine

    def setMachine(self, machine):
        self.machine = machine

    def getPriority(self):
        return self.priority

    def setPriority(self, priority):
        self.priority = priority

    def getSourceKey(self):
        return self.sourceKey

    def setSourceKey(self, sourceKey):
        self.sourceKey = sourceKey

    def getCategory(self):
        return self.category

    def setCategory(self, category):
        self.category = category

    def getAudioFile(self):
        return self.audioFile

    def setAudioFile(self, audioFile):
        self.audioFile = audioFile

    def getFilters(self):
        return self.filters

    def setFilters(self, filters):
        if filters is None:
            self.filters = {}
        elif not(None in filters
                 or filters.values().count(None) > 0
                 or '' in filters
                 or filters.values().count('') > 0):
            self.filters = filters
        else:
            raise ValueError('Filters must not contain None or empty keys or values: %s' % filters)
