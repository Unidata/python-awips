#
# Test the CombinedTimedQuery module
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    06/24/16        5591          bsteffen       Initial Creation.
#    11/08/16        5895          tgurney        Change grid model
#
#
#

from awips.dataaccess import DataAccessLayer as DAL
from awips.dataaccess import CombinedTimeQuery as CTQ

import unittest
import os


class CombinedTimeQueryTestCase(unittest.TestCase):

    modelName = "RAP13"

    @classmethod
    def setUp(cls):
        host = os.environ.get('DAF_TEST_HOST')
        if host is None:
            host = 'edex-cloud.unidata.ucar.edu'
        DAL.changeEDEXHost(host)

    def testSuccessfulQuery(self):
        req = DAL.newDataRequest('grid')
        req.setLocationNames(self.modelName)
        req.setParameters('T', 'GH')
        req.setLevels('300MB', '500MB', '700MB')
        times = CTQ.getAvailableTimes(req)
        self.assertNotEqual(len(times), 0)

    def testNonIntersectingQuery(self):
        """
        Test that when a parameter is only available on one of the levels that no times are returned.
        """
        req = DAL.newDataRequest('grid')
        req.setLocationNames(self.modelName)
        req.setParameters('T', 'GH', 'LgSP1hr')
        req.setLevels('300MB', '500MB', '700MB', '0.0SFC')
        times = CTQ.getAvailableTimes(req)
        self.assertEqual(len(times), 0)
