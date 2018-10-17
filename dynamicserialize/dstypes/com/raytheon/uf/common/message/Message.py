

class Message(object):

    def __init__(self, header=None, body=None):
        self.header = header
        self.body = body

    def getHeader(self):
        return self.header

    def setHeader(self, header):
        self.header = header

    def getBody(self):
        return self.body

    def setBody(self, body):
        self.body = body
