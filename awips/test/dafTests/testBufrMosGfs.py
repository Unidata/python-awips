#
# Test DAF support for bufrmosGFS data
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

from awips.test.dafTests import baseBufrMosTestCase


class BufrMosGfsTestCase(baseBufrMosTestCase.BufrMosTestCase):
    """Test DAF support for bufrmosGFS data"""

    datatype = "bufrmosGFS"

    # All tests inherited from superclass
