##
##

from __future__ import print_function
from awips.dataaccess import DataAccessLayer as DAL

import baseDafTestCase
import unittest

#
# Test DAF support for pirep data
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


class PirepTestCase(baseDafTestCase.DafTestCase):
    """Test DAF support for pirep data"""

    datatype = "pirep"

    def testGetAvailableParameters(self):
        req = DAL.newDataRequest(self.datatype)
        self.runParametersTest(req)

    def testGetAvailableLocations(self):
        req = DAL.newDataRequest(self.datatype)
        self.runLocationsTest(req)

    def testGetAvailableTimes(self):
        req = DAL.newDataRequest(self.datatype)
        req.setLocationNames('OMA')
        self.runTimesTest(req)

    def testGetGeometryData(self):
        req = DAL.newDataRequest(self.datatype)
        req.setLocationNames('OMA')
        req.setParameters("temperature", "windSpeed", "hazardType", "turbType")

        print("Testing getGeometryData()")

        geomData = DAL.getGeometryData(req)
        self.assertIsNotNone(geomData)
        print("Number of geometry records: " + str(len(geomData)))
        print("Sample geometry data:")
        for record in geomData[:self.sampleDataLimit]:
            print("level=", record.getLevel(), end="")
            # One dimensional parameters are reported on the 0.0UNKNOWN level.
            # 2D parameters are reported on MB levels from pressure.
            if record.getLevel() == "0.0UNKNOWN":
                print(" temperature=" + record.getString("temperature") + record.getUnit("temperature"), end="")
                print(" windSpeed=" + record.getString("windSpeed") + record.getUnit("windSpeed"), end="")
            else:
                print(" hazardType=" + record.getString("hazardType"), end="")
                print(" turbType=" + record.getString("turbType"), end="")
            print(" geometry=", record.getGeometry())

        print("getGeometryData() complete\n")

