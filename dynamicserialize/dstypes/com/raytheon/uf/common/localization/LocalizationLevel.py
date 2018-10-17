
knownLevels = {
    "BASE": {"text": "BASE", "order": 0, "systemLevel": True},
    "CONFIGURED": {"text": "CONFIGURED", "order": 250, "systemLevel": True},
    "SITE": {"text": "SITE", "order": 500, "systemLevel": False},
    "USER": {"text": "USER", "order": 1000, "systemLevel": False},
    "UNKNOWN": {"text": "UNKNOWN", "order": -1}
}


class LocalizationLevel(object):

    def __init__(self, level, order=750, systemLevel=False):
        if level.upper() in knownLevels:
            self.text = level.upper()
            self.order = knownLevels[self.text]["order"]
            self.systemLevel = knownLevels[self.text]["systemLevel"]
        else:
            self.text = level.upper()
            self.order = int(order)
            self.systemLevel = systemLevel

    def getText(self):
        return self.text

    def setText(self, text):
        self.text = text

    def getOrder(self):
        return self.order

    def setOrder(self, order):
        self.order = int(order)

    def isSystemLevel(self):
        return self.systemLevel

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return str(self.text)
