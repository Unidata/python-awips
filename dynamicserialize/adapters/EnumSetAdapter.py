#
# Adapter for java.util.EnumSet
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    07/28/11                      dgilling       Initial Creation.
#    12/02/13        2537          bsteffen       Serialize empty enum sets.
#

from dynamicserialize.dstypes.java.util import EnumSet

ClassAdapter = ['java.util.EnumSet', 'java.util.RegularEnumSet']


def serialize(context, set):
    setSize = len(set)
    context.writeI32(setSize)
    context.writeString(set.getEnumClass())
    for val in set:
        context.writeString(val)


def deserialize(context):
    setSize = context.readI32()
    enumClassName = context.readString()
    valList = []
    for i in range(setSize):
        valList.append(context.readString())
    return EnumSet(enumClassName, valList)
