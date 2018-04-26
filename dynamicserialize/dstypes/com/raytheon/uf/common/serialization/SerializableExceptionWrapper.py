
# File auto-generated against equivalent DynamicSerialize Java class and
# modified.
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    2015-02-27      4174          nabowle        Output full stacktrace.
#

class SerializableExceptionWrapper(object):

    def __init__(self):
        self.stackTrace = None
        self.message = None
        self.exceptionClass = None
        self.wrapper = None

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        if not self.message:
            self.message = b''
        retVal = b"" + self.exceptionClass + b" exception thrown: " + self.message + b"\n"
        retVal = retVal.decode('UTF-8')
        for element in self.stackTrace:
            retVal += "\tat " + str(element) + "\n"

        if self.wrapper:
            retVal += "Caused by: " + self.wrapper.__repr__()
        return retVal

    def getStackTrace(self):
        return self.stackTrace

    def setStackTrace(self, stackTrace):
        self.stackTrace = stackTrace

    def getMessage(self):
        return self.message

    def setMessage(self, message):
        self.message = message

    def getExceptionClass(self):
        return self.exceptionClass

    def setExceptionClass(self, exceptionClass):
        self.exceptionClass = exceptionClass

    def getWrapper(self):
        return self.wrapper

    def setWrapper(self, wrapper):
        self.wrapper = wrapper

