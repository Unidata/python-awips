#
# Notification object that produces grid data
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    06/03/16        2416          rjpeter        Initial Creation.
#    09/06/17        6175          tgurney        Override messageReceived
#

import dynamicserialize
import traceback
from awips.dataaccess.PyNotification import PyNotification


class PyGridNotification(PyNotification):

    def messageReceived(self, msg):
        dataUriMsg = dynamicserialize.deserialize(msg)
        dataUris = dataUriMsg.getDataURIs()
        for dataUri in dataUris:
            if not self.notificationFilter.accept(dataUri):
                continue
            try:
                # This improves performance over requesting by datatime since it requests only the
                # parameter that the notification was received for (instead of this and all previous
                # parameters for the same forecast hour)
                # TODO: This utterly fails for derived requests
                newReq = self.DAL.newDataRequest(self.request.getDatatype())
                newReq.addIdentifier("dataURI", dataUri)
                newReq.setParameters(self.request.getParameters())
                data = self.getData(newReq, [])
                self.callback(data)
            except ValueError:
                traceback.print_exc()

    def getData(self, request, dataTimes):
        return self.DAL.getGridData(request, dataTimes)
