#
# Test DAF support for radar grid data
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    08/25/16        2671          tgurney        Initial creation
#
#

from awips.dataaccess import DataAccessLayer as DAL
from dynamicserialize.dstypes.com.raytheon.uf.common.dataquery.requests import RequestConstraint

from awips.test.dafTests import baseRadarTestCase
from awips.test.dafTests import params


class RadarTestCase(baseRadarTestCase.BaseRadarTestCase):
    """Test DAF support for radar data"""

    datatype = 'radar'

    parameterList = ['94']

    def runConstraintTest(self, key, operator, value):
        req = DAL.newDataRequest(self.datatype)
        constraint = RequestConstraint.new(operator, value)
        req.addIdentifier(key, constraint)
        req.setParameters(*self.parameterList)
        # Don't test shapes since they may differ.
        return self.runGridDataTest(req, testSameShape=False)

    def testGetGridData(self):
        req = DAL.newDataRequest(self.datatype)
        req.setEnvelope(params.ENVELOPE)
        req.setLocationNames(self.radarLoc)
        req.setParameters(*self.parameterList)
        # Don't test shapes since they may differ.
        self.runGridDataTest(req, testSameShape=False)
