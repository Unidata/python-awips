#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    07/23/14         #3185        njensen        Initial Creation.
#    Jun 01, 2016     5587         tgurney        Change self.datatype to
#                                                 self.request
#
#

from six import with_metaclass
import abc


class AbstractIdentifierRequest(with_metaclass(abc.ABCMeta, object)):
    def __init__(self):
        self.request = None

    def getRequest(self):
        return self.request

    def setRequest(self, request):
        self.request = request

