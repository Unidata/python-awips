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


.. parsed-literal::

    getParameters is ['precip1Hour', 'tempFromTenths', 'precip24Hour', 'seaLevelPress', 'pressChange3Hour', 'temperature', 'dpFromTenths', 'reportType', 'pressChangeChar', 'elevation', 'precip3Hour', 'dewpoint', 'visibility', 'timeObs', 'maxTemp24Hour', 'stationName', 'altimeter', 'autoStationType', 'wmoId', 'windDir', 'windSpeed', 'minTemp24Hour', 'windGust', 'precip6Hour']
    24
    KBJC from Mar 15 16 22:46:00 GMT
    stationName is KBJC
    timeObs is 1458081960000
    wmoId is -9999
    autoStationType is 
    elevation is 1729.0
    reportType is METAR
    temperature is 7.0
    tempFromTenths is -9999.0
    dewpoint is -12.0
    dpFromTenths is -9999.0
    windDir is 230.0
    windSpeed is 15.0
    windGust is 25.0
    visibility is 60.0
    altimeter is 29.9599990845
    seaLevelPress is -9999.0
    pressChange3Hour is -9999.0
    pressChangeChar is 
    maxTemp24Hour is -9999.0
    minTemp24Hour is -9999.0
    precip1Hour is -9999.0
    precip3Hour is -9999.0
    precip6Hour is -9999.0
    precip24Hour is -9999.0


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


.. parsed-literal::

    getParameters is ['presWeather']
    VCSH
    getParameters is ['presWeather']
    
    getParameters is ['presWeather']
    
    getParameters is ['presWeather']
    
    getParameters is ['presWeather']
    
    FEW
    8000.0
    SCT
    12000.0
    BKN
    20000.0
    
    -9999.0
    
    -9999.0
    
    -9999.0


Synop/Marine
------------

.. code:: python

    from awips.dataaccess import DataAccessLayer
    
    DataAccessLayer.changeEDEXHost("edex-cloud.unidata.ucar.edu")
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



.. parsed-literal::

    [<awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b404f3310>]
    getParameters is ['windDir', 'pressChange3Hour', 'elevation', 'temperature', 'wetBulb', 'wx_present', 'stationPress', 'visibility', 'dewpoint', 'stationId', 'precip1Hour', 'equivWindSpeed10m', 'windSpeed', 'pressChangeChar', 'windGust', 'timeObs', 'reportType', 'precip6Hour', 'precip24Hour', 'seaSurfaceTemp', 'seaLevelPress']
    21


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


.. parsed-literal::

    [<awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b4481b390>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b40510ad0>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b279852d0>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b27985310>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b279853d0>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b27985410>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b27985450>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b27985490>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b279854d0>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b27985510>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b27985550>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b27985590>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b279855d0>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b27985610>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b27985650>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b27985690>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b279856d0>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b27985710>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b27985750>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b27985790>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b279857d0>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b27985810>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b27985850>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b27985890>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b279858d0>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b27985910>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b27985950>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b27985990>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b279859d0>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b27985a10>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b27985a50>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b27985a90>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b3018ab50>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b4053b6d0>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b27985ad0>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b27985b10>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b27985b50>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b27985b90>]
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['numProfLvls', 'elevation', 'windDirSfc', 'validTime', 'windSpeedSfc', 'pressure', 'submode', 'relHumidity', 'profilerId', 'rainRate', 'temperature']
    11
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['vComponent', 'uComponent', 'peakPower', 'levelMode', 'uvQualityCode', 'consensusNum', 'HorizSpStdDev', 'wComponent', 'height', 'VertSpStdDev']
    10
    getParameters is ['numProfLvls', 'elevation', 'windDirSfc', 'validTime', 'windSpeedSfc', 'pressure', 'submode', 'relHumidity', 'profilerId', 'rainRate', 'temperature']
    11


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


.. parsed-literal::

    [<awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b30196dd0>]
    getParameters is ['flightPhase', 'icing', 'temp', 'humidity', 'pressure', 'windSpeed', 'receiver', 'mixingRatio', 'windDirection', 'rollAngleQuality', 'tailNumber']
    11


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


.. parsed-literal::

    [<awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b3044f6d0>]
    getParameters is ['flightWeather', 'flightHazard', 'flightConditions', 'windSpeed', 'flightLevel', 'id']
    6


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


.. parsed-literal::

    [<awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b301a2210>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x7f1b301a2510>]
    getParameters is ['skyTopHeight', 'skyBaseHeight', 'turbTopHeight', 'iceBaseHeight', 'skyCover1', 'turbBaseHeight', 'iceType', 'iceTopHeight', 'turbType', 'hazardType', 'skyCover2']
    11
    getParameters is ['horzVisibility', 'weatherGroup', 'windSpeed', 'aircraftType', 'flightLevel', 'id']
    6


