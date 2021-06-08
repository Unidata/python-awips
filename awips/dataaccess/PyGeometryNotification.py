#
# Notification object that produces geometry data
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    07/22/16        2416          tgurney        Initial creation
#    09/07/17        6175          tgurney        Override messageReceived
#

import traceback
import dynamicserialize
from awips.dataaccess.PyNotification import PyNotification


class PyGeometryNotification(PyNotification):

    def messageReceived(self, msg):
        dataUriMsg = dynamicserialize.deserialize(msg)
        dataUris = dataUriMsg.getDataURIs()
        dataTimes = set()
        for dataUri in dataUris:
            if self.notificationFilter.accept(dataUri):
                dataTimes.add(self.getDataTime(dataUri))
        if dataTimes:
            try:
                data = self.getData(self.request, list(dataTimes))
                self.callback(data)
            except ValueError:
                traceback.print_exc()

    def getData(self, request, dataTimes):
        return self.DAL.getGeometryData(request, dataTimes)
