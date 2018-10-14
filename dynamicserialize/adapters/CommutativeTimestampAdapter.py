#
# Adapter for CommutativeTimestamp
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    9/21/2015       4486          rjpeter        Initial creation.
#    Jun 23, 2016    5696          rjpeter        Handle CommutativeTimestamp.
#

from dynamicserialize.dstypes.com.raytheon.uf.common.time import CommutativeTimestamp

ClassAdapter = 'com.raytheon.uf.common.time.CommutativeTimestamp'


def serialize(context, date):
    context.writeI64(date.getTime())


def deserialize(context):
    result = CommutativeTimestamp()
    result.setTime(context.readI64())
    return result
