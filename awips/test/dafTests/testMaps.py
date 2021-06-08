#
# Test DAF support for maps data
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    01/19/16        4795          mapeters       Initial Creation.
#    04/11/16        5548          tgurney        Cleanup
#    04/18/16        5548          tgurney        More cleanup
#    04/26/16        5587          tgurney        Add identifier values tests
#    06/13/16        5574          mapeters       Add advanced query tests
#    06/21/16        5548          tgurney        Skip tests that cause errors
#    06/30/16        5725          tgurney        Add test for NOT IN
#    01/06/17        5981          tgurney        Do not check data times
#
#

from __future__ import print_function
from dynamicserialize.dstypes.com.raytheon.uf.common.dataquery.requests import RequestConstraint
from awips.dataaccess import DataAccessLayer as DAL
from awips.ThriftClient import ThriftRequestException

from awips.test.dafTests import baseDafTestCase


class MapsTestCase(baseDafTestCase.DafTestCase):
    """Test DAF support for maps data"""

    datatype = 'maps'

    def testGetAvailableParameters(self):
        req = DAL.newDataRequest(self.datatype)
        req.addIdentifier('table', 'mapdata.county')
        req.addIdentifier('geomField', 'the_geom')
        self.runParametersTest(req)

    def testGetAvailableLocations(self):
        req = DAL.newDataRequest(self.datatype)
        req.addIdentifier('table', 'mapdata.county')
        req.addIdentifier('geomField', 'the_geom')
        req.addIdentifier('locationField', 'cwa')
        self.runLocationsTest(req)

    def testGetGeometryData(self):
        req = DAL.newDataRequest(self.datatype)
        req.addIdentifier('table', 'mapdata.county')
        req.addIdentifier('geomField', 'the_geom')
        req.addIdentifier('inLocation', 'true')
        req.addIdentifier('locationField', 'cwa')
        req.setLocationNames('OAX')
        req.addIdentifier('cwa', 'OAX')
        req.setParameters('countyname', 'state', 'fips')
        self.runGeometryDataTest(req, checkDataTimes=False)

    def testRequestingTimesThrowsTimeAgnosticDataException(self):
        req = DAL.newDataRequest(self.datatype)
        self.runTimeAgnosticTest(req)

    def testGetTableIdentifierValues(self):
        self.runGetIdValuesTest(['table'])

    def testGetGeomFieldIdentifierValues(self):
        req = DAL.newDataRequest(self.datatype)
        req.addIdentifier('table', 'mapdata.county')
        idValues = DAL.getIdentifierValues(req, 'geomField')
        for idValue in idValues:
            self.assertTrue(idValue.startswith('the_geom'))

    def testGetGeomFieldIdValuesWithoutTableThrowsException(self):
        with self.assertRaises(ThriftRequestException):
            self.runGetIdValuesTest(['geomField'])

    def testGetColumnIdValuesWithTable(self):
        req = DAL.newDataRequest(self.datatype)
        req.addIdentifier('table', 'mapdata.county')
        req.addIdentifier('geomField', 'the_geom')
        idValues = DAL.getIdentifierValues(req, 'state')
        self.assertIn('NE', idValues)

    def testGetColumnIdValuesWithoutTableThrowsException(self):
        req = DAL.newDataRequest(self.datatype)
        req.addIdentifier('geomField', 'the_geom')
        with self.assertRaises(ThriftRequestException):
            DAL.getIdentifierValues(req, 'state')

    def testGetInvalidIdentifierValuesThrowsException(self):
        self.runInvalidIdValuesTest()

    def testGetNonexistentIdentifierValuesThrowsException(self):
        self.runNonexistentIdValuesTest()

    def _runConstraintTest(self, key, operator, value):
        req = DAL.newDataRequest(self.datatype)
        req.addIdentifier('table', 'mapdata.ffmp_basins')
        req.addIdentifier('geomField', 'the_geom')
        req.addIdentifier('cwa', 'OAX')
        constraint = RequestConstraint.new(operator, value)
        req.addIdentifier(key, constraint)
        req.setParameters('state', 'reservoir', 'area_sq_mi')
        return self.runGeometryDataTest(req, checkDataTimes=False)

    def testGetDataWithEqualsString(self):
        geometryData = self._runConstraintTest('state', '=', 'NE')
        for record in geometryData:
            self.assertEqual(record.getString('state'), 'NE')

    def testGetDataWithEqualsInt(self):
        geometryData = self._runConstraintTest('reservoir', '=', 1)
        for record in geometryData:
            self.assertEqual(record.getNumber('reservoir'), 1)

    def testGetDataWithEqualsLong(self):
        geometryData = self._runConstraintTest('reservoir', '=', 1)
        for record in geometryData:
            self.assertEqual(record.getNumber('reservoir'), 1)

    def testGetDataWithEqualsFloat(self):
        geometryData = self._runConstraintTest('area_sq_mi', '=', 5.00)
        for record in geometryData:
            self.assertEqual(round(record.getNumber('area_sq_mi'), 2), 5.00)

    def testGetDataWithEqualsNone(self):
        geometryData = self._runConstraintTest('state', '=', None)
        for record in geometryData:
            self.assertEqual(record.getType('state'), 'NULL')

    def testGetDataWithNotEquals(self):
        geometryData = self._runConstraintTest('state', '!=', 'NE')
        for record in geometryData:
            self.assertNotEqual(record.getString('state'), 'NE')

    def testGetDataWithNotEqualsNone(self):
        geometryData = self._runConstraintTest('state', '!=', None)
        for record in geometryData:
            self.assertNotEqual(record.getType('state'), 'NULL')

    def testGetDataWithGreaterThan(self):
        geometryData = self._runConstraintTest('area_sq_mi', '>', 5)
        for record in geometryData:
            self.assertGreater(record.getNumber('area_sq_mi'), 5)

    def testGetDataWithLessThan(self):
        geometryData = self._runConstraintTest('area_sq_mi', '<', 5)
        for record in geometryData:
            self.assertLess(record.getNumber('area_sq_mi'), 5)

    def testGetDataWithGreaterThanEquals(self):
        geometryData = self._runConstraintTest('area_sq_mi', '>=', 5)
        for record in geometryData:
            self.assertGreaterEqual(record.getNumber('area_sq_mi'), 5)

    def testGetDataWithLessThanEquals(self):
        geometryData = self._runConstraintTest('area_sq_mi', '<=', 5)
        for record in geometryData:
            self.assertLessEqual(record.getNumber('area_sq_mi'), 5)

    def testGetDataWithInTuple(self):
        collection = ('NE', 'TX')
        geometryData = self._runConstraintTest('state', 'in', collection)
        for record in geometryData:
            self.assertIn(record.getString('state'), collection)

    def testGetDataWithInList(self):
        collection = ['NE', 'TX']
        geometryData = self._runConstraintTest('state', 'in', collection)
        for record in geometryData:
            self.assertIn(record.getString('state'), collection)

    def testGetDataWithInGenerator(self):
        collection = ('NE', 'TX')
        generator = (item for item in collection)
        geometryData = self._runConstraintTest('state', 'in', generator)
        for record in geometryData:
            self.assertIn(record.getString('state'), collection)

    def testGetDataWithNotInList(self):
        collection = ['IA', 'TX']
        geometryData = self._runConstraintTest('state', 'not in', collection)
        for record in geometryData:
            self.assertNotIn(record.getString('state'), collection)

    def testGetDataWithInvalidConstraintTypeThrowsException(self):
        with self.assertRaises(ValueError):
            self._runConstraintTest('state', 'junk', 'NE')

    def testGetDataWithInvalidConstraintValueThrowsException(self):
        with self.assertRaises(TypeError):
            self._runConstraintTest('state', '=', {})

    def testGetDataWithEmptyInConstraintThrowsException(self):
        with self.assertRaises(ValueError):
            self._runConstraintTest('state', 'in', [])
