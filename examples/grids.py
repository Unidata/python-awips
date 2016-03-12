#!python
from awips.dataaccess import DataAccessLayer

# Set host
DataAccessLayer.changeEDEXHost("edex-cloud.unidata.ucar.edu")

# Init data request
request = DataAccessLayer.newDataRequest()

# Set datatype
request.setDatatype("grid")

#
# getAvailableLocationNames method will return a list of all available models
#
# LocationNames mean different things to different plugins beware...radar is icao,
# satellite is sector, etc
#
available_grids = DataAccessLayer.getAvailableLocationNames(request)
for grid in available_grids:
    print grid
