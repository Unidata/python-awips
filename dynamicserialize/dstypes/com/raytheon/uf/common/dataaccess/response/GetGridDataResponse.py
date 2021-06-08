

class GetGridDataResponse(object):

    def __init__(self):
        self.gridData = None
        self.siteNxValues = None
        self.siteNyValues = None
        self.siteLatGrids = None
        self.siteLonGrids = None
        self.siteEnvelopes = None
        self.siteCrsWkt = None

    def getGridData(self):
        return self.gridData

    def setGridData(self, gridData):
        self.gridData = gridData

    def getSiteNxValues(self):
        return self.siteNxValues

    def setSiteNxValues(self, siteNxValues):
        self.siteNxValues = siteNxValues

    def getSiteNyValues(self):
        return self.siteNyValues

    def setSiteNyValues(self, siteNyValues):
        self.siteNyValues = siteNyValues

    def getSiteLatGrids(self):
        return self.siteLatGrids

    def setSiteLatGrids(self, siteLatGrids):
        self.siteLatGrids = siteLatGrids

    def getSiteLonGrids(self):
        return self.siteLonGrids

    def setSiteLonGrids(self, siteLonGrids):
        self.siteLonGrids = siteLonGrids

    def getSiteEnvelopes(self):
        return self.siteEnvelopes

    def setSiteEnvelopes(self, siteEnvelopes):
        self.siteEnvelopes = siteEnvelopes

    def getSiteCrsWkt(self):
        return self.siteCrsWkt

    def setSiteCrsWkt(self, siteCrsWkt):
        self.siteCrsWkt = siteCrsWkt
