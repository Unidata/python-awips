#
# Adapter for FormattedDate
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    9/21/2015       4486          rjpeter        Initial creation.
#

from dynamicserialize.dstypes.com.raytheon.uf.common.time import FormattedDate

ClassAdapter = 'com.raytheon.uf.common.time.FormattedDate'


def serialize(context, date):
    context.writeI64(date.getTime())


def deserialize(context):
    result = FormattedDate()
    result.setTime(context.readI64())
    return result
