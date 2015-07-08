#!/awips2/python/bin/python
from ufpy.dataaccess import DataAccessLayer

request = DataAccessLayer.newDataRequest()
request.setDatatype("bufrua")
#request.setParameters("temperature","dewpoint")
request.setParameters("prMan","htMan")


locations = DataAccessLayer.getAvailableLocationNames(request)
print locations

request.setLocationNames("72230")

datatimes = DataAccessLayer.getAvailableTimes(request)
print datatimes[-1].validPeriod

response = DataAccessLayer.getGeometryData(request,times=datatimes[-1].validPeriod)
print response

ob = response[0]
print "KBMX observation from %s" %ob.getDataTime().getRefTime()
print "Temperature is",ob.getString("temperature")
print "Dewpoint is",ob.getString("dewpoint")
