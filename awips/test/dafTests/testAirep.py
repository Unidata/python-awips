#
# Test DAF support for airep data
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    01/19/16        4795          mapeters       Initial Creation.
#    04/11/16        5548          tgurney        Cleanup
#    04/18/16        5548          tgurney        More cleanup
#    06/09/16        5587          bsteffen       Add getIdentifierValues tests
#    06/13/16        5574          tgurney        Add advanced query tests
#    06/30/16        5725          tgurney        Add test for NOT IN
#
#

from __future__ import print_function
from awips.dataaccess import DataAccessLayer as DAL

from dynamicserialize.dstypes.com.raytheon.uf.common.dataquery.requests import RequestConstraint
from awips.test.dafTests import baseDafTestCase


class AirepTestCase(baseDafTestCase.DafTestCase):
    """Test DAF support for airep data"""

    datatype = "airep"

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
        req.setParameters("flightLevel", "reportType")
        self.runGeometryDataTest(req)

    def testGetIdentifierValues(self):
        req = DAL.newDataRequest(self.datatype)
        optionalIds = set(DAL.getOptionalIdentifiers(req))
        self.runGetIdValuesTest(optionalIds)

    def testGetInvalidIdentifierValuesThrowsException(self):
        self.runInvalidIdValuesTest()

    def testGetNonexistentIdentifierValuesThrowsException(self):
        self.runNonexistentIdValuesTest()

    def _runConstraintTest(self, key, operator, value):
        req = DAL.newDataRequest(self.datatype)
        constraint = RequestConstraint.new(operator, value)
        req.setParameters("flightLevel", "reportType")
        req.addIdentifier(key, constraint)
        return self.runGeometryDataTest(req)

    def testGetDataWithEqualsString(self):
        geometryData = self._runConstraintTest('reportType', '=', 'AIREP')
        for record in geometryData:
            self.assertEqual(record.getString('reportType'), 'AIREP')

    # No numeric tests since no numeric identifiers are available.

    def testGetDataWithEqualsNone(self):
        geometryData = self._runConstraintTest('reportType', '=', None)
        for record in geometryData:
            self.assertEqual(record.getType('reportType'), 'NULL')

    def testGetDataWithNotEquals(self):
        geometryData = self._runConstraintTest('reportType', '!=', 'AIREP')
        for record in geometryData:
            self.assertNotEqual(record.getString('reportType'), 'AIREP')

    def testGetDataWithNotEqualsNone(self):
        geometryData = self._runConstraintTest('reportType', '!=', None)
        for record in geometryData:
            self.assertNotEqual(record.getType('reportType'), 'NULL')

    def testGetDataWithGreaterThan(self):
        geometryData = self._runConstraintTest('reportType', '>', 'AIREP')
        for record in geometryData:
            self.assertGreater(record.getString('reportType'), 'AIREP')

    def testGetDataWithLessThan(self):
        geometryData = self._runConstraintTest('reportType', '<', 'AIREP')
        for record in geometryData:
            self.assertLess(record.getString('reportType'), 'AIREP')

    def testGetDataWithGreaterThanEquals(self):
        geometryData = self._runConstraintTest('reportType', '>=', 'AIREP')
        for record in geometryData:
            self.assertGreaterEqual(record.getString('reportType'), 'AIREP')

    def testGetDataWithLessThanEquals(self):
        geometryData = self._runConstraintTest('reportType', '<=', 'AIREP')
        for record in geometryData:
            self.assertLessEqual(record.getString('reportType'), 'AIREP')

    def testGetDataWithInTuple(self):
        collection = ('AIREP', 'AMDAR')
        geometryData = self._runConstraintTest('reportType', 'in', collection)
        for record in geometryData:
            self.assertIn(record.getString('reportType'), collection)

    def testGetDataWithInList(self):
        collection = ['AIREP', 'AMDAR']
        geometryData = self._runConstraintTest('reportType', 'in', collection)
        for record in geometryData:
            self.assertIn(record.getString('reportType'), collection)

    def testGetDataWithInGenerator(self):
        collection = ('AIREP', 'AMDAR')
        generator = (item for item in collection)
        geometryData = self._runConstraintTest('reportType', 'in', generator)
        for record in geometryData:
            self.assertIn(record.getString('reportType'), collection)

    def testGetDataWithNotInList(self):
        collection = ['AMDAR']
        geometryData = self._runConstraintTest('reportType', 'not in', collection)
        for record in geometryData:
            self.assertNotIn(record.getString('reportType'), collection)

    def testGetDataWithInvalidConstraintTypeThrowsException(self):
        with self.assertRaises(ValueError):
            self._runConstraintTest('reportType', 'junk', 'AIREP')

    def testGetDataWithInvalidConstraintValueThrowsException(self):
        with self.assertRaises(TypeError):
            self._runConstraintTest('reportType', '=', {})

    def testGetDataWithEmptyInConstraintThrowsException(self):
        with self.assertRaises(ValueError):
            self._runConstraintTest('reportType', 'in', [])

    def testGetDataWithNestedInConstraintThrowsException(self):
        collection = ('AIREP', 'AMDAR', ())
        with self.assertRaises(TypeError):
            self._runConstraintTest('reportType', 'in', collection)
