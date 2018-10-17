

class ServerErrorResponse(object):

    def __init__(self):
        self.exception = None

    def getException(self):
        return self.exception

    def setException(self, exception):
        self.exception = exception
