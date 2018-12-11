====================
Available Data Types
====================

.. _awips.dataaccess.DataAccessLayer.getGeometryData(request, times=[]): api/DataAccessLayer.html#awips.dataaccess.DataAccessLayer.getGeometryData

.. _awips.dataaccess.DataAccessLayer.getGridData(request, times=[]): api/DataAccessLayer.html#awips.dataaccess.DataAccessLayer.getGridData

.. _RadarCommon.get_hdf5_data(idra): api/RadarCommon.html



satellite
---------

- 2-D NumPy Array
- returned by: `awips.dataaccess.DataAccessLayer.getGridData(request, times=[])`_
- example::

    # Contrust a full satellite product tree
    DataAccessLayer.changeEDEXHost("edex-cloud.unidata.ucar.edu)
    request = DataAccessLayer.newDataRequest("satellite")
    creatingEntities = DataAccessLayer.getIdentifierValues(request, "creatingEntity")
    for entity in creatingEntities:
        print(entity)
        request = DataAccessLayer.newDataRequest("satellite")
        request.addIdentifier("creatingEntity", entity)
        availableSectors = DataAccessLayer.getAvailableLocationNames(request)
        availableSectors.sort()
        for sector in availableSectors:
            print(" - " + sector)
            request.setLocationNames(sector)
            availableProducts = DataAccessLayer.getAvailableParameters(request)
            availableProducts.sort()
            for product in availableProducts:
                print("    - " + product)

---

binlightning
------------

- Shapely Point::

    POINT (-65.65293884277344 -16.94915580749512)

- returned by: `awips.dataaccess.DataAccessLayer.getGeometryData(request, times=[])`_
- example (GLM)::

    request = DataAccessLayer.newDataRequest("binlightning")
    request.addIdentifier("source", "GLMgr")
    request.setParameters("intensity")
    times = DataAccessLayer.getAvailableTimes(request)
    response = DataAccessLayer.getGeometryData(request, times[-10:-1])
    for ob in response:
        geom = ob.getGeometry()

---


grid
----

- 2-D NumPy Array
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


---

warning
-------

- Shapely MultiPolygon, Polygon::

    MULTIPOLYGON ((-92.092348410 46.782322971, ..., -92.092348410 46.782322971),
                  (-90.948581075 46.992865960, ..., -90.948581075 46.992865960),
                   ...
                  (-92.274543999 46.652773000, ..., -92.280511999 46.656933000),
                  (-92.285491999 46.660741000, ..., -92.285491999 46.660741000))

- returned by: `awips.dataaccess.DataAccessLayer.getGeometryData(request, times=[])`_
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


---

radar
-----

- 2-D NumPy Array
- returned by: `awips.dataaccess.DataAccessLayer.getGridData(request, times=[])`_
- also returned by: `RadarCommon.get_hdf5_data(idra)`_
- example::

    request = DataAccessLayer.newDataRequest("radar")
    request.setLocationNames("kmhx")
    request.setParameters("Digital Hybrid Scan Refl")
    availableLevels = DataAccessLayer.getAvailableLevels(request)
    times = DataAccessLayer.getAvailableTimes(request)
    response = DataAccessLayer.getGridData(request, [times[-1]])
    for image in response:
        data = image.getRawData()
        lons, lats = image.getLatLonCoords()

