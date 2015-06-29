
n
#!/awips2/python/bin/python
from ufpy.dataaccess import DataAccessLayer
import numpy as np

request = DataAccessLayer.newDataRequest()
request.setDatatype("satellite")
request.setLocationNames("East CONUS")
request.setParameters("Imager 6.7-6.5 micron IR (WV)")

t = DataAccessLayer.getAvailableTimes(request)
print t[-1].getRefTime()

response = DataAccessLayer.getGridData(request, times=[t[-1]])
print response
data = response[0]

print 'Units are in', data.getUnit()
lon,lat = data.getLatLonCoords()

print 'Parameter we requested is',data.getParameter()
print data.getRawData()
```

```
May 04 15 18:45:19 GMT
```

```
[<ufpy.dataaccess.PyGridData.PyGridData object at 0x157d550>]
```

```
Units are in None
```

```
Parameter we requested is Imager 6.7-6.5 micron IR (WV)
```

```
[[ 186.  185.  186. ...,  180.  181.  181.]
 [ 186.  185.  186. ...,  180.  181.  181.]
 [ 186.  186.  185. ...,  180.  181.  181.]
 ..., 
 [   0.    0.    0. ...,  145.  145.  145.]
 [   0.    0.    0. ...,  145.  145.  145.]
 [   0.    0.    0. ...,  145.  145.  144.]]
```
