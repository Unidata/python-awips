##
##


#
# Pure python logging mechanism for logging to AlertViz from
# pure python (ie not JEP).  DO NOT USE IN PYTHON CALLED
# FROM JAVA.
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    11/03/10        5849          cjeanbap       Initial Creation.
#
#
#

import os
import sys

class Record():
    def __init__(self, level=0, msg='Test Message'):
        self.levelno=level
        self.message=msg
        self.exc_info=sys.exc_info()
        self.exc_text="TEST"

    def getMessage(self):
        return self.message
