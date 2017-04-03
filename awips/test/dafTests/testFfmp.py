##
##

from __future__ import print_function
from awips.dataaccess import DataAccessLayer as DAL

import baseDafTestCase
import unittest

#
# Test DAF support for ffmp data
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    01/19/16        4795          mapeters       Initial Creation.
#    04/11/16        5548          tgurney        Cleanup
#    04/18/16        5548          tgurney        More cleanup
#    04/18/16        5587          tgurney        Add test for sane handling of
#                                                 zero records returned
#    06/20/16        5587          tgurney        Add identifier values tests
#    11/08/16        5985          tgurney        Do not check data times
#
#


class FfmpTestCase(baseDafTestCase.DafTestCase):
    """Test DAF support for ffmp data"""

    datatype = "ffmp"

    @staticmethod
    def addIdentifiers(req):
        req.addIdentifier("wfo", "OAX")
        req.addIdentifier("siteKey", "hpe")
        req.addIdentifier("dataKey", "hpe")
        req.addIdentifier("huc", "ALL")

    def testGetAvailableParameters(self):
        req = DAL.newDataRequest(self.datatype)
        self.runParametersTest(req)

    def testGetAvailableLocations(self):
        req = DAL.newDataRequest(self.datatype)
        self.addIdentifiers(req)
        self.runLocationsTest(req)

    def testGetAvailableTimes(self):
        req = DAL.newDataRequest(self.datatype)
        self.addIdentifiers(req)
        self.runTimesTest(req)

    def testGetGeometryData(self):
        req = DAL.newDataRequest(self.datatype)
        self.addIdentifiers(req)
        req.setParameters("PRTM")
        self.runGeometryDataTest(req, checkDataTimes=False)

    def testGetGeometryDataEmptyResult(self):
        req = DAL.newDataRequest(self.datatype)
        self.addIdentifiers(req)
        req.setParameters("blah blah blah") # force 0 records returned
        result = self.runGeometryDataTest(req, checkDataTimes=False)
        self.assertEqual(len(result), 0)

    def testGetIdentifierValues(self):
        req = DAL.newDataRequest(self.datatype)
        optionalIds = set(DAL.getOptionalIdentifiers(req))
        requiredIds = set(DAL.getRequiredIdentifiers(req))
        ids = requiredIds | optionalIds
        # These two not yet supported
        ids.remove('huc')
        ids.remove('accumHrs')
        self.runGetIdValuesTest(ids)

    def testGetInvalidIdentifierValuesThrowsException(self):
        self.runInvalidIdValuesTest()

    def testGetNonexistentIdentifierValuesThrowsException(self):
        self.runNonexistentIdValuesTest()
