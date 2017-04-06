##
##


#
# Adapter for com.raytheon.uf.common.message.WsId
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    09/16/10                      dgilling       Initial Creation.
#    04/25/12              545     randerso       Repurposed the lockKey field as threadId
#
#
#



from dynamicserialize.dstypes.com.raytheon.uf.common.message import WsId

ClassAdapter = 'com.raytheon.uf.common.message.WsId'


def serialize(context, wsId):
    context.writeString(wsId.toString())

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

