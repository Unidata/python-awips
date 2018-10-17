

class DataURINotificationMessage(object):

    def __init__(self):
        self.dataURIs = None
        self.ids = None

    def getDataURIs(self):
        return self.dataURIs

    def setDataURIs(self, dataURIs):
        self.dataURIs = dataURIs

    def getIds(self):
        return self.ids

    def setIds(self, ids):
        self.ids = ids
