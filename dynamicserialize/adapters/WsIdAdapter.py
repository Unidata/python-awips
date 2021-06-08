#
# Adapter for com.raytheon.uf.common.message.WsId
#
#
# SOFTWARE HISTORY
#
# Date          Ticket#  Engineer  Description
# ------------- -------- --------- ---------------------------------------------
# Sep 16, 2010           dgilling  Initial Creation.
# Apr 25, 2012  545      randerso  Repurposed the lockKey field as threadId
# Feb 06, 2017  5959     randerso  Removed Java .toString() calls
#

from dynamicserialize.dstypes.com.raytheon.uf.common.message import WsId

ClassAdapter = 'com.raytheon.uf.common.message.WsId'


def serialize(context, wsId):
    context.writeString(str(wsId))


def deserialize(context):
    wsIdString = context.readString()
    wsIdParts = wsIdString.split(":", 5)
    wsId = WsId()
    wsId.setNetworkId(wsIdParts[0])
    wsId.setUserName(wsIdParts[1])
    wsId.setProgName(wsIdParts[2])
    wsId.setPid(wsIdParts[3])
    wsId.setThreadId(int(wsIdParts[4]))
    return wsId
