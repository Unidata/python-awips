

class GetGeometryDataResponse(object):

    def __init__(self):
        self.geometryWKBs = None
        self.geoData = None

    def getGeometryWKBs(self):
        return self.geometryWKBs

    def setGeometryWKBs(self, geometryWKBs):
        self.geometryWKBs = geometryWKBs

    def getGeoData(self):
        return self.geoData

    def setGeoData(self, geoData):
        self.geoData = geoData
