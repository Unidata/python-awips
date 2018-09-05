```python
#!python
from awips.dataaccess import DataAccessLayer
from shapely.geometry import Polygon,Point
from datetime import datetime

#Initiate a new DataRequest
#Get all of the states from the database
print "Requesting all states from DAF"
t1=datetime.utcnow()
request = DataAccessLayer.newDataRequest()
request.setDatatype("maps")
request.addIdentifier("geomField","the_geom")
request.addIdentifier("table","mapdata.states")
request.setParameters("state","fips","name")
states = DataAccessLayer.getGeometryData(request, None)
t2=datetime.utcnow()
tdelta = t2-t1
print 'DAF query to get all states took %i.%i seconds' %(tdelta.seconds,tdelta.microseconds)

#Create a polygon object...for example this is a polygon around Oklahoma City
polygon = Polygon([(-97.82,35.63),(-97.21,35.63),(-97.21,35.15),(-97.82,35.15),(-97.82,35.63)])
#Now lets filter the states down to the one that contains the above polygon
#We will use the python built in filter method to accomplish this
#the expression below goes through each state object, gets it's geometry, and calls
#it's contains method. It in essence creates a new list, state_contain_polygon, with
#only the states where the contains method evaluates to true.
t1=datetime.utcnow()
state_contain_polygon = filter(lambda state: state.getGeometry().contains(polygon),states)
t2= datetime.utcnow()
tdelta = t2-t1
print '\nFilter state objects to one that contains polygon took %i.%i seconds' %(tdelta.seconds,tdelta.microseconds)
print state_contain_polygon
print "Polygon is in the state of",state_contain_polygon[0].getString('name')

#Lets also create a point object...this one is located in the state of Iowa
point = Point(-93.62,41.60)
#Now lets see what state our point is in
t1=datetime.utcnow()
state_contain_point = filter(lambda state: state.getGeometry().contains(point),states)
t2= datetime.utcnow()
tdelta = t2-t1
print '\nFilter state objects to one that contains point took %i.%i seconds ' %(tdelta.seconds,tdelta.microseconds)
print state_contain_point
print "Point is in the state of",state_contain_point[0].getString('name')

#One last example...this time for an intersection. Lets find all of the states this polygon intersects
#This polygon is the same as above just extended it further south to 33.15 degrees
polygon2 = Polygon([(-97.82,35.63),(-97.21,35.63),(-97.21,33.15),(-97.82,33.15),(-97.82,35.63)])
t1=datetime.utcnow()
state_intersect_polygon = filter(lambda state: state.getGeometry().intersects(polygon2),states)
t2= datetime.utcnow()
tdelta = t2-t1
print '\nFilter state objects to the ones that intersect polygon took %i.%i seconds ' %(tdelta.seconds,tdelta.microseconds)
print state_intersect_polygon
for state in state_intersect_polygon:
    print "Polygon intersects the state of",state.getString('name')
```

```python
Requesting all states from DAF
DAF query to get all states took 21.915029 seconds
```

```python
Filter state objects to one that contains polygon took 0.382097 seconds
[<awips.dataaccess.PyGeometryData.PyGeometryData object at 0x2bebdd0>]
Polygon is in the state of Oklahoma
```

```python
Filter state objects to one that contains point took 0.2028 seconds
[<awips.dataaccess.PyGeometryData.PyGeometryData object at 0x2beb9d0>]
Point is in the state of Iowa
```

```python
Filter state objects to the ones that intersect polygon took 0.4032 seconds
[<awips.dataaccess.PyGeometryData.PyGeometryData object at 0x2beb610>, <awips.dataaccess.PyGeometryData.PyGeometryData object at 0x2bebdd0>]
Polygon intersects the state of Texas
Polygon intersects the state of Oklahoma
```
