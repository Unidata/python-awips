#
#      SOFTWARE HISTORY
#
#     Date            Ticket#       Engineer       Description
#     ------------    ----------    -----------    --------------------------
#     Oct 10, 2016    5916          bsteffen       Generated


class GetGridLatLonResponse(object):

    def __init__(self):
        self.lats = None
        self.lons = None
        self.nx = None
        self.ny = None

    def getLats(self):
        return self.lats

    def setLats(self, lats):
        self.lats = lats

    def getLons(self):
        return self.lons

    def setLons(self, lons):
        self.lons = lons

    def getNx(self):
        return self.nx

    def setNx(self, nx):
        self.nx = nx

    def getNy(self):
        return self.ny

    def setNy(self, ny):
        self.ny = ny
