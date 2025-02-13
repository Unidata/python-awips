##
# This software was developed and / or modified by Raytheon Company,
# pursuant to Contract DG133W-05-CQ-1067 with the US Government.
# 
# U.S. EXPORT CONTROLLED TECHNICAL DATA
# This software product contains export-restricted data whose
# export/transfer/disclosure is restricted by U.S. law. Dissemination
# to non-U.S. persons whether in the United States or abroad requires
# an export license or other authorization.
# 
# Contractor Name:        Raytheon Company
# Contractor Address:     6825 Pine Street, Suite 340
#                         Mail Stop B8
#                         Omaha, NE 68106
#                         402.291.0100
# 
# See the AWIPS II Master Rights File ("Master Rights File.pdf") for
# further licensing information.
##


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
# Jun 24, 2020  8187     randerso  Changed to use hostName instead of integer
#                                  network address.
# Dec 08, 2020  8239     randerso  Undo change to use hostName instead of 
#                                  integer network address.
#                                  Re-implemented for greater efficiency
# 
##



from dynamicserialize.dstypes.com.raytheon.uf.common.message import WsId

ClassAdapter = 'com.raytheon.uf.common.message.WsId'


def serialize(context, wsId):
    context.writeString(str(wsId))

def deserialize(context):
    wsIdString = context.readString()
    wsIdParts = wsIdString.split(":", 5)
    
    wsId = WsId(networkId=wsIdParts[0], 
                userName=wsIdParts[1], 
                progName=wsIdParts[2], 
                pid=int(wsIdParts[3]), 
                threadId=int(wsIdParts[4]))
    
    return wsId

