#
# Adapter for java.sql.Timestamp
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    06/30/11                      dgilling      Initial Creation.
#

from dynamicserialize.dstypes.java.sql import Timestamp

ClassAdapter = 'java.sql.Timestamp'


def serialize(context, timestamp):
    context.writeI64(timestamp.getTime())


def deserialize(context):
    result = Timestamp(context.readI64())
    return result
