#
# Test DAF support for topo data
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    01/19/16        4795          mapeters       Initial Creation.
#    04/11/16        5548          tgurney        Cleanup
#    04/18/16        5548          tgurney        More cleanup
#    05/26/16        5587          tgurney        Add test for
#                                                 getIdentifierValues()
#    06/01/16        5587          tgurney        Update testGetIdentifierValues
#    07/18/17        6253          randerso       Removed referenced to GMTED
#

from __future__ import print_function
from awips.dataaccess import DataAccessLayer as DAL
from awips.ThriftClient import ThriftRequestException
import shapely.geometry

from awips.test.dafTests import baseDafTestCase


class TopoTestCase(baseDafTestCase.DafTestCase):
    """Test DAF support for topo data"""

    datatype = "topo"

    def testGetGridData(self):
        print("defaultTopo")
        req = DAL.newDataRequest(self.datatype)
        req.addIdentifier("group", "/")
        req.addIdentifier("dataset", "full")
        poly = shapely.geometry.LinearRing(((-70, 40), (-71, 40), (-71, 42), (-70, 42)))
        req.setEnvelope(poly)
        gridData = DAL.getGridData(req)
        self.assertIsNotNone(gridData)
        print("Number of grid records: " + str(len(gridData)))
        print("Sample grid data shape:\n" + str(gridData[0].getRawData().shape) + "\n")
        print("Sample grid data:\n" + str(gridData[0].getRawData()) + "\n")

        for topoFile in ["gtopo30"]:
            print("\n" + topoFile)
            req.addIdentifier("topoFile", topoFile)
            gridData = DAL.getGridData(req)
            self.assertIsNotNone(gridData)
            print("Number of grid records: " + str(len(gridData)))
            print("Sample grid data shape:\n" + str(gridData[0].getRawData().shape) + "\n")
            print("Sample grid data:\n" + str(gridData[0].getRawData()) + "\n")

    def testRequestingTooMuchDataThrowsResponseTooLargeException(self):
        req = DAL.newDataRequest(self.datatype)
        req.addIdentifier("group", "/")
        req.addIdentifier("dataset", "full")
        points = ((-180, 90), (180, 90), (180, -90), (-180, -90))
        poly = shapely.geometry.LinearRing(points)
        req.setEnvelope(poly)

        with self.assertRaises(ThriftRequestException) as cm:
            DAL.getGridData(req)
        self.assertIn('ResponseTooLargeException', str(cm.exception))

    def testGetIdentifierValues(self):
        req = DAL.newDataRequest(self.datatype)
        optionalIds = set(DAL.getOptionalIdentifiers(req))
        requiredIds = set(DAL.getRequiredIdentifiers(req))
        self.runGetIdValuesTest(optionalIds | requiredIds)

    def testGetInvalidIdentifierValuesThrowsException(self):
        self.runInvalidIdValuesTest()

    def testGetNonexistentIdentifierValuesThrowsException(self):
        self.runNonexistentIdValuesTest()
