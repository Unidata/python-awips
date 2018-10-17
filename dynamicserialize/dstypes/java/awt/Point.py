#
# Custom python class representing a java.awt.Point.
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    08/31/10                      njensen       Initial Creation.
#
#


class Point(object):

    def __init__(self):
        self.x = None
        self.y = None

    def __str__(self):
        return str((self.x, self.y))

    def __repr__(self):
        return self.__str__()

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y
