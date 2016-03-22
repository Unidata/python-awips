============
Gridded Data
============
`Notebook <http://nbviewer.ipython.org/github/Unidata/python-awips/blob/master/examples/notebooks/Gridded_Data.ipynb>`_

EDEX Grid Inventory
-------------------

.. code:: python

    from awips.dataaccess import DataAccessLayer
    
    # Set host
    DataAccessLayer.changeEDEXHost("edex-cloud.unidata.ucar.edu")
    
    # Init data request
    request = DataAccessLayer.newDataRequest()
    
    # Set datatype
    request.setDatatype("grid")
    
    # Get a list of all available models
    available_grids = DataAccessLayer.getAvailableLocationNames(request)
    
    # Sort
    available_grids.sort()
    
    for grid in available_grids:
        print grid


.. parsed-literal::

    AUTOSPE
    AVN211
    AVN225
    DGEX
    ECMF-Global
    ECMF1
    ECMF10
    ECMF11
    ECMF12
    ECMF2
    ECMF3
    ECMF4
    ECMF5
    ECMF6
    ECMF7
    ECMF8
    ECMF9
    ESTOFS
    ETA
    FFG-ALR
    FFG-FWR
    FFG-KRF
    FFG-MSR
    FFG-ORN
    FFG-RHA
    FFG-RSA
    FFG-TAR
    FFG-TIR
    FFG-TUA
    GFS
    GFS40
    GFSGuide
    GFSLAMP5
    GribModel:9:151:172
    HFR-EAST_6KM
    HFR-EAST_PR_6KM
    HFR-US_EAST_DELAWARE_1KM
    HFR-US_EAST_FLORIDA_2KM
    HFR-US_EAST_NORTH_2KM
    HFR-US_EAST_SOUTH_2KM
    HFR-US_EAST_VIRGINIA_1KM
    HFR-US_HAWAII_1KM
    HFR-US_HAWAII_2KM
    HFR-US_HAWAII_6KM
    HFR-US_WEST_500M
    HFR-US_WEST_CENCAL_2KM
    HFR-US_WEST_LOSANGELES_1KM
    HFR-US_WEST_LOSOSOS_1KM
    HFR-US_WEST_NORTH_2KM
    HFR-US_WEST_SANFRAN_1KM
    HFR-US_WEST_SOCAL_2KM
    HFR-US_WEST_WASHINGTON_1KM
    HFR-WEST_6KM
    HPCGuide
    HPCqpf
    HPCqpfNDFD
    HRRR
    LAMP2p5
    MPE-Local-ORN
    MPE-Local-RHA
    MPE-Local-RSA
    MPE-Local-TAR
    MPE-Local-TIR
    MPE-Mosaic-MSR
    MPE-Mosaic-ORN
    MPE-Mosaic-RHA
    MPE-Mosaic-TAR
    MPE-Mosaic-TIR
    MRMS_1000
    NAM12
    NAM40
    NCWF
    NOHRSC-SNOW
    NamDNG
    NamDNG5
    QPE-ALR
    QPE-Auto-TUA
    QPE-FWR
    QPE-KRF
    QPE-MSR
    QPE-RFC-RSA
    QPE-RFC-STR
    QPE-TIR
    QPE-TUA
    QPE-XNAV-ALR
    QPE-XNAV-FWR
    QPE-XNAV-KRF
    QPE-XNAV-MSR
    QPE-XNAV-RHA
    QPE-XNAV-SJU
    QPE-XNAV-TAR
    QPE-XNAV-TIR
    QPE-XNAV-TUA
    RAP13
    RAP40
    RCM
    RFCqpf
    RTMA
    RTMA5
    UKMET-Global
    UKMET37
    UKMET38
    UKMET39
    UKMET40
    UKMET41
    UKMET42
    UKMET43
    UKMET44
    URMA25
    estofsPR
    fnmocWave


**LocationNames** is different for different plugins - radar is icao -
satellite is sector

Requesting a Grid
-----------------

.. code:: python

    # Grid request
    request.setLocationNames('RAP40')
    request.setParameters("RH")
    request.setLevels("850MB")
    
    # Get available times
    t = DataAccessLayer.getAvailableTimes(request)
    
    # Select last available time [-1]
    response = DataAccessLayer.getGridData(request, [t[0]])
    data = response[0]
    lon,lat = data.getLatLonCoords()
    
    # Print info
    print 'Time :', t[-1]
    print 'Model:', data.getLocationName()
    print 'Unit :', data.getUnit()
    print 'Parm :', data.getParameter()
    
    # Print data array
    print data.getRawData().shape
    print data.getRawData()
    print "lat array =", lat
    print "lon array =", lon



.. parsed-literal::

    Time : 2016-02-23 15:00:00 (12)
    Model: RAP40
    Unit : %
    Parm : RH
    (151, 113)
    [[ 93.05456543  93.05456543  87.05456543 ...,  73.05456543  72.05456543
       71.05456543]
     [ 70.05456543  70.05456543  67.05456543 ...,  69.05456543  46.05456924
       37.05456924]
     [ 40.05456924  56.05456924  68.05456543 ...,  51.05456924  73.05456543
       74.05456543]
     ..., 
     [ 65.05456543  62.05456924  63.05456924 ...,  67.05456543  65.05456543
       46.05456924]
     [ 48.05456924  59.05456924  62.05456924 ...,   4.05456877   5.05456877
        5.05456877]
     [  7.05456877   8.05456829  10.05456829 ...,  91.05456543  95.05456543
       95.05456543]]
    lat array = [[ 54.24940109  54.35071945  54.45080566 ...,  57.9545517   57.91926193
       57.88272858]
     [ 57.84495163  57.80593109  57.76566696 ...,  58.07667542  58.08861542
       58.09931183]
     [ 58.10876846  58.11697769  58.12394714 ...,  56.40270996  56.46187973
       56.51980972]
     ..., 
     [ 19.93209648  19.89832115  19.86351395 ...,  20.054636    20.06362152
       20.07156372]
     [ 20.0784626   20.08431816  20.08912849 ...,  18.58354759  18.63155174
       18.67854691]
     [ 18.72453308  18.76950836  18.81346893 ...,  17.49624634  17.42861557
       17.36001205]]
    lon array = [[-139.83120728 -139.32348633 -138.81448364 ...,  -79.26060486
       -78.70166016  -78.14326477]
     [ -77.58544922  -77.02822876  -76.47161865 ..., -100.70157623
      -100.13801575  -99.57427216]
     [ -99.01037598  -98.44634247  -97.88218689 ..., -121.69165039
      -121.15060425 -120.60871887]
     ..., 
     [ -82.65139008  -82.26644897  -81.88170624 ...,  -98.52494049
       -98.13802338  -97.75105286]
     [ -97.36403656  -96.97698212  -96.58989716 ..., -113.07767487
      -112.69831085 -112.31866455]
     [-111.93874359 -111.5585556  -111.17810822 ...,  -69.85433197
       -69.48160553  -69.10926819]]


Plotting a Grid with Basemap
----------------------------

Using **matplotlib**, **numpy**, and **basemap**:

.. code:: python

    import matplotlib.tri as mtri
    import matplotlib.pyplot as plt
    from matplotlib.transforms import offset_copy
    from mpl_toolkits.basemap import Basemap, cm
    import numpy as np
    from numpy import linspace, transpose
    from numpy import meshgrid
    
    
    plt.figure(figsize=(12, 12), dpi=100)
    lons,lats = data.getLatLonCoords()
    
    map = Basemap(projection='cyl',
          resolution = 'c',
          llcrnrlon = lons.min(), llcrnrlat = lats.min(),
          urcrnrlon =lons.max(), urcrnrlat = lats.max()
    )
    map.drawcoastlines()
    map.drawstates()
    map.drawcountries()
    
    # 
    # We have to reproject our grid, see https://stackoverflow.com/questions/31822553/m
    #
    x = linspace(0, map.urcrnrx, data.getRawData().shape[1])
    y = linspace(0, map.urcrnry, data.getRawData().shape[0])
    xx, yy = meshgrid(x, y)
    ngrid = len(x)
    rlons = np.repeat(np.linspace(np.min(lons), np.max(lons), ngrid),
              ngrid).reshape(ngrid, ngrid)
    rlats = np.repeat(np.linspace(np.min(lats), np.max(lats), ngrid),
              ngrid).reshape(ngrid, ngrid).T
    tli = mtri.LinearTriInterpolator(mtri.Triangulation(lons.flatten(),
              lats.flatten()), data.getRawData().flatten())
    rdata = tli(rlons, rlats)
    cs = map.contourf(rlons, rlats, rdata, latlon=True, vmin=0, vmax=100, cmap='YlGn')
    
    # add colorbar.
    cbar = map.colorbar(cs,location='bottom',pad="5%")
    cbar.set_label(data.getParameter() + data.getUnit() )
    
    # Show plot
    plt.show()




.. image:: Gridded_Data_files/Gridded_Data_5_0.png


or use **pcolormesh** rather than **contourf**

.. code:: python

    plt.figure(figsize=(12, 12), dpi=100)
    map = Basemap(projection='cyl',
          resolution = 'c',
          llcrnrlon = lons.min(), llcrnrlat = lats.min(),
          urcrnrlon =lons.max(), urcrnrlat = lats.max()
    )
    map.drawcoastlines()
    map.drawstates()
    map.drawcountries()
    cs = map.pcolormesh(rlons, rlats, rdata, latlon=True, vmin=0, vmax=100, cmap='YlGn')



.. image:: Gridded_Data_files/Gridded_Data_7_0.png


Plotting a Grid with Cartopy
----------------------------

.. code:: python

    import os
    import matplotlib.pyplot as plt
    import numpy as np
    import iris
    import cartopy.crs as ccrs
    from cartopy import config
    
    lon,lat = data.getLatLonCoords()
    plt.figure(figsize=(12, 12), dpi=100)
    ax = plt.axes(projection=ccrs.PlateCarree())
    cs = plt.contourf(rlons, rlats, rdata, 60, transform=ccrs.PlateCarree(), vmin=0, vmax=100, cmap='YlGn')
    ax.coastlines()
    ax.gridlines()
    
    # add colorbar
    cbar = plt.colorbar(orientation='horizontal')
    cbar.set_label(data.getParameter() + data.getUnit() )
    plt.show()



.. image:: Gridded_Data_files/Gridded_Data_9_0.png


