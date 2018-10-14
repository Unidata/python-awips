#
# Adapter for java.util.Calendar
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    09/29/10                      wldougher     Initial Creation.
#

from dynamicserialize.dstypes.java.util import Calendar

ClassAdapter = 'java.util.Calendar'


def serialize(context, calendar):
    calTiM = calendar.getTimeInMillis()
    context.writeI64(calTiM)


def deserialize(context):
    result = Calendar()
    result.setTimeInMillis(context.readI64())
    return result
