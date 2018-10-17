from .Property import Property


class Header(object):

    def __init__(self, properties=None, multimap=None):
        if properties is None:
            self.properties = []
        else:
            self.properties = properties

        if multimap is not None:
            for k, l in multimap.items():
                for v in l:
                    self.properties.append(Property(k, v))

    def getProperties(self):
        return self.properties

    def setProperties(self, properties):
        self.properties = properties
