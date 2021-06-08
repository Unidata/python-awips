

class Coordinate(object):

    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def __str__(self):
        return str((self.x, self.y))

    def __repr__(self):
        return self.__str__()
