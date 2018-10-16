#
# Test DAF support for binlightning data
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    01/19/16        4795          mapeters       Initial Creation.
#    04/11/16        5548          tgurney        Cleanup
#    04/18/16        5548          tgurney        More cleanup
#    04/21/16        5551          tgurney        Add tests to verify #5551
#    04/25/16        5587          tgurney        Enable skipped test added in
#                                                 #5551
#    04/26/16        5587          tgurney        Move identifier values tests
#                                                 out of base class
#    06/01/16        5587          tgurney        Update testGetIdentifierValues
#    06/03/16        5574          tgurney        Add advanced query tests
#    06/13/16        5574          tgurney        Typo
#    06/30/16        5725          tgurney        Add test for NOT IN
#    11/08/16        5985          tgurney        Do not check data times
#
#
from __future__ import print_function
from awips.dataaccess import DataAccessLayer as DAL
from awips.ThriftClient import ThriftRequestException
from dynamicserialize.dstypes.com.raytheon.uf.common.dataquery.requests import RequestConstraint
from awips.test.dafTests import baseDafTestCase


class BinLightningTestCase(baseDafTestCase.DafTestCase):
    """Test DAF support for binlightning data"""

    datatype = "binlightning"
    source = "GLMfl"

    def testGetAvailableParameters(self):
        req = DAL.newDataRequest(self.datatype)
        self.runParametersTest(req)

    def testGetAvailableTimes(self):
        req = DAL.newDataRequest(self.datatype)
        req.addIdentifier('source', self.source)
        self.runTimesTest(req)

    def testGetGeometryDataSingleSourceSingleParameter(self):
        req = DAL.newDataRequest(self.datatype)
        req.addIdentifier('source', self.source)
        req.setParameters('intensity')
        self.runGeometryDataTest(req, checkDataTimes=False)

    def testGetGeometryDataInvalidParamRaisesIncompatibleRequestException(self):
        req = DAL.newDataRequest(self.datatype)
        req.addIdentifier('source', self.source)
        req.setParameters('blahblahblah')
        with self.assertRaises(ThriftRequestException) as cm:
            self.runGeometryDataTest(req)
        self.assertIn('IncompatibleRequestException', str(cm.exception))

    def testGetGeometryDataSingleSourceAllParameters(self):
        req = DAL.newDataRequest(self.datatype)
        req.addIdentifier('source', self.source)
        req.setParameters(*DAL.getAvailableParameters(req))
        self.runGeometryDataTest(req, checkDataTimes=False)

    def testGetIdentifierValues(self):
        req = DAL.newDataRequest(self.datatype)
        optionalIds = set(DAL.getOptionalIdentifiers(req))
        requiredIds = set(DAL.getRequiredIdentifiers(req))
        self.runGetIdValuesTest(optionalIds | requiredIds)

    def testGetInvalidIdentifierValuesThrowsException(self):
        self.runInvalidIdValuesTest()

    def testGetNonexistentIdentifierValuesThrowsException(self):
        self.runNonexistentIdValuesTest()

    def _runConstraintTest(self, key, operator, value):
        req = DAL.newDataRequest(self.datatype)
        constraint = RequestConstraint.new(operator, value)
        req.addIdentifier(key, constraint)
        req.setParameters('intensity')
        return self.runGeometryDataTest(req, checkDataTimes=False)

    def testGetDataWithEqualsString(self):
        geomData = self._runConstraintTest('source', '=', self.source)
        for record in geomData:
            self.assertEqual(record.getAttribute('source'), self.source)

    def testGetDataWithEqualsInt(self):
        geomData = self._runConstraintTest('source', '=', 1000)
        for record in geomData:
            self.assertEqual(record.getAttribute('source'), 1000)

    def testGetDataWithEqualsLong(self):
        geomData = self._runConstraintTest('source', '=', 1000)
        for record in geomData:
            self.assertEqual(record.getAttribute('source'), 1000)

    def testGetDataWithEqualsFloat(self):
        geomData = self._runConstraintTest('source', '=', 1.0)
        for record in geomData:
            self.assertEqual(round(record.getAttribute('source'), 1), 1.0)

    def testGetDataWithEqualsNone(self):
        geomData = self._runConstraintTest('source', '=', None)
        for record in geomData:
            self.assertIsNone(record.getAttribute('source'))

    def testGetDataWithNotEquals(self):
        geomData = self._runConstraintTest('source', '!=', self.source)
        for record in geomData:
            self.assertNotEqual(record.getAttribute('source'), self.source)

    def testGetDataWithNotEqualsNone(self):
        geomData = self._runConstraintTest('source', '!=', None)
        for record in geomData:
            self.assertIsNotNone(record.getAttribute('source'))

    def testGetDataWithGreaterThan(self):
        geomData = self._runConstraintTest('source', '>', self.source)
        for record in geomData:
            self.assertGreater(record.getAttribute('source'), self.source)

    def testGetDataWithLessThan(self):
        geomData = self._runConstraintTest('source', '<', self.source)
        for record in geomData:
            self.assertLess(record.getAttribute('source'), self.source)

    def testGetDataWithGreaterThanEquals(self):
        geomData = self._runConstraintTest('source', '>=', self.source)
        for record in geomData:
            self.assertGreaterEqual(record.getAttribute('source'), self.source)

    def testGetDataWithLessThanEquals(self):
        geomData = self._runConstraintTest('source', '<=', self.source)
        for record in geomData:
            self.assertLessEqual(record.getAttribute('source'), self.source)

    def testGetDataWithInTuple(self):
        geomData = self._runConstraintTest('source', 'in', (self.source, 'GLMev'))
        for record in geomData:
            self.assertIn(record.getAttribute('source'), (self.source, 'GLMev'))

    def testGetDataWithInList(self):
        geomData = self._runConstraintTest('source', 'in', [self.source, 'GLMev'])
        for record in geomData:
            self.assertIn(record.getAttribute('source'), (self.source, 'GLMev'))

    def testGetDataWithInGenerator(self):
        generator = (item for item in (self.source, 'GLMev'))
        geomData = self._runConstraintTest('source', 'in', generator)
        for record in geomData:
            self.assertIn(record.getAttribute('source'), (self.source, 'GLMev'))

    def testGetDataWithNotInList(self):
        geomData = self._runConstraintTest('source', 'not in', [self.source, 'blah'])
        for record in geomData:
            self.assertNotIn(record.getAttribute('source'), (self.source, 'blah'))

    def testGetDataWithInvalidConstraintTypeThrowsException(self):
        with self.assertRaises(ValueError):
            self._runConstraintTest('source', 'junk', self.source)

    def testGetDataWithInvalidConstraintValueThrowsException(self):
        with self.assertRaises(TypeError):
            self._runConstraintTest('source', '=', {})

    def testGetDataWithEmptyInConstraintThrowsException(self):
        with self.assertRaises(ValueError):
            self._runConstraintTest('source', 'in', [])
