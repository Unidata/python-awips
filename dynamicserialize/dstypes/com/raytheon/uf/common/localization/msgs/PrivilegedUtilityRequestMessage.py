##
##

# File auto-generated against equivalent DynamicSerialize Java class

from dynamicserialize.dstypes.com.raytheon.uf.common.plugin.nwsauth.user import User

class PrivilegedUtilityRequestMessage(object):

    def __init__(self):
        self.commands = None
        self.user = User()

    def getCommands(self):
        return self.commands

    def setCommands(self, commands):
        self.commands = commands

    def getUser(self):
        return self.user

    def setUser(self, user):
        self.user = user

