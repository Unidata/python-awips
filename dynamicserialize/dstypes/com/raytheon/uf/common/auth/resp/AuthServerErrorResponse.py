# nothing to implement here that isn't already covered by ServerErrorResponse
# Just need the separate class for de-serialization.

from dynamicserialize.dstypes.com.raytheon.uf.common.serialization.comm.response import ServerErrorResponse


class AuthServerErrorResponse(ServerErrorResponse):

    def __init__(self):
        super(AuthServerErrorResponse, self).__init__()
