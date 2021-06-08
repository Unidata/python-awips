#
# Implements IData for use by native Python clients to the Data Access
# Framework.
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer      Description
#    ------------    ----------    -----------   --------------------------
#    Jun 22, 2016    2416          rjpeter       Initial creation
#    Jul 22, 2016    2416          tgurney       Finish implementation
#    Sep 07, 2017    6175          tgurney       Override messageReceived in subclasses
#

from six import with_metaclass
import abc

from awips.dataaccess import DataAccessLayer
from awips.dataaccess import INotificationSubscriber
from awips.QpidSubscriber import QpidSubscriber
from dynamicserialize.dstypes.com.raytheon.uf.common.time import DataTime


class PyNotification(with_metaclass(abc.ABCMeta, INotificationSubscriber)):
    """
    Receives notifications for new data and retrieves the data that meets
    specified filtering criteria.
    """

    def __init__(self, request, notificationFilter, host='localhost',
                 port=5672, requestHost='localhost'):
        self.DAL = DataAccessLayer
        self.DAL.changeEDEXHost(requestHost)
        self.request = request
        self.notificationFilter = notificationFilter
        self.__topicSubscriber = QpidSubscriber(host, port, decompress=True)
        self.__topicName = "edex.alerts"
        self.callback = None

    def subscribe(self, callback):
        """
        Start listening for notifications.

        Args:
            callback: Function to call with a list of received data objects.
              Will be called once for each request made for data.
        """
        assert hasattr(callback, '__call__'), 'callback arg must be callable'
        self.callback = callback
        self.__topicSubscriber.topicSubscribe(self.__topicName, self.messageReceived)
        # Blocks here

    def close(self):
        if self.__topicSubscriber.subscribed:
            self.__topicSubscriber.close()

    def getDataTime(self, dataURI):
        dataTimeStr = dataURI.split('/')[2]
        return DataTime(dataTimeStr)

    @abc.abstractmethod
    def messageReceived(self, msg):
        """Called when a message is received from QpidSubscriber.

        This method must call self.callback once for each request made for data
        """
        pass

    @abc.abstractmethod
    def getData(self, request, dataTimes):
        """
        Retrieve and return data

        Args:
            request: IDataRequest to send to the server
            dataTimes: list of data times
        Returns:
            list of IData
        """
        pass

    @property
    def subscribed(self):
        """True if currently subscribed to notifications."""
        return self.__topicSubscriber.queueStarted
