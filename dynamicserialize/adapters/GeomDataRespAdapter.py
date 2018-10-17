#
#    Efficient adapter for GetGeometryDataResponse
#
#
#    SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    Oct 17, 2016     5919         njensen        Initial creation
#
#
#

from dynamicserialize.dstypes.com.raytheon.uf.common.dataaccess.response import GeometryResponseData
from dynamicserialize.dstypes.com.raytheon.uf.common.dataaccess.response import GetGeometryDataResponse

ClassAdapter = 'com.raytheon.uf.common.dataaccess.response.GetGeometryDataResponse'


def serialize(context, resp):
    wkbs = resp.getGeometryWKBs()
    # write list size
    context.writeI32(len(wkbs))
    # write byte arrays
    for b in wkbs:
        context.writeBinary(b)

    geoData = resp.getGeoData()
    # write list size
    context.writeI32(len(geoData))
    # write objects
    for geo in geoData:
        context.writeI32(geo.getGeometryWKBindex())
        context.writeObject(geo.getTime())
        context.writeObject(geo.getLevel())
        context.writeObject(geo.getLocationName())
        context.writeObject(geo.getAttributes())

        # write data map
        params = geo.getDataMap()
        context.writeI32(len(params))
        for p in params:
            context.writeString(p)
            value = params[p]
            # actual value
            context.writeObject(value[0])
            # value type as string
            context.writeString(str(value[1]))
            # unit
            context.writeObject(value[2])


def deserialize(context):
    size = context.readI32()
    wkbs = []
    for __ in range(size):
        wkb = context.readBinary()
        wkbs.append(wkb)

    geoData = []
    size = context.readI32()
    for _ in range(size):
        data = GeometryResponseData()
        # wkb index
        wkbIndex = context.readI32()
        data.setGeometryWKBindex(wkbIndex)

        time = context.readObject()
        data.setTime(time)
        level = context.readObject()
        data.setLevel(level)
        locName = context.readObject()
        data.setLocationName(locName)
        attrs = context.readObject()
        data.setAttributes(attrs)

        # parameters
        paramSize = context.readI32()
        paramMap = {}
        for __ in range(paramSize):
            paramName = context.readString()
            value = context.readObject()
            tName = context.readString()
            unit = context.readObject()
            paramMap[paramName] = [value, tName, unit]
        data.setDataMap(paramMap)
        geoData.append(data)

    # make the response object
    resp = GetGeometryDataResponse()
    resp.setGeometryWKBs(wkbs)
    resp.setGeoData(geoData)

    return resp
