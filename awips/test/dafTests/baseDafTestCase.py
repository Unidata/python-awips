#
# Base TestCase for DAF tests. This class provides helper methods and
# tests common to all DAF test cases.
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    01/19/16        4795          mapeters       Initial Creation.
#    04/11/16        5548          tgurney        Cleanup
#    04/13/16        5379          tgurney        Add identifier values tests
#    04/18/16        5548          tgurney        More cleanup, plus new tests
#    04/26/16        5587          tgurney        Move identifier values tests
#                                                 to subclasses
#    06/01/16        5587          tgurney        Add testGet*Identifiers
#    06/07/16        5574          tgurney        Make geometry/grid data tests
#                                                 return the retrieved data
#    06/10/16        5548          tgurney        Make testDatatypeIsSupported
#                                                 case-insensitive
#    08/10/16        2416          tgurney        Don't test identifier values
#                                                 for dataURI
#    10/05/16        5926          dgilling       Better checks in runGeometryDataTest.
#    11/08/16        5985          tgurney        Do not check data times on
#                                                 time-agnostic data
#    03/13/17        5981          tgurney        Do not check valid period on
#                                                 data time
#
#

from __future__ import print_function
from awips.dataaccess import DataAccessLayer as DAL
from awips.ThriftClient import ThriftRequestException

import os
import unittest


class DafTestCase(unittest.TestCase):

    sampleDataLimit = 5
    """
    Maximum number of levels, locations, times, and geometry/grid data to
    display
    """

    numTimesToLimit = 3
    """
    When limiting geometry/grid data requests with times, only retrieve data
    for this many times
    """

    datatype = None
    """Name of the datatype"""

    @classmethod
    def setUpClass(cls):
        host = os.environ.get('DAF_TEST_HOST')
        if host is None:
            host = 'edex-cloud.unidata.ucar.edu'
        DAL.changeEDEXHost(host)

    @staticmethod
    def getTimesIfSupported(req):
        """Return available times for req. If req refers to a time-agnostic
        datatype, return an empty list instead.
        """
        times = []
        try:
            times = DAL.getAvailableTimes(req)
        except ThriftRequestException as e:
            if 'TimeAgnosticDataException' not in str(e):
                raise
        return times

    def testDatatypeIsSupported(self):
        allSupported = DAL.getSupportedDatatypes()
        self.assertIn(self.datatype, allSupported)

    def testGetRequiredIdentifiers(self):
        req = DAL.newDataRequest(self.datatype)
        required = DAL.getRequiredIdentifiers(req)
        self.assertIsNotNone(required)
        print("Required identifiers:", required)

    def testGetOptionalIdentifiers(self):
        req = DAL.newDataRequest(self.datatype)
        optional = DAL.getOptionalIdentifiers(req)
        self.assertIsNotNone(optional)
        print("Optional identifiers:", optional)

    def runGetIdValuesTest(self, identifiers):
        for identifier in identifiers:
            if identifier.lower() == 'datauri':
                continue
            req = DAL.newDataRequest(self.datatype)
            idValues = DAL.getIdentifierValues(req, identifier)
            self.assertTrue(hasattr(idValues, '__iter__'))

    def runInvalidIdValuesTest(self):
        badString = 'id from ' + self.datatype + '; select 1;'
        with self.assertRaises(ThriftRequestException):
            req = DAL.newDataRequest(self.datatype)
            DAL.getIdentifierValues(req, badString)

    def runNonexistentIdValuesTest(self):
        with self.assertRaises(ThriftRequestException):
            req = DAL.newDataRequest(self.datatype)
            DAL.getIdentifierValues(req, 'idthatdoesnotexist')

    def runParametersTest(self, req):
        params = DAL.getAvailableParameters(req)
        self.assertIsNotNone(params)
        print(params)

    def runLevelsTest(self, req):
        levels = DAL.getAvailableLevels(req)
        self.assertIsNotNone(levels)
        print("Number of levels: " + str(len(levels)))
        strLevels = [str(t) for t in levels[:self.sampleDataLimit]]
        print("Sample levels:\n" + str(strLevels))

    def runLocationsTest(self, req):
        locs = DAL.getAvailableLocationNames(req)
        self.assertIsNotNone(locs)
        print("Number of location names: " + str(len(locs)))
        print("Sample location names:\n" + str(locs[:self.sampleDataLimit]))

    def runTimesTest(self, req):
        times = DAL.getAvailableTimes(req)
        self.assertIsNotNone(times)
        print("Number of times: " + str(len(times)))
        strTimes = [str(t) for t in times[:self.sampleDataLimit]]
        print("Sample times:\n" + str(strTimes))

    def runTimeAgnosticTest(self, req):
        with self.assertRaises(ThriftRequestException) as cm:
            DAL.getAvailableTimes(req)
        self.assertIn('TimeAgnosticDataException', str(cm.exception))

    def runGeometryDataTest(self, req, checkDataTimes=True):
        """
        Test that we are able to successfully retrieve geometry data for the
        given request.
        """
        times = DafTestCase.getTimesIfSupported(req)
        geomData = DAL.getGeometryData(req, times[:self.numTimesToLimit])
        self.assertIsNotNone(geomData)
        if not geomData:
            raise unittest.SkipTest("No data available")
        print("Number of geometry records: " + str(len(geomData)))
        return geomData

    def runGeometryDataTestWithTimeRange(self, req, timeRange):
        """
        Test that we are able to successfully retrieve geometry data for the
        given request.
        """
        geomData = DAL.getGeometryData(req, timeRange)
        self.assertIsNotNone(geomData)
        if not geomData:
            raise unittest.SkipTest("No data available")
        print("Number of geometry records: " + str(len(geomData)))
        return geomData

    def runGridDataTest(self, req, testSameShape=True):
        """
        Test that we are able to successfully retrieve grid data for the given
        request.

        Args:
            req: the grid request
            testSameShape: whether or not to verify that all the retrieved data
                           have the same shape (most data don't change shape)
        """
        times = DafTestCase.getTimesIfSupported(req)
        gridData = DAL.getGridData(req, times[:self.numTimesToLimit])
        self.assertIsNotNone(gridData)
        if not gridData:
            raise unittest.SkipTest("No data available")
        print("Number of grid records: " + str(len(gridData)))
        if len(gridData) > 0:
            print("Sample grid data shape:\n" + str(gridData[0].getRawData().shape) + "\n")
            print("Sample grid data:\n" + str(gridData[0].getRawData()) + "\n")
            print("Sample lat-lon data:\n" + str(gridData[0].getLatLonCoords()) + "\n")

            if testSameShape:
                correctGridShape = gridData[0].getLatLonCoords()[0].shape
                for record in gridData:
                    rawData = record.getRawData()
                    self.assertIsNotNone(rawData)
                    self.assertEqual(rawData.shape, correctGridShape)
        return gridData
