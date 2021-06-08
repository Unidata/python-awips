

class Property(object):

    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value
