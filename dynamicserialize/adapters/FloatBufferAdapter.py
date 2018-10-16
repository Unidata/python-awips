#
# Adapter for java.nio.FloatBuffer
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    08/01/11                      dgilling       Initial Creation.
#

ClassAdapter = ['java.nio.FloatBuffer', 'java.nio.HeapFloatBuffer']


def serialize(context, bufferset):
    raise NotImplementedError("Serialization of FloatBuffers is not supported.")


def deserialize(context):
    floatBuf = context.readFloatArray()
    return floatBuf
