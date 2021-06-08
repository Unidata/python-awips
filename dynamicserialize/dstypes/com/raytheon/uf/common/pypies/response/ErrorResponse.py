

class ErrorResponse(object):

    def __init__(self):
        self.error = None

    def getError(self):
        return self.error

    def setError(self, error):
        self.error = error
