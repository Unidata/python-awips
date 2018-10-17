from dynamicserialize.dstypes.com.raytheon.uf.common.auth.user import UserId


class User(object):

    def __init__(self, userId=None):
        if userId is None:
            self.userId = UserId.UserId()
        else:
            self.userId = userId
        self.authenticationData = None

    def getUserId(self):
        return self.userId

    def setUserId(self, userId):
        self.userId = userId

    def getAuthenticationData(self):
        return self.authenticationData

    def setAuthenticationData(self, authenticationData):
        self.authenticationData = authenticationData
