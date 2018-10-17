#
#      SOFTWARE HISTORY
#
#     Date            Ticket#       Engineer       Description
#     ------------    ----------    -----------    --------------------------
#     Jul 27, 2015    1574          nabowle        Generated
#     Feb 23, 2016    5389          nabowle        Regenerated


class DeleteOrphansRequest(object):

    def __init__(self):
        self.oldestDateMap = None
        self.filename = None

    def getOldestDateMap(self):
        return self.oldestDateMap

    def setOldestDateMap(self, oldestDateMap):
        self.oldestDateMap = oldestDateMap

    def getFilename(self):
        return self.filename

    def setFilename(self, filename):
        self.filename = filename
