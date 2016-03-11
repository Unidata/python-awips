```python
#!python
import numpy as np
from awips.dataaccess import DataAccessLayer

#Initiate a new DataRequest
request = DataAccessLayer.newDataRequest()
#Set the datatype to grid so it knows what plugin to route the request too
request.setDatatype("grid")

#Use setLocationNames to set the model we want data from
request.setLocationNames('RUC130')
#Next we set the variable and level of data we want
request.setParameters("T")
request.setLevels("850MB")

#getAvailableTimes allows us to query what times are available based off of the
#model, parameter, and levels we have previously identified. These are of the type
#dynamicserialize.dstypes.com.raytheon.uf.common.time.DataTime.DataTime.
t = DataAccessLayer.getAvailableTimes(request)

#Finally lets request some data. There are two types of data (Grid, Geometry) here we are
#requesting gridded data and therefore use the getGridData method. We pass it our DataRequest object 
#that has all of our model, parameter, and level information and also a list of DataTime objects we want
#the data for. In this case just give us the data from the last DataTime in the above list (t[-1]). This returns 
#a list of awips.dataaccess.PyGridData.PyGridData objects.
response = DataAccessLayer.getGridData(request, [t[-1]])
print response

#Since we only asked for one DataTime we only have one PyGridData object. Lets pull this out
#into a variable named data. Then we can use functions available from awips.dataaccess.PyGridData.PyGridData
#objects (see module for more methods or details)
data = response[0]

#Show the units of the data
print 'Units are in', data.getUnit()

#Get LatLon coords of the gridded data, Returns a tuple <lon,lat> arrays
lon,lat = data.getLatLonCoords()
print lon

#In case we forget what we requested we can get the parameter
print 'Parameter we requested is', data.getParameter()
#And finally lets get the data itself. This returns an array of the raw data
print data.getRawData()
```

Our response object is a list of !PyGridData objects
```python

[<awips.dataaccess.PyGridData.PyGridData object at 0x1d39910>]
```

Output of our print statement getting the units
```python
Units are in K
```

print lon
```python
[[-118.09392548 -117.93661499 -117.77923584 ...,  -90.46847534
   -90.30672455  -90.14498901]
 [-118.06690216 -117.90976715 -117.75257111 ...,  -90.47387695
   -90.31232452  -90.15077972]
 [-118.03994751 -117.88298798 -117.72595978 ...,  -90.47927094
   -90.31790161  -90.15655518]
 ..., 
 [-114.21573639 -114.08406067 -113.9523468  ...,  -91.24035645
   -91.10612488  -90.97190094]
 [-114.19696808 -114.06542206 -113.93383026 ...,  -91.24407959
   -91.10997772  -90.97589111]
 [-114.17823792 -114.04681396 -113.91535187 ...,  -91.24778748
   -91.11382294  -90.97986603]]
```

Our print statement from getParameter()
```python
Parameter we requested is T
```

And finally our call to getRawData() gets a numpy array of the temperature values
```python
[[ 283.88305664  284.50805664  285.25805664 ...,  280.88305664
   280.75805664  280.63305664]
 [ 284.38305664  285.00805664  285.75805664 ...,  281.00805664
   280.88305664  280.75805664]
 [ 284.50805664  285.13305664  285.75805664 ...,  281.13305664
   281.00805664  280.88305664]
 ..., 
 [ 285.38305664  285.63305664  285.88305664 ...,  286.88305664
   286.88305664  287.00805664]
 [ 285.25805664  285.50805664  285.75805664 ...,  287.00805664
   287.00805664  287.13305664]
 [ 285.13305664  285.50805664  285.75805664 ...,  287.25805664
   287.25805664  287.25805664]]
```

