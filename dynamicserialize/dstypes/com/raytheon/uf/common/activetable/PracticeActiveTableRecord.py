##
##
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    05/22/2015       4522         randerso       Changed to inherit from ActiveTableRecord
#
##

from . import ActiveTableRecord

class PracticeActiveTableRecord(ActiveTableRecord):

    def __init__(self):
        super(PracticeActiveTableRecord, self).__init__()
