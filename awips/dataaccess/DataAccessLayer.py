#
# Published interface for awips.dataaccess package
#
#
#     SOFTWARE HISTORY
#
#    Date           Ticket#  Engineer    Description
#    ------------   -------  ----------  -------------------------
#    12/10/12                njensen     Initial Creation.
#    Feb 14, 2013   1614     bsteffen    refactor data access framework to use single request.
#    04/10/13       1871     mnash       move getLatLonCoords to JGridData and add default args
#    05/29/13       2023     dgilling    Hook up ThriftClientRouter.
#    03/03/14       2673     bsteffen    Add ability to query only ref times.
#    07/22/14       3185     njensen     Added optional/default args to newDataRequest
#    07/30/14       3185     njensen     Renamed valid identifiers to optional
#    Apr 26, 2015   4259     njensen     Updated for new JEP API
#    Apr 13, 2016   5379     tgurney     Add getIdentifierValues(), getRequiredIdentifiers(),
#                                        and getOptionalIdentifiers()
#    Oct 07, 2016   ----     mjames@ucar Added getForecastRun
#    Oct 18, 2016   5916     bsteffen    Add setLazyLoadGridLatLon
#    Oct 11, 2018   ----     mjames@ucar Added getMetarObs() getSynopticObs()
#

import sys
import warnings

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


def getRadarProductIDs(availableParms):
    """
    Get only the numeric idetifiers for NEXRAD3 products.

    Args:
            availableParms: Full list of radar parameters

    Returns:
            List of filtered parameters
    """
    productIDs = []
    for p in list(availableParms):
        try:
            if isinstance(int(p), int):
                productIDs.append(str(p))
        except ValueError:
            pass

    return productIDs


def getRadarProductNames(availableParms):
    """
     Get only the named idetifiers for NEXRAD3 products.

    Args:
            availableParms: Full list of radar parameters

    Returns:
            List of filtered parameters
    """
    productNames = []
    for p in list(availableParms):
        if len(p) > 3:
            productNames.append(p)

    return productNames


def getMetarObs(response):
    """
    Processes a DataAccessLayer "obs" response into a dictionary,
    with special consideration for multi-value parameters
    "presWeather", "skyCover", and "skyLayerBase".

    Args:
            response: DAL getGeometry() list

    Returns:
            A dictionary of METAR obs
    """
    from datetime import datetime
    single_val_params = ["timeObs", "stationName", "longitude", "latitude",
                         "temperature", "dewpoint", "windDir",
                         "windSpeed", "seaLevelPress"]
    multi_val_params = ["presWeather", "skyCover", "skyLayerBase"]
    params = single_val_params + multi_val_params
    station_names, pres_weather, sky_cov, sky_layer_base = [], [], [], []
    obs = dict({params: [] for params in params})
    for ob in response:
        avail_params = ob.getParameters()
        if "presWeather" in avail_params:
            pres_weather.append(ob.getString("presWeather"))
        elif "skyCover" in avail_params and "skyLayerBase" in avail_params:
            sky_cov.append(ob.getString("skyCover"))
            sky_layer_base.append(ob.getNumber("skyLayerBase"))
        else:
            # If we already have a record for this stationName, skip
            if ob.getString('stationName') not in station_names:
                station_names.append(ob.getString('stationName'))
                for param in single_val_params:
                    if param in avail_params:
                        if param == 'timeObs':
                            obs[param].append(datetime.fromtimestamp(ob.getNumber(param) / 1000.0))
                        else:
                            try:
                                obs[param].append(ob.getNumber(param))
                            except TypeError:
                                obs[param].append(ob.getString(param))
                    else:
                        obs[param].append(None)

                obs['presWeather'].append(pres_weather)
                obs['skyCover'].append(sky_cov)
                obs['skyLayerBase'].append(sky_layer_base)
                pres_weather = []
                sky_cov = []
                sky_layer_base = []
    return obs


def getSynopticObs(response):
    """
    Processes a DataAccessLayer "sfcobs" response into a dictionary
    of available parameters.

    Args:
            response: DAL getGeometry() list

    Returns:
            A dictionary of synop obs
    """
    from datetime import datetime
    station_names = []
    params = response[0].getParameters()
    sfcobs = dict({params: [] for params in params})
    for sfcob in response:
        # If we already have a record for this stationId, skip
        if sfcob.getString('stationId') not in station_names:
            station_names.append(sfcob.getString('stationId'))
            for param in params:
                if param == 'timeObs':
                    sfcobs[param].append(datetime.fromtimestamp(sfcob.getNumber(param) / 1000.0))
                else:
                    try:
                        sfcobs[param].append(sfcob.getNumber(param))
                    except TypeError:
                        sfcobs[param].append(sfcob.getString(param))

    return sfcobs


def getForecastRun(cycle, times):
    """
    Get the latest forecast run (list of objects) from all
    all cycles and times returned from DataAccessLayer "grid"
    response.

    Args:
            cycle: Forecast cycle reference time
            times: All available times/cycles

    Returns:
            DataTime array for a single forecast run
    """
    fcstRun = []
    for t in times:
        if str(t)[:19] == str(cycle):
            fcstRun.append(t)
    return fcstRun


def getAvailableTimes(request, refTimeOnly=False):
    """
    Get the times of available data to the request.

    Args:
            request: the IDataRequest to get data for
            refTimeOnly: optional, use True if only unique refTimes should be
                returned (without a forecastHr)

    Returns:
            a list of DataTimes
    """
    return router.getAvailableTimes(request, refTimeOnly)


def getGridData(request, times=[]):
    """
    Gets the grid data that matches the request at the specified times.  Each
    combination of parameter, level, and dataTime will be returned as a
    separate IGridData.

    Args:
            request: the IDataRequest to get data for
            times: a list of DataTimes, a TimeRange, or None if the data is time
                agnostic

    Returns:
            a list of IGridData
    """
    return router.getGridData(request, times)


def getGeometryData(request, times=[]):
    """
    Gets the geometry data that matches the request at the specified times.
    Each combination of geometry, level, and dataTime will be returned as a
    separate IGeometryData.

    Args:
            request: the IDataRequest to get data for
            times: a list of DataTimes, a TimeRange, or None if the data is time
                agnostic

    Returns:
       a list of IGeometryData
    """
    return router.getGeometryData(request, times)


def getAvailableLocationNames(request):
    """
    Gets the available location names that match the request without actually
    requesting the data.

    Args:
            request: the request to find matching location names for

    Returns:
            a list of strings of available location names.
    """
    return router.getAvailableLocationNames(request)


def getAvailableParameters(request):
    """
    Gets the available parameters names that match the request without actually
    requesting the data.

    Args:
            request: the request to find matching parameter names for

    Returns:
            a list of strings of available parameter names.
    """
    return router.getAvailableParameters(request)


def getAvailableLevels(request):
    """
    Gets the available levels that match the request without actually
    requesting the data.

    Args:
            request: the request to find matching levels for

    Returns:
            a list of strings of available levels.
    """
    return router.getAvailableLevels(request)


def getRequiredIdentifiers(request):
    """
    Gets the required identifiers for this request.  These identifiers
    must be set on a request for the request of this datatype to succeed.

    Args:
            request: the request to find required identifiers for

    Returns:
            a list of strings of required identifiers
    """
    if str(request) == request:
        warnings.warn("Use getRequiredIdentifiers(IDataRequest) instead",
                      DeprecationWarning)
    return router.getRequiredIdentifiers(request)


def getOptionalIdentifiers(request):
    """
    Gets the optional identifiers for this request.

    Args:
            request: the request to find optional identifiers for

    Returns:
            a list of strings of optional identifiers
    """
    if str(request) == request:
        warnings.warn("Use getOptionalIdentifiers(IDataRequest) instead",
                      DeprecationWarning)
    return router.getOptionalIdentifiers(request)


def getIdentifierValues(request, identifierKey):
    """
    Gets the allowed values for a particular identifier on this datatype.

    Args:
            request: the request to find identifier values for
            identifierKey: the identifier to find values for

    Returns:
            a list of strings of allowed values for the specified identifier
    """
    return router.getIdentifierValues(request, identifierKey)


def newDataRequest(datatype=None, **kwargs):
    """
    Creates a new instance of IDataRequest suitable for the runtime environment.
    All args are optional and exist solely for convenience.

    Args:
            datatype: the datatype to create a request for
            parameters: a list of parameters to set on the request
            levels: a list of levels to set on the request
            locationNames: a list of locationNames to set on the request
            envelope: an envelope to limit the request
            kwargs: any leftover kwargs will be set as identifiers

    Returns:
            a new IDataRequest
    """
    return router.newDataRequest(datatype, **kwargs)


def getSupportedDatatypes():
    """
    Gets the datatypes that are supported by the framework

    Returns:
            a list of strings of supported datatypes
    """
    return router.getSupportedDatatypes()


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


def setLazyLoadGridLatLon(lazyLoadGridLatLon):
    """
    Provide a hint to the Data Access Framework indicating whether to load the
    lat/lon data for a grid immediately or wait until it is needed. This is
    provided as a performance tuning hint and should not affect the way the
    Data Access Framework is used. Depending on the internal implementation of
    the Data Access Framework this hint might be ignored. Examples of when this
    should be set to True are when the lat/lon information is not used or when
    it is used only if certain conditions within the data are met. It could be
    set to False if it is guaranteed that all lat/lon information is needed and
    it would be better to get any performance overhead for generating the
    lat/lon data out of the way during the initial request.


    Args:
            lazyLoadGridLatLon: Boolean value indicating whether to lazy load.
    """
    try:
        router.setLazyLoadGridLatLon(lazyLoadGridLatLon)
    except AttributeError:
        # The router is not required to support this capability.
        pass
