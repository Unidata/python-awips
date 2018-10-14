#
# A port of the Java DynamicSerializeManager.  Should be used to read/write
# DynamicSerialize binary data.
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    06/09/10                      njensen       Initial Creation.
#

from thrift.transport import TTransport
from . import SelfDescribingBinaryProtocol, ThriftSerializationContext


class DynamicSerializationManager:

    def __init__(self):
        self.transport = None

    def _deserialize(self, ctx):
        return ctx.deserializeMessage()

    def deserializeBytes(self, bytes):
        ctx = self._buildSerializationContext(bytes)
        ctx.readMessageStart()
        obj = self._deserialize(ctx)
        ctx.readMessageEnd()
        return obj

    def _buildSerializationContext(self, bytes=None):
        self.transport = TTransport.TMemoryBuffer(bytes)
        protocol = SelfDescribingBinaryProtocol.SelfDescribingBinaryProtocol(self.transport)
        return ThriftSerializationContext.ThriftSerializationContext(self, protocol)

    def serializeObject(self, obj):
        ctx = self._buildSerializationContext()
        ctx.writeMessageStart("dynamicSerialize")
        self._serialize(ctx, obj)
        ctx.writeMessageEnd()
        return self.transport.getvalue()

    def _serialize(self, ctx, obj):
        ctx.serializeMessage(obj)
