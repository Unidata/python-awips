#!/awips2/python/bin/python
from ufpy.dataaccess import DataAccessLayer


# set everything up
DataAccessLayer.changeEDEXHost("edex.unidata.ucar.edu")
request = DataAccessLayer.newDataRequest()

# set grid 
request.setDatatype("grid")
available_grids = DataAccessLayer.getAvailableLocationNames(request)
for grid in available_grids:
    print grid

exit()	



# set uair
request.setDatatype("bufrua")
# set parameters
request.setParameters("tpMan","tdMan","prMan","htMan","wdMan","wsMan")


locations = DataAccessLayer.getAvailableLocationNames(request)
#print locations

request.setLocationNames("72230")

datatimes = DataAccessLayer.getAvailableTimes(request)
#print datatimes[0].validPeriod

response = DataAccessLayer.getGeometryData(request,times=datatimes[-1].validPeriod)
#print response

for ob in response:
	print "Pres is",ob.getString("prMan")
	print "   KBMX observation from %s" %ob.getDataTime().getRefTime()
	print "   Temperature is",ob.getString("tpMan")
	print "   Dewpoint is",ob.getString("tdMan")
	print "   Height is",ob.getString("htMan")
	print "   Wind dir is",ob.getString("wdMan")
	print "   Wind speed is",ob.getString("wsMan")

