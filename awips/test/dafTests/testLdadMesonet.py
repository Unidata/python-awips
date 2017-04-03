##
##

from __future__ import print_function
from shapely.geometry import Polygon
from awips.dataaccess import DataAccessLayer as DAL

import baseDafTestCase
import unittest

#
# Test DAF support for ldadmesonet data
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


class LdadMesonetTestCase(baseDafTestCase.DafTestCase):
    """Test DAF support for ldadmesonet data"""

    datatype = "ldadmesonet"

    envelope = None

    @classmethod
    def getReqEnvelope(cls):
        # Restrict the output to only records with latitude and
        # longitude between -30 and 30.
        if not cls.envelope:
            vertices = [(-30, -30), (-30, 30), (30, 30), (30, -30)]
            polygon = Polygon(vertices)
            cls.envelope = polygon.envelope
        return cls.envelope

    def testGetAvailableParameters(self):
        req = DAL.newDataRequest(self.datatype)
        self.runParametersTest(req)

    def testGetAvailableLocations(self):
        req = DAL.newDataRequest(self.datatype)
        req.setEnvelope(self.getReqEnvelope())
        self.runLocationsTest(req)

    def testGetAvailableTimes(self):
        req = DAL.newDataRequest(self.datatype)
        req.setEnvelope(self.getReqEnvelope())
        self.runTimesTest(req)

    def testGetGeometryData(self):
        req = DAL.newDataRequest(self.datatype)
        req.setParameters("highLevelCloud", "pressure")
        req.setEnvelope(self.getReqEnvelope())
        self.runGeometryDataTest(req)
