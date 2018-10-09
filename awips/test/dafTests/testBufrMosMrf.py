from awips.dataaccess import DataAccessLayer as DAL

from awips.test.dafTests import baseBufrMosTestCase
from awips.test.dafTests import params
import unittest

#
# Test DAF support for bufrmosMRF data
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    01/19/16        4795          mapeters       Initial Creation.
#    04/11/16        5548          tgurney        Cleanup
#    04/18/16        5548          tgurney        More cleanup
#    12/07/16        5981          tgurney        Parameterize
#    12/20/16        5981          tgurney        Inherit all tests
#
#


class BufrMosMrfTestCase(baseBufrMosTestCase.BufrMosTestCase):
    """Test DAF support for bufrmosMRF data"""

    datatype = "bufrmosMRF"
    data_params = "forecastHr", "maxTempDay"

    # All tests inherited from superclass
