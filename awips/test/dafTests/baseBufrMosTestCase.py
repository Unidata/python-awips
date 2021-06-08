#
# Base TestCase for BufrMos* tests.
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    01/19/16        4795          mapeters       Initial Creation.
#    04/11/16        5548          tgurney        Cleanup
#    12/07/16        5981          tgurney        Parameterize
#    12/15/16        5981          tgurney        Add envelope test
#
#

from awips.dataaccess import DataAccessLayer as DAL

from awips.test.dafTests import baseDafTestCase
from awips.test.dafTests import params


class BufrMosTestCase(baseDafTestCase.DafTestCase):
    """Base class for testing DAF support of bufrmos data"""

    data_params = "temperature", "dewpoint"

    def testGetAvailableParameters(self):
        req = DAL.newDataRequest(self.datatype)
        self.runParametersTest(req)

    def testGetAvailableLocations(self):
        req = DAL.newDataRequest(self.datatype)
        self.runLocationsTest(req)

    def testGetAvailableTimes(self):
        req = DAL.newDataRequest(self.datatype)
        req.setLocationNames(params.OBS_STATION)
        self.runTimesTest(req)

    def testGetGeometryData(self):
        req = DAL.newDataRequest(self.datatype)
        req.setLocationNames(params.OBS_STATION)
        req.setParameters(*self.data_params)
        self.runGeometryDataTest(req)

    def testGetGeometryDataWithEnvelope(self):
        req = DAL.newDataRequest(self.datatype)
        req.setParameters(*self.data_params)
        req.setEnvelope(params.ENVELOPE)
        data = self.runGeometryDataTest(req)
        for item in data:
            self.assertTrue(params.ENVELOPE.contains(item.getGeometry()))
