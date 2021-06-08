#
# Adapter for java.lang.StackTraceElement[]
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    09/21/10                      njensen       Initial Creation.
#

import dynamicserialize
from dynamicserialize.dstypes.java.lang import StackTraceElement

ClassAdapter = 'java.lang.StackTraceElement'


def serialize(context, obj):
    raise dynamicserialize.SerializationException('Not implemented yet')


def deserialize(context):
    result = StackTraceElement()
    result.setDeclaringClass(context.readString())
    result.setMethodName(context.readString())
    result.setFileName(context.readString())
    result.setLineNumber(context.readI32())
    return result
