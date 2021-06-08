#
# Test DAF support for ACARS data
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    01/19/16        4795          mapeters       Initial Creation.
#    04/11/16        5548          tgurney        Cleanup
#    04/18/16        5548          tgurney        More cleanup
#
#

from __future__ import print_function
from awips.dataaccess import DataAccessLayer as DAL
from awips.test.dafTests import baseDafTestCase


class AcarsTestCase(baseDafTestCase.DafTestCase):
    """Test DAF support for ACARS data"""

    datatype = "acars"

    def testGetAvailableParameters(self):
        req = DAL.newDataRequest(self.datatype)
        self.runParametersTest(req)

    def testGetAvailableLocations(self):
        req = DAL.newDataRequest(self.datatype)
        self.runLocationsTest(req)

    def testGetAvailableTimes(self):
        req = DAL.newDataRequest(self.datatype)
        self.runTimesTest(req)

    def testGetGeometryData(self):
        req = DAL.newDataRequest(self.datatype)
        req.setParameters("flightLevel", "tailNumber")
        self.runGeometryDataTest(req)
