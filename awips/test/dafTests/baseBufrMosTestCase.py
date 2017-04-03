##
##

from awips.dataaccess import DataAccessLayer as DAL

import baseDafTestCase

#
# Base TestCase for BufrMos* tests.
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    01/19/16        4795          mapeters       Initial Creation.
#    04/11/16        5548          tgurney        Cleanup
#
#
#


class BufrMosTestCase(baseDafTestCase.DafTestCase):
    """Base class for testing DAF support of bufrmos data"""

    def testGetAvailableParameters(self):
        req = DAL.newDataRequest(self.datatype)
        self.runParametersTest(req)

    def testGetAvailableLocations(self):
        req = DAL.newDataRequest(self.datatype)
        self.runLocationsTest(req)

    def testGetAvailableTimes(self):
        req = DAL.newDataRequest(self.datatype)
        req.setLocationNames("KOMA")
        self.runTimesTest(req)

    def testGetGeometryData(self):
        req = DAL.newDataRequest(self.datatype)
        req.setLocationNames("KOMA")
        req.setParameters("temperature", "dewpoint")
        self.runGeometryDataTest(req)
