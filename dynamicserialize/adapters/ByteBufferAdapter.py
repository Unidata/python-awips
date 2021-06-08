#
# Adapter for java.nio.ByteBuffer
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    08/03/11                      dgilling       Initial Creation.
#

ClassAdapter = ['java.nio.ByteBuffer', 'java.nio.HeapByteBuffer']


def serialize(context, bufferset):
    raise NotImplementedError("Serialization of ByteBuffers is not supported.")


def deserialize(context):
    byteBuf = context.readBinary()
    return byteBuf
