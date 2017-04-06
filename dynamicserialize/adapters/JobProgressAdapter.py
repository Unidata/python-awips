##
##


#
# Adapter for com.raytheon.uf.common.dataplugin.gfe.svcbu.JobProgress
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    06/22/2015       4573         randerso       Initial creation
#
#
#

from thrift.Thrift import TType
from dynamicserialize.dstypes.com.raytheon.uf.common.dataplugin.gfe.svcbu import JobProgress

ClassAdapter = 'com.raytheon.uf.common.dataplugin.gfe.svcbu.JobProgress'

def serialize(context, mode):
    context.protocol.writeFieldBegin('__enumValue__', TType.STRING, 0)
    context.writeString(mode.value)

def deserialize(context):
    result = JobProgress()
    # Read the TType.STRING, "__enumValue__", and id.
    # We're not interested in any of those, so just discard them.
    context.protocol.readFieldBegin()
    # now get the actual enum value
    result.value = context.readString()
    return result
