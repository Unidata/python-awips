#
# Published interface for retrieving data updates via awips.dataaccess package
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    May 26, 2016    2416          rjpeter        Initial Creation.
#    Aug  1, 2016    2416          tgurney        Finish implementation
#
#

"""
Interface for the DAF's data notification feature, which allows continuous
retrieval of new data as it is coming into the system.

There are two ways to access this feature:

1. The DataQueue module (awips.dataaccess.DataQueue) offers a collection that
automatically fills up with new data as it receives notifications. See that
module for more information.

2. Depending on the type of data you want, use either getGridDataUpdates() or
getGeometryDataUpdates() in this module. Either one will give you back an
object that will retrieve new data for you and will call a function you specify
each time new data is received.

Example code follows. This example prints temperature as observed from KOMA
each time a METAR is received from there.

  from awips.dataaccess import DataAccessLayer as DAL
  from awips.dataaccess import DataNotificationLayer as DNL

  def process_obs(list_of_data):
      for item in list_of_data:
          print(item.getNumber('temperature'))

  request = DAL.newDataRequest('obs')
  request.setParameters('temperature')
  request.setLocationNames('KOMA')

  notifier = DNL.getGeometryDataUpdates(request)
  notifier.subscribe(process_obs)
  # process_obs will called with a list of data each time new data comes in

"""

import re
import sys
from awips.dataaccess.PyGeometryNotification import PyGeometryNotification
from awips.dataaccess.PyGridNotification import PyGridNotification


THRIFT_HOST = "edex"

USING_NATIVE_THRIFT = False

JMS_HOST_PATTERN = re.compile('tcp://([^:]+):([0-9]+)')

if 'jep' in sys.modules:
    # intentionally do not catch if this fails to import, we want it to
    # be obvious that something is configured wrong when running from within
    # Java instead of allowing false confidence and fallback behavior
    import JepRouter
    router = JepRouter
else:
    from awips.dataaccess import ThriftClientRouter
    router = ThriftClientRouter.ThriftClientRouter(THRIFT_HOST)
    USING_NATIVE_THRIFT = True


def _getJmsConnectionInfo(notifFilterResponse):
    serverString = notifFilterResponse.getJmsConnectionInfo()
    try:
        host, port = JMS_HOST_PATTERN.match(serverString).groups()
    except AttributeError:
        raise RuntimeError('Got bad JMS connection info from server: ' + serverString)
    return {'host': host, 'port': port}


def getGridDataUpdates(request):
    """
    Get a notification object that receives updates to grid data.

    Args:
            request: the IDataRequest specifying the data you want to receive

    Returns:
            an update request object that you can listen for updates to by
            calling its subscribe() method
    """
    response = router.getNotificationFilter(request)
    notificationFilter = response.getNotificationFilter()
    jmsInfo = _getJmsConnectionInfo(response)
    notifier = PyGridNotification(request, notificationFilter,
                                  requestHost=THRIFT_HOST, **jmsInfo)
    return notifier


def getGeometryDataUpdates(request):
    """
    Get a notification object that receives updates to geometry data.

    Args:
            request: the IDataRequest specifying the data you want to receive

    Returns:
            an update request object that you can listen for updates to by
            calling its subscribe() method
    """
    response = router.getNotificationFilter(request)
    notificationFilter = response.getNotificationFilter()
    jmsInfo = _getJmsConnectionInfo(response)
    notifier = PyGeometryNotification(request, notificationFilter,
                                      requestHost=THRIFT_HOST, **jmsInfo)
    return notifier


def changeEDEXHost(newHostName):
    """
    Changes the EDEX host the Data Access Framework is communicating with. Only
    works if using the native Python client implementation, otherwise, this
    method will throw a TypeError.

    Args:
            newHostName: the EDEX host to connect to
    """
    if USING_NATIVE_THRIFT:
        global THRIFT_HOST
        THRIFT_HOST = newHostName
        global router
        router = ThriftClientRouter.ThriftClientRouter(THRIFT_HOST)
    else:
        raise TypeError("Cannot call changeEDEXHost when using JepRouter.")
