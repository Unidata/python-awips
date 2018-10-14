#
# Adapter for java.util.Date
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    12/06/10                      dgilling      Initial Creation.
#

from dynamicserialize.dstypes.java.util import Date

ClassAdapter = 'java.util.Date'


def serialize(context, date):
    context.writeI64(date.getTime())


def deserialize(context):
    result = Date()
    result.setTime(context.readI64())
    return result
