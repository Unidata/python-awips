##
##

from __future__ import print_function
from awips.dataaccess import DataAccessLayer as DAL

import baseDafTestCase
import testWarning

import unittest

#
# Test DAF support for practicewarning data
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    01/19/16        4795          mapeters       Initial Creation.
#    04/11/16        5548          tgurney        Cleanup
#    04/18/16        5548          tgurney        More cleanup
#    06/10/16        5548          tgurney        Inherit all tests from
#                                                 warning
#


class PracticeWarningTestCase(testWarning.WarningTestCase):
    """Test DAF support for practicewarning data"""

    datatype = "practicewarning"

    # All tests taken from testWarning
