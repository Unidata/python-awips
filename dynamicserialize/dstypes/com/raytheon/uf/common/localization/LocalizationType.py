

class LocalizationType(object):

    def __init__(self, text=None):
        self.text = text

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return str(self.text)

    def getText(self):
        return self.text

    def setText(self, text):
        self.text = text
