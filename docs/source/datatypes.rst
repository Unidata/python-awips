====================
Available Data Types
====================

.. _awips.dataaccess.DataAccessLayer.getGeometryData(request, times=[]): api/DataAccessLayer.html#awips.dataaccess.DataAccessLayer.getGeometryData

.. _awips.dataaccess.DataAccessLayer.getGridData(request, times=[]): api/DataAccessLayer.html#awips.dataaccess.DataAccessLayer.getGridData

.. _RadarCommon.get_hdf5_data(idra): api/RadarCommon.html



binlightning
------------

- Shapely Point::

    POINT (-65.65293884277344 -16.94915580749512)

- returned by `awips.dataaccess.DataAccessLayer.getGeometryData(request, times=[])`_
- example (GLM)::

    request = DataAccessLayer.newDataRequest()
    request.setDatatype("binlightning")
    request.addIdentifier("source", "GLMgr")
    request.setParameters("intensity")
    times = DataAccessLayer.getAvailableTimes(request)
    response = DataAccessLayer.getGeometryData(request, times[-10:-1])
    for ob in response:
        dir(ob.getGeometry())


------------------


grid
----

- NumPy Array
- returned by: `awips.dataaccess.DataAccessLayer.getGridData(request, times=[])`_
- example::

    request = DataAccessLayer.newDataRequest()
    request.setDatatype("grid")
    request.setLocationNames("RAP13")
    request.setParameters("T")
    request.setLevels("2.0FHAG")
    cycles = DataAccessLayer.getAvailableTimes(request, True)
    times = DataAccessLayer.getAvailableTimes(request)
    fcstRun = DataAccessLayer.getForecastRun(cycles[-1], times)
    response = DataAccessLayer.getGridData(request, [fcstRun[-1]])
    for grid in response:
        data = grid.getRawData()
        lons, lats = grid.getLatLonCoords()


------------------

warning
-------

- Shapely MultiPolygon, Polygon::

    MULTIPOLYGON ((-92.092348410 46.782322971, ..., -92.092348410 46.782322971),
                  (-90.948581075 46.992865960, ..., -90.948581075 46.992865960),
                   ...
                  (-92.274543999 46.652773000, ..., -92.280511999 46.656933000),
                  (-92.285491999 46.660741000, ..., -92.285491999 46.660741000))

- returned by `awips.dataaccess.DataAccessLayer.getGeometryData(request, times=[])`_
- example::

    request = DataAccessLayer.newDataRequest()
    request.setDatatype("warning")
    request.setParameters('phensig')
    times = DataAccessLayer.getAvailableTimes(request)
    response = DataAccessLayer.getGeometryData(request, times[-50:-1])
    for ob in response:
        poly = ob.getGeometry()
        site = ob.getLocationName()
        pd   = ob.getDataTime().getValidPeriod()
        ref  = ob.getDataTime().getRefTime()


------------------

radar
-----

- NumPy Array
- returned by: `RadarCommon.get_hdf5_data(idra)`_
- example::

    request = DataAccessLayer.newDataRequest()
    request.setDatatype("radar")
    request.setLocationNames("klzk")
    # Get latest time for site
    datatimes = DataAccessLayer.getAvailableTimes(request)
    dateTimeStr = str(datatimes[-1])
    #dateTimeStr = "2017-02-02 03:53:03"
    buffer = 60 # seconds
    dateTime = datetime.strptime(dateTimeStr, '%Y-%m-%d %H:%M:%S')
    # Build timerange +/- buffer
    beginRange = dateTime - timedelta(0, buffer)
    endRange = dateTime + timedelta(0, buffer)
    timerange = TimeRange(beginRange, endRange)
    client = ThriftClient.ThriftClient("edex-cloud.unidata.ucar.edu")
    request = GetRadarDataRecordRequest()
    request.setTimeRange(timerange)
    request.setRadarId("klzk")
    request.setProductCode("94") # N0Q
    request.setPrimaryElevationAngle("0.5")
    response = client.sendRequest(request)
    for record in response.getData():
        # Get record hdf5 data
        idra = record.getHdf5Data()
        rdat,azdat,depVals,threshVals = RadarCommon.get_hdf5_data(idra)
        dim = rdat.getDimension()
        lat,lon = float(record.getLatitude()),float(record.getLongitude())
        radials,rangeGates = rdat.getSizes()
        # Convert raw byte to pixel value
        rawValue=np.array(rdat.getByteData())
