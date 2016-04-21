===========
Surface Obs
===========
`Notebook <http://nbviewer.ipython.org/github/Unidata/python-awips/blob/master/examples/notebooks/Surface_Obs.ipynb>`_

.. code:: python

    from awips.dataaccess import DataAccessLayer
    
    # Set host
    DataAccessLayer.changeEDEXHost("edex-cloud.unidata.ucar.edu")
    # Init data request
    request = DataAccessLayer.newDataRequest()
    request.setDatatype("obs")
    request.setLocationNames("KBJC")
    datatimes = DataAccessLayer.getAvailableTimes(request)
    time = datatimes[-1].validPeriod
    
    # "presWeather","skyCover","skyLayerBase"
    # are multi-dimensional... deal with these later
    request.setParameters(
        "stationName",
        "timeObs",
        "wmoId",
        "autoStationType",
        "elevation",
        "reportType",
        "temperature",
        "tempFromTenths",
        "dewpoint",
        "dpFromTenths",
        "windDir",
        "windSpeed",
        "windGust",
        "visibility",
        "altimeter",
        "seaLevelPress",
        "pressChange3Hour",
        "pressChangeChar",
        "maxTemp24Hour",
        "minTemp24Hour",
        "precip1Hour",
        "precip3Hour",
        "precip6Hour",
        "precip24Hour"
    )
    
    response = DataAccessLayer.getGeometryData(request,times=time)
    for ob in response:
        print "getParameters is",ob.getParameters()
        print len(ob.getParameters())
        #getParameters
        print ob.getString("stationName"), "from", ob.getDataTime().getRefTime()
        print "stationName is",ob.getString("stationName")
        print "timeObs is",ob.getString("timeObs")
        print "wmoId is",ob.getString("wmoId")
        print "autoStationType is",ob.getString("autoStationType")
        print "elevation is",ob.getString("elevation")
        print "reportType is",ob.getString("reportType")
        print "temperature is",ob.getString("temperature")
        print "tempFromTenths is",ob.getString("tempFromTenths")
        print "dewpoint is",ob.getString("dewpoint")
        print "dpFromTenths is",ob.getString("dpFromTenths")
        print "windDir is",ob.getString("windDir")
        print "windSpeed is",ob.getString("windSpeed")
        print "windGust is",ob.getString("windGust")
        print "visibility is",ob.getString("visibility")
        print "altimeter is",ob.getString("altimeter")
        print "seaLevelPress is",ob.getString("seaLevelPress")
        print "pressChange3Hour is",ob.getString("pressChange3Hour")
        print "pressChangeChar is",ob.getString("pressChangeChar")
        print "maxTemp24Hour is",ob.getString("maxTemp24Hour")
        print "minTemp24Hour is",ob.getString("minTemp24Hour")
        print "precip1Hour is",ob.getString("precip1Hour")
        print "precip3Hour is",ob.getString("precip3Hour")
        print "precip6Hour is",ob.getString("precip6Hour")
        print "precip24Hour is",ob.getString("precip24Hour")

.. code:: python

    # multi-dimensional present WX
    request = DataAccessLayer.newDataRequest()
    request.setDatatype("obs")
    request.setLocationNames("KBJC")
    request.setParameters("presWeather")
    response = DataAccessLayer.getGeometryData(request,times=time)
    for ob in response:
        print "getParameters is",ob.getParameters()
        print ob.getString("presWeather")
    
    
    # multi-dimensional Sky Condition
    request.setParameters("skyCover", "skyLayerBase")
    response = DataAccessLayer.getGeometryData(request,times=time)
    for ob in response:
        print ob.getString("skyCover")
        print ob.getString("skyLayerBase")

Synop/Marine
------------

.. code:: python

    from awips.dataaccess import DataAccessLayer
    
    request = DataAccessLayer.newDataRequest()
    request.setDatatype("sfcobs")
    request.setLocationNames("72421") # Covington, Kentucky (KCVG)
    
    request.setParameters("stationId","timeObs","elevation","reportType",
                      "wx_present","visibility","seaLevelPress","stationPress",
                      "pressChange3Hour","pressChangeChar","temperature",
                      "dewpoint","seaSurfaceTemp","wetBulb","windDir",
                      "windSpeed","equivWindSpeed10m","windGust","precip1Hour",
                      "precip6Hour","precip24Hour" )
    
    datatimes = DataAccessLayer.getAvailableTimes(request)
    time = datatimes[-1].validPeriod
    
    response = DataAccessLayer.getGeometryData(request,times=time)
    print response
    for ob in response:
        print "getParameters is",ob.getParameters()
        print len(ob.getParameters())


Profiler
--------

.. code:: python

    MULTI_DIM_PARAMS = set(['vComponent', 'uComponent', 'peakPower', 
                                'levelMode', 'uvQualityCode', 'consensusNum', 
                                'HorizSpStdDev', 'wComponent', 'height', 
                                'VertSpStdDev'])
    
    request = DataAccessLayer.newDataRequest("profiler")
    request.setParameters('numProfLvls', 'elevation', 'windDirSfc', 'validTime', 
                      'windSpeedSfc', 'pressure', 'submode', 'relHumidity', 
                      'profilerId', 'rainRate', 'temperature')
    request.getParameters().extend(MULTI_DIM_PARAMS)
    
    datatimes = DataAccessLayer.getAvailableTimes(request)
    time = datatimes[-1].validPeriod
    
    response = DataAccessLayer.getGeometryData(request,times=time)
    print response
    for ob in response:
        print "getParameters is",ob.getParameters()
        print len(ob.getParameters())

ACARS
-----

.. code:: python

    request = DataAccessLayer.newDataRequest("acars")
    request.setParameters("tailNumber", "receiver", "pressure", "flightPhase", 
                      "rollAngleQuality", "temp", "windDirection", "windSpeed",
                      "humidity", "mixingRatio", "icing")
    datatimes = DataAccessLayer.getAvailableTimes(request)
    time = datatimes[-1].validPeriod
    
    response = DataAccessLayer.getGeometryData(request,times=time)
    print response
    for ob in response:
        print "getParameters is",ob.getParameters()
        print len(ob.getParameters())

AIREP
-----

.. code:: python

    request = DataAccessLayer.newDataRequest("airep")
    request.setParameters("id", "flightLevel", "temp", "windDirection", "windSpeed",
                      "flightWeather", "flightHazard", "flightConditions")
    
    datatimes = DataAccessLayer.getAvailableTimes(request)
    time = datatimes[-1].validPeriod
    
    response = DataAccessLayer.getGeometryData(request,times=time)
    print response
    for ob in response:
        print "getParameters is",ob.getParameters()
        print len(ob.getParameters())

PIREP
-----

.. code:: python

    MULTI_DIM_PARAMS = set(["hazardType", 
                            "turbType", "turbBaseHeight", "turbTopHeight",
                            "iceType", "iceBaseHeight", "iceTopHeight",
                            "skyCover1", "skyCover2", "skyBaseHeight", "skyTopHeight"
                            ])
        
    request = DataAccessLayer.newDataRequest("pirep")
    request.setParameters('id', 'flightLevel', 'temp', 'windDirection', 'windSpeed',
                      'horzVisibility', 'aircraftType', 'weatherGroup')
    request.getParameters().extend(MULTI_DIM_PARAMS)
    
    datatimes = DataAccessLayer.getAvailableTimes(request)
    time = datatimes[-1].validPeriod
    
    response = DataAccessLayer.getGeometryData(request,times=time)
    print response
    for ob in response:
        print "getParameters is",ob.getParameters()
        print len(ob.getParameters())

