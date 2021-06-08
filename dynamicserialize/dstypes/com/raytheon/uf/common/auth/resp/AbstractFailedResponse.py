from six import with_metaclass
import abc


class AbstractFailedResponse(with_metaclass(abc.ABCMeta, object)):
    @abc.abstractmethod
    def __init__(self):
        self.request = None

    def getRequest(self):
        return self.request

    def setRequest(self, request):
        self.request = request
