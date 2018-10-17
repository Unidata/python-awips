#
#      SOFTWARE HISTORY
#
#     Date            Ticket#       Engineer       Description
#     ------------    ----------    -----------    --------------------------
#     Oct 08, 2014                  reblum         Generated


class RegionLookupRequest(object):

    def __init__(self):
        self.region = None
        self.site = None

    def getRegion(self):
        return self.region

    def setRegion(self, region):
        self.region = region

    def getSite(self):
        return self.site

    def setSite(self, site):
        self.site = site
