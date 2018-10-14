#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    09/21/2015      4486          rjpeter        Initial creation.
#    06/23/2016      #5696         rjpeter        Extend CommutativeTimestamp
#

from .CommutativeTimestamp import CommutativeTimestamp


# TODO: Remove after 16.4.1 no longer in field
class FormattedDate(CommutativeTimestamp):

    def __init__(self, timeInMillis=None):
        super(FormattedDate, self).__init__(timeInMillis)
