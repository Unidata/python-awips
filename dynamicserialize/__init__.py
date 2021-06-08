#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    08/20/10                      njensen       Initial Creation.
#
#

__all__ = ['SerializationException']

from . import dstypes, adapters
from . import DynamicSerializationManager


class SerializationException(Exception):

    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        if self.message:
            return self.message
        else:
            return ""


def serialize(obj):
    dsm = DynamicSerializationManager.DynamicSerializationManager()
    return dsm.serializeObject(obj)


def deserialize(objbytes):
    dsm = DynamicSerializationManager.DynamicSerializationManager()
    return dsm.deserializeBytes(objbytes)
