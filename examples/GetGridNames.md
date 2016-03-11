#### Using the DAF to get all of the available grids

```python
#!python
from awips.dataaccess import DataAccessLayer

#Initiate a new DataRequest
request = DataAccessLayer.newDataRequest()

#Set the datatype to grid so it knows what plugin to route the request too
request.setDatatype("grid")

#getAvailableLocationNames method will return a list of all available models
#LocationNames mean different things to different plugins beware...radar is icao,
#satellite is sector, etc
available_grids = DataAccessLayer.getAvailableLocationNames(request)
for grid in available_grids:
    print grid
```

And the output of the print grid statement would look something like this:

```python
RUC236
SREF216
ENSEMBLE
RTOFS-WestAtl
AKwave10
HiResW-NMM-AK
QPE-KRF
AK-NamDNG5
GFS160
FFG-TIR
GFS254
SPCGuide
RFCqpf
RTMA-Mosaic
QPE-RFC-RSA
UKMET40
MPE-Local-MSR
gefs
WNAwave4
GFS201
QPE-XNAV-ALR
AK-RTMA3
GFS212
...
```
