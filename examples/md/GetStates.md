```python
#!python
#!/awips2/python/bin/python
from awips.dataaccess import DataAccessLayer

#Initiate a new DataRequest
b = DataAccessLayer.newDataRequest()
#Set the datatype to maps so it knows what plugin to route the request too
b.setDatatype("maps")
#setParameters indicates the columns from table that we want returned along with our geometry
b.setParameters("state","fips")
#Add a couple of identifiers to indicate the geomField and table we are querying
b.addIdentifier("geomField","the_geom")
b.addIdentifier("table","mapdata.states")

#getAvailableLocationNames method will return a list of all available locations
#based off the table we have specified previously. LocationNames mean different
#things to different plugins beware...radar is icao, satellite is sector, etc
a = DataAccessLayer.getAvailableLocationNames(b)
print a

#Use setLocationNames to set the states we want data from
b.setLocationNames("Oklahoma","Texas","Kansas")

#Finally lets request some data. There are two types of data (Grid, Geometry) here we are
#requesting geometry data and therefore use the getGeometryData method. We pass it our DataRequest object
#that has all of our parameters and None for the DataTime object argument since maps are time agnostic
#This returns a list of awips.dataaccess.PyGeometryData.PyGeometryData objects.
c = DataAccessLayer.getGeometryData(b, None)
print c

#Now lets loop through our list of PyGeometryData objects of states and look at some data
for shape in c:
    #Lets print the locationname for this object
    print 'Location name is',shape.getLocationName()
    #getGeometry returns a shapely geometry object for this state. Using shapely allows
    #us to perform postgis type operations outside the database (contains,within,etc). If
    #not familiar with shapely recommend you look at the documentation available online.
    #This is a 3rd party python module so just Google search python shapely to find the docs
    mpoly = shape.getGeometry()
    #These next few items allow us to access the column data we requested when we set the
    #parameters
    print 'Parameters requested are',shape.getParameters()
    print 'state column is',shape.getString('state')
    print 'fips column is',shape.getString('fips')
```

```python
['Alabama', 'Alaska', 'American Samoa', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Guam', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Puerto Rico', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virgin Islands', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
```

```python
[<awips.dataaccess.PyGeometryData.PyGeometryData object at 0x1ec4410>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x1ec4510>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x1ec4550>]
```

```python
Location name is Texas
Parameters requested are ['state', 'fips']
state column is TX
fips column is 48
Location name is Kansas
Parameters requested are ['state', 'fips']
state column is KS
fips column is 20
Location name is Oklahoma
Parameters requested are ['state', 'fips']
state column is OK
fips column is 40
```
