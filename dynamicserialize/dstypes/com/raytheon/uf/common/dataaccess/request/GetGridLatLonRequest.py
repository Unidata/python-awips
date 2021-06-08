#
#      SOFTWARE HISTORY
#
#     Date            Ticket#       Engineer       Description
#     ------------    ----------    -----------    --------------------------
#     Oct 10, 2016    5916          bsteffen       Generated


class GetGridLatLonRequest(object):

    def __init__(self):
        self.envelope = None
        self.crsWkt = None
        self.nx = None
        self.ny = None

    def getEnvelope(self):
        return self.envelope

    def setEnvelope(self, envelope):
        self.envelope = envelope

    def getCrsWkt(self):
        return self.crsWkt

    def setCrsWkt(self, crsWkt):
        self.crsWkt = crsWkt

    def getNx(self):
        return self.nx

    def setNx(self, nx):
        self.nx = nx

    def getNy(self):
        return self.ny

    def setNy(self, ny):
        self.ny = ny

