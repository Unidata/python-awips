```python
#!python
from ufpy.dataaccess import DataAccessLayer
import numpy as np

request = DataAccessLayer.newDataRequest()
request.setDatatype("gfe")

# For GFE our locationNames are tied to the activated sites in GFE
locationNames = DataAccessLayer.getAvailableLocationNames(request)
print locationNames

request.setLocationNames('OUN')
# For GFE data we use the addIdentifier method to add a constraint.
# Our constraint is for the modelName attribute and this determines
# which GFE database to query the data from. In this request we will
# query the Official database.
request.addIdentifier('modelName','Official')
request.setParameters('PoP')

t = DataAccessLayer.getAvailableTimes(request)
for each in t:
    print each.getRefTime(),each.getValidPeriod()
    
response = DataAccessLayer.getGridData(request, [t[0]])
print response
data = response[0]

print 'Units are in', data.getUnit()

lon,lat = data.getLatLonCoords()
print lon

print 'Parameter we requested is',data.getParameter()

print data.getRawData()

```

```python
['OUN']
```

```python
May 03 15 18:00:00 GMT (May 03 15 18:00:00 , May 03 15 21:00:00 )
May 03 15 21:00:00 GMT (May 03 15 21:00:00 , May 04 15 00:00:00 )
May 04 15 00:00:00 GMT (May 04 15 00:00:00 , May 04 15 08:00:00 )
May 04 15 08:00:00 GMT (May 04 15 08:00:00 , May 04 15 12:00:00 )
May 04 15 12:00:00 GMT (May 04 15 12:00:00 , May 04 15 18:00:00 )
May 04 15 18:00:00 GMT (May 04 15 18:00:00 , May 05 15 00:00:00 )
May 05 15 00:00:00 GMT (May 05 15 00:00:00 , May 05 15 06:00:00 )
May 05 15 06:00:00 GMT (May 05 15 06:00:00 , May 05 15 12:00:00 )
May 05 15 12:00:00 GMT (May 05 15 12:00:00 , May 05 15 18:00:00 )
May 05 15 18:00:00 GMT (May 05 15 18:00:00 , May 06 15 00:00:00 )
May 06 15 00:00:00 GMT (May 06 15 00:00:00 , May 06 15 12:00:00 )
May 06 15 12:00:00 GMT (May 06 15 12:00:00 , May 06 15 18:00:00 )
May 06 15 18:00:00 GMT (May 06 15 18:00:00 , May 07 15 00:00:00 )
May 07 15 00:00:00 GMT (May 07 15 00:00:00 , May 07 15 12:00:00 )
May 07 15 12:00:00 GMT (May 07 15 12:00:00 , May 08 15 00:00:00 )
May 08 15 00:00:00 GMT (May 08 15 00:00:00 , May 08 15 12:00:00 )
May 08 15 12:00:00 GMT (May 08 15 12:00:00 , May 09 15 00:00:00 )
May 09 15 00:00:00 GMT (May 09 15 00:00:00 , May 09 15 12:00:00 )
May 09 15 12:00:00 GMT (May 09 15 12:00:00 , May 10 15 00:00:00 )
May 10 15 00:00:00 GMT (May 10 15 00:00:00 , May 10 15 12:00:00 )
May 10 15 12:00:00 GMT (May 10 15 12:00:00 , May 11 15 00:00:00 )
May 11 15 00:00:00 GMT (May 11 15 00:00:00 , May 11 15 12:00:00 )
May 11 15 12:00:00 GMT (May 11 15 12:00:00 , May 12 15 00:00:00 )
May 12 15 00:00:00 GMT (May 12 15 00:00:00 , May 12 15 12:00:00 )
May 12 15 12:00:00 GMT (May 12 15 12:00:00 , May 12 15 13:00:00 )
```

```python
[<ufpy.dataaccess.PyGridData.PyGridData object at 0x26f9690>]
```

```python
Units are in %
```

```python
[[-101.30716705 -101.27905273 -101.25093842 ...,  -95.05664062
   -95.02846527  -95.00028992]
 [-101.3058548  -101.27774811 -101.24964142 ...,  -95.056633    -95.02845764
   -95.00028992]
 [-101.30455017 -101.27644348 -101.24834442 ...,  -95.05661774
   -95.02845764  -95.00028992]
 ..., 
 [-101.02937317 -101.00249481 -100.97560883 ...,  -95.05414581
   -95.02721405  -95.00027466]
 [-101.02817535 -101.001297   -100.97442627 ...,  -95.05413055
   -95.02720642  -95.00027466]
 [-101.02697754 -101.00010681 -100.97324371 ...,  -95.05412292
   -95.02719879  -95.00027466]]
```

```python
Parameter we requested is PoP
```

```python
[[ 8.  8.  7. ...,  7.  7.  7.]
 [ 8.  7.  7. ...,  7.  7.  7.]
 [ 7.  7.  7. ...,  7.  7.  7.]
 ..., 
 [ 3.  3.  3. ...,  2.  2.  2.]
 [ 3.  3.  3. ...,  2.  2.  2.]
 [ 3.  3.  3. ...,  2.  2.  2.]]
```
