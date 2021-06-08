#
# Test DAF support for radar graphics data
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    08/25/16        2671          tgurney        Initial creation.
#    08/31/16        2671          tgurney        Add mesocyclone
#    09/08/16        2671          tgurney        Add storm track
#    09/27/16        2671          tgurney        Add hail index
#    09/30/16        2671          tgurney        Add TVS
#    12/07/16        5981          tgurney        Parameterize
#    12/19/16        5981          tgurney        Do not check data times on
#                                                 returned data
#
#

from dynamicserialize.dstypes.com.raytheon.uf.common.dataquery.requests import RequestConstraint
from awips.dataaccess import DataAccessLayer as DAL

from awips.test.dafTests import baseRadarTestCase
from awips.test.dafTests import params


class RadarGraphicsTestCase(baseRadarTestCase.BaseRadarTestCase):
    """Test DAF support for radar data"""

    datatype = 'radar'

    def runConstraintTest(self, key, operator, value):
        req = DAL.newDataRequest(self.datatype)
        constraint = RequestConstraint.new(operator, value)
        req.addIdentifier(key, constraint)
        req.setParameters('166')
        # TODO: Cannot check datatimes on the result because the times returned
        # by getAvailableTimes have level = -1.0, while the time on the actual
        # data has the correct level set (>= 0.0).
        return self.runGeometryDataTest(req, checkDataTimes=False)

    def testGetGeometryDataMeltingLayer(self):
        req = DAL.newDataRequest(self.datatype)
        req.setEnvelope(params.ENVELOPE)
        req.setLocationNames(self.radarLoc)
        req.setParameters('166')
        self.runGeometryDataTest(req, checkDataTimes=False)

    def testGetGeometryDataMesocyclone(self):
        req = DAL.newDataRequest(self.datatype)
        req.setEnvelope(params.ENVELOPE)
        req.setLocationNames(self.radarLoc)
        req.setParameters('141')
        self.runGeometryDataTest(req, checkDataTimes=False)

    def testGetGeometryDataStormTrack(self):
        req = DAL.newDataRequest(self.datatype)
        req.setEnvelope(params.ENVELOPE)
        req.setLocationNames(self.radarLoc)
        req.setParameters('58')
        self.runGeometryDataTest(req, checkDataTimes=False)

    def testGetGeometryDataHailIndex(self):
        req = DAL.newDataRequest(self.datatype)
        req.setEnvelope(params.ENVELOPE)
        req.setLocationNames(self.radarLoc)
        req.setParameters('59')
        self.runGeometryDataTest(req, checkDataTimes=False)

    def testGetGeometryDataTVS(self):
        req = DAL.newDataRequest(self.datatype)
        req.setEnvelope(params.ENVELOPE)
        req.setLocationNames(self.radarLoc)
        req.setParameters('61')
        self.runGeometryDataTest(req, checkDataTimes=False)
