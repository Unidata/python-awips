#### Below shows an example of only requesting data over a specific envelope (ie bounding box). This examples uses a request from the maps database to get the Envelope around the CWA of OUN for our request. This can be used to fine tune your request to only get the data you really need and speed up requests.

#### You could do this same type of request using any other geometry. For example, you could query the states table and only pull out model data over a particular state. You can also create your own Shapely geometry from scratch and use it to define your envelope.

```
#!python
#!/awips2/python/bin/python
from ufpy.dataaccess import DataAccessLayer
import numpy as np

# First we will request the OUN CWA from the maps database.
# We will use this to create the envelope for our grid request.
request = DataAccessLayer.newDataRequest()
request.setDatatype("maps")
request.setParameters("cwa","wfo")
request.addIdentifier("locationField","wfo")
request.addIdentifier("geomField","the_geom")
request.addIdentifier("table","mapdata.cwa")
request.setLocationNames("OUN")
response = DataAccessLayer.getGeometryData(request, None)
oungeom = response[0].getGeometry()

# First let's get the nonclipped 850MB Temp so we can compare
# the lat/lons and shape of the arrays
request = DataAccessLayer.newDataRequest()
request.setDatatype("grid")
request.setLocationNames('RUC130')
request.setParameters("T")
request.setLevels("850MB")
t = DataAccessLayer.getAvailableTimes(request)
response = DataAccessLayer.getGridData(request, times=[t[-1]])
data = response[0]
coords = data.getLatLonCoords()
print coords[0].shape,coords[1].shape

# Since the only thing we are changing is adding an Envelope
# we can reuse our previous request without having to make a
# new one.
# Now we will request only the grid points that are within the envelope (bbox)
# of the OUN cwa by using the setEnvelope method
print 'OUN Envelope is',oungeom.envelope
request.setEnvelope(oungeom)
response = DataAccessLayer.getGridData(request, times=[t[-1]])
data = response[0]
coords = data.getLatLonCoords()
print coords[0].shape,coords[1].shape

# Let's say we want to get an area a little bit larger than our CWA. For this we can use
# Shapely's buffer method to enlarge our envelope. In this example we will buffer the OUN
# geometry by half a degree.
ounbufferedgeom = oungeom.buffer(0.5)
print 'OUN Envelope with buffer is',ounbufferedgeom.envelope
request.setEnvelope(ounbufferedgeom)
response = DataAccessLayer.getGridData(request, times=[t[-1]])
data = response[0]
coords = data.getLatLonCoords()
print coords[0].shape,coords[1].shape
```

```
(175, 175) (175, 175)
```

```
OUN Envelope is POLYGON ((-100.0485000609999702 33.3954124450000336, -95.6716995239999619 33.3954124450000336, -95.6716995239999619 37.0016136170000323, -100.0485000609999702 37.0016136170000323, -100.0485000609999702 33.3954124450000336))
```

```
(32, 33) (32, 33)
```

```
OUN Envelope with buffer is POLYGON ((-100.5485000609999702 32.8954672430463262, -95.1716995239999619 32.8954672430463262, -95.1716995239999619 37.5016136170000323, -100.5485000609999702 37.5016136170000323, -100.5485000609999702 32.8954672430463262))
```

```
(39, 41) (39, 41)
```
