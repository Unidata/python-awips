

class Request(object):

    def __init__(self):
        self.points = None
        self.indices = None
        self.minIndexForSlab = None
        self.maxIndexForSlab = None
        self.type = None

    def getPoints(self):
        return self.points

    def setPoints(self, points):
        self.points = points

    def getIndices(self):
        return self.indices

    def setIndices(self, indices):
        self.indices = indices

    def getMinIndexForSlab(self):
        return self.minIndexForSlab

    def setMinIndexForSlab(self, minIndexForSlab):
        self.minIndexForSlab = minIndexForSlab

    def getMaxIndexForSlab(self):
        return self.maxIndexForSlab

    def setMaxIndexForSlab(self, maxIndexForSlab):
        self.maxIndexForSlab = maxIndexForSlab

    def getType(self):
        return self.type

    def setType(self, requesttype):
        self.type = requesttype
