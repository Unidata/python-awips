

class StackTraceElement(object):

    def __init__(self):
        self.declaringClass = None
        self.methodName = None
        self.fileName = None
        self.lineNumber = 0

    def getDeclaringClass(self):
        return self.declaringClass

    def setDeclaringClass(self, clz):
        self.declaringClass = clz

    def getMethodName(self):
        return self.methodName

    def setMethodName(self, methodName):
        self.methodName = methodName

    def getFileName(self):
        return self.fileName

    def setFileName(self, filename):
        self.fileName = filename

    def getLineNumber(self):
        return self.lineNumber

    def setLineNumber(self, lineNumber):
        self.lineNumber = int(lineNumber)

    def isNativeMethod(self):
        return self.lineNumber == -2

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        msg = self.declaringClass.decode('cp437') + "." + self.methodName.decode('cp437')
        if self.isNativeMethod():
            msg += "(Native Method)"
        elif self.fileName is not None and self.lineNumber >= 0:
            msg += "(" + self.fileName.decode('cp437') + ":" + str(self.lineNumber) + ")"
        elif self.fileName is not None:
            msg += "(" + self.fileName.decode('cp437') + ")"
        else:
            msg += "(Unknown Source)"
        return msg
