#
# Provides a Python-based interface for executing Thrift requests.
#
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    09/20/10                      dgilling       Initial Creation.
#
#

try:
    import http.client as httpcl
except ImportError:
    import httplib as httpcl
from dynamicserialize import DynamicSerializationManager


class ThriftClient:

    # How to call this constructor:
    #   1. Pass in all arguments separately (e.g.,
    #      ThriftClient.ThriftClient("localhost", 9581, "/services"))
    #      will return a Thrift client pointed at http://localhost:9581/services.
    #   2. Pass in all arguments through the host string (e.g.,
    #      ThriftClient.ThriftClient("localhost:9581/services"))
    #      will return a Thrift client pointed at http://localhost:9581/services.
    #   3. Pass in host/port arguments through the host string (e.g.,
    #      ThriftClient.ThriftClient("localhost:9581", "/services"))
    #      will return a Thrift client pointed at http://localhost:9581/services.
    def __init__(self, host, port=9581, uri="/services"):
        hostParts = host.split("/", 1)
        if len(hostParts) > 1:
            hostString = hostParts[0]
            self.__uri = "/" + hostParts[1]
            self.__httpConn = httpcl.HTTPConnection(hostString)
        else:
            if port is None:
                self.__httpConn = httpcl.HTTPConnection(host)
            else:
                self.__httpConn = httpcl.HTTPConnection(host, port)

            self.__uri = uri

        self.__dsm = DynamicSerializationManager.DynamicSerializationManager()

    def sendRequest(self, request, uri="/thrift"):
        message = self.__dsm.serializeObject(request)

        self.__httpConn.connect()
        self.__httpConn.request("POST", self.__uri + uri, message)

        response = self.__httpConn.getresponse()
        if response.status != 200:
            raise ThriftRequestException("Unable to post request to server")

        rval = self.__dsm.deserializeBytes(response.read())
        self.__httpConn.close()

        # let's verify we have an instance of ServerErrorResponse
        # IF we do, through an exception up to the caller along
        # with the original Java stack trace
        # ELSE: we have a valid response and pass it back
        try:
            forceError = rval.getException()
            raise ThriftRequestException(forceError)
        except AttributeError:
            pass

        return rval


class ThriftRequestException(Exception):
    def __init__(self, value):
        self.parameter = value

    def __str__(self):
        return repr(self.parameter)
