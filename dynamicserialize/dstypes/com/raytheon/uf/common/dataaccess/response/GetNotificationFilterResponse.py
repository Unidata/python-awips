

class GetNotificationFilterResponse(object):

    def __init__(self):
        self.notificationFilter = None
        self.jmsConnectionInfo = None

    def getNotificationFilter(self):
        return self.notificationFilter

    def setNotificationFilter(self, notificationFilter):
        self.notificationFilter = notificationFilter

    def getJmsConnectionInfo(self):
        return self.jmsConnectionInfo

    def setJmsConnectionInfo(self, jmsConnectionInfo):
        self.jmsConnectionInfo = jmsConnectionInfo
