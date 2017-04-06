##
##

# File auto-generated against equivalent DynamicSerialize Java class
# and then modified post-generation to make it a abstract base class.
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

import abc
from six import with_metaclass

class AbstractIdentifierRequest(with_metaclass(abc.ABCMeta, object)):
    def __init__(self):
        self.request = None

    def getRequest(self):
        return self.request

    def setRequest(self, request):
        self.request = request

