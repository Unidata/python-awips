#
# SOFTWARE HISTORY
#
# Date          Ticket#  Engineer  Description
# ------------- -------- --------- ---------------------------------------------
# Apr 25, 2012  545      randerso  Repurposed the lockKey field as threadId
# Jun 12, 2013  2099     dgilling  Implemented toPrettyString().
# Feb 06, 2017  5959     randerso  Removed Java .toString() calls
#

import struct
import socket
import os
try:
    import pwd
    pwd_error = False
except ImportError:
    pwd_error = True
try:
    import _thread
except ImportError:
    import thread as _thread


class WsId(object):

    def __init__(self, networkId=None, userName=None, progName=None):
        self.networkId = networkId
        if networkId is None:
            self.networkId = str(struct.unpack('<L', socket.inet_aton(socket.gethostbyname(socket.gethostname())))[0])

        self.userName = userName
        if userName is None:
            if not pwd_error:
                self.userName = pwd.getpwuid(os.getuid()).pw_name
            else:
                self.userName = "GenericUsername"

        self.progName = progName
        if progName is None:
            self.progName = "unknown"

        self.pid = os.getpid()

        self.threadId = int(_thread.get_ident())

    def getNetworkId(self):
        return self.networkId

    def setNetworkId(self, networkId):
        self.networkId = networkId

    def getUserName(self):
        return self.userName

    def setUserName(self, userName):
        self.userName = userName

    def getProgName(self):
        return self.progName

    def setProgName(self, progName):
        self.progName = progName

    def getPid(self):
        return self.pid

    def setPid(self, pid):
        self.pid = pid

    def getThreadId(self):
        return self.threadId

    def setThreadId(self, threadId):
        self.threadId = threadId

    def toPrettyString(self):
        hostname = socket.gethostbyaddr(socket.inet_ntoa(struct.pack('<L', int(self.networkId))))[0]
        return self.userName + "@" + hostname + ":" + self.progName + ":" + str(self.pid) + ":" + str(self.threadId)

    def __str__(self):
        return self.networkId + ":" + self.userName + ":" + self.progName + ":" \
               + str(self.pid) + ":" + str(self.threadId)

    def __repr__(self):
        return self.__str__()
