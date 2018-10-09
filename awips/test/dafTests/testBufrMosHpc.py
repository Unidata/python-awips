from awips.dataaccess import DataAccessLayer as DAL

from awips.test.dafTests import baseBufrMosTestCase
from awips.test.dafTests import params
import unittest

#
# Test DAF support for bufrmosHPC data
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


class BufrMosHpcTestCase(baseBufrMosTestCase.BufrMosTestCase):
    """Test DAF support for bufrmosHPC data"""

    datatype = "bufrmosHPC"
    data_params = "forecastHr", "maxTemp24Hour"

    # All tests inherited from superclass
