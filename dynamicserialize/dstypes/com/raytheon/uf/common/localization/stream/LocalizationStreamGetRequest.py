from dynamicserialize.dstypes.com.raytheon.uf.common.localization.stream import AbstractLocalizationStreamRequest


class LocalizationStreamGetRequest(AbstractLocalizationStreamRequest):

    def __init__(self):
        super(LocalizationStreamGetRequest, self).__init__()
        self.offset = None
        self.numBytes = None

    def getOffset(self):
        return self.offset

    def setOffset(self, offset):
        self.offset = offset

    def getNumBytes(self):
        return self.numBytes

    def setNumBytes(self, numBytes):
        self.numBytes = numBytes
