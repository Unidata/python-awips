# #
# This software was developed and / or modified by Raytheon Company,
# pursuant to Contract DG133W-05-CQ-1067 with the US Government.
#
# U.S. EXPORT CONTROLLED TECHNICAL DATA
# This software product contains export-restricted data whose
# export/transfer/disclosure is restricted by U.S. law. Dissemination
# to non-U.S. persons whether in the United States or abroad requires
# an export license or other authorization.
#
# Contractor Name:        Raytheon Company
# Contractor Address:     6825 Pine Street, Suite 340
#                         Mail Stop B8
#                         Omaha, NE 68106
#                         402.291.0100
#
# See the AWIPS II Master Rights File ("Master Rights File.pdf") for
# further licensing information.
# #


#
# Published interface for awips.dataaccess package
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    12/10/12                      njensen        Initial Creation.
#    Feb 14, 2013    1614          bsteffen       refactor data access framework
#                                                 to use single request.
#    04/10/13         1871         mnash          move getLatLonCoords to JGridData and add default args
#    05/29/13         2023         dgilling       Hook up ThriftClientRouter.
#    03/03/14         2673         bsteffen       Add ability to query only ref times.
#    07/22/14         3185         njensen        Added optional/default args to newDataRequest
#    07/30/14         3185         njensen        Renamed valid identifiers to optional
#    Apr 26, 2015     4259         njensen        Updated for new JEP API
#
#
#


import sys
import subprocess

THRIFT_HOST = "edex"
USING_NATIVE_THRIFT = False

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

def getForecastCycle(cycle, times):
    """
    :param cycle: Forecast cycle reference time
    :param times: All available times/cycles
    :return: DataTime array for a single forecast run
    """
    forecast_run = []
    for time in times:
        if time.getRefTime() == cycle.getRefTime():
            forecast_run.append(time)
    return forecast_run

def getAvailableTimes(request, refTimeOnly=False):
    """
    Get the times of available data to the request.

    :param request: the IDataRequest to get data for
    :param refTimeOnly: optional, use True if only unique refTimes should be returned (without a forecastHr)

    :returns: a list of DataTimes
    """
    return router.getAvailableTimes(request, refTimeOnly)

def getGridData(request, times=[]):
    """
    Gets the grid data that matches the request at the specified times.  Each
    combination of parameter, level, and dataTime will be returned as a
    separate IGridData.

    :param request: the IDataRequest to get data for
    :param times: a list of DataTimes, a TimeRange, or None if the data is time agnostic

    :returns: a list of IGridData
    """
    return router.getGridData(request, times)

def getGeometryData(request, times=[]):
    """
    Gets the geometry data that matches the request at the specified times.
    Each combination of geometry, level, and dataTime will be returned as a
    separate IGeometryData.

    :param request: the IDataRequest to get data for
    :param times: a list of DataTimes, a TimeRange, or None if the data is time agnostic

    :returns: a list of IGeometryData
    """
    return router.getGeometryData(request, times)

def getAvailableLocationNames(request):
    """
    Gets the available location names that match the request without actually
    requesting the data.

    :param request: the request to find matching location names for

    :returns: a list of strings of available location names.
    """
    return router.getAvailableLocationNames(request)

def getAvailableParameters(request):
    """
    Gets the available parameters names that match the request without actually
    requesting the data.

    :param request: the request to find matching parameter names for

    :returns: a list of strings of available parameter names.
    """
    return router.getAvailableParameters(request)

def getAvailableLevels(request):
    """
    Gets the available levels that match the request without actually
    requesting the data.

    :param request: the request to find matching levels for

    :returns: a list of strings of available levels.
    """
    return router.getAvailableLevels(request)

def getRequiredIdentifiers(datatype):
    """
    Gets the required identifiers for this datatype.  These identifiers
    must be set on a request for the request of this datatype to succeed.

    :param datatype: the datatype to find required identifiers for

    :returns: a list of strings of required identifiers
    """
    return router.getRequiredIdentifiers(datatype)

def getOptionalIdentifiers(datatype):
    """
    Gets the optional identifiers for this datatype.

    :param datatype: the datatype to find optional identifiers for

    :returns: a list of strings of optional identifiers
    """
    return router.getOptionalIdentifiers(datatype)

def newDataRequest(datatype=None, **kwargs):
    """
    Creates a new instance of IDataRequest suitable for the runtime environment.
    All args are optional and exist solely for convenience.

    :param datatype: the datatype to create a request for
    :param parameters: a list of parameters to set on the request
    :param levels: a list of levels to set on the request
    :param locationNames: a list of locationNames to set on the request
    :param envelope: an envelope to limit the request
    :param kwargs: any leftover kwargs will be set as identifiers

    :returns: a new IDataRequest
    """
    return router.newDataRequest(datatype, **kwargs)

def getSupportedDatatypes():
    """
    Gets the datatypes that are supported by the framework

    :returns: a list of strings of supported datatypes
    """
    return router.getSupportedDatatypes()


def changeEDEXHost(newHostName):
    """
    Changes the EDEX host the Data Access Framework is communicating with. Only
    works if using the native Python client implementation, otherwise, this
    method will throw a TypeError.

    :param newHostHame: the EDEX host to connect to
    """
    if USING_NATIVE_THRIFT:
        global THRIFT_HOST
        THRIFT_HOST = newHostName
        global router
        router = ThriftClientRouter.ThriftClientRouter(THRIFT_HOST)
    else:
        raise TypeError("Cannot call changeEDEXHost when using JepRouter.")
