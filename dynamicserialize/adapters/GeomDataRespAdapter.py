##
# This software was developed and / or modified by Raytheon Company,
# pursuant to Contract DG133W-05-CQ-1067 with the US Government.
#
# U.S. EXPORT CONTROLLED TECHNICAL DATA
# This software product contains export-restricted data whose
# export/transfer/disclosure is restricted by U.S. law. Dissemination
# to non-U.S. persons whether in the United States or abroad requires
# an export license or other authorization.
#
# Contractor Name:        Raytheon Company
# Contractor Address:     6825 Pine Street, Suite 340
#                         Mail Stop B8
#                         Omaha, NE 68106
#                         402.291.0100
#
# See the AWIPS II Master Rights File ("Master Rights File.pdf") for
# further licensing information.
##


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

from thrift.Thrift import TType
from dynamicserialize import SelfDescribingBinaryProtocol
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
    for i in range(size):
        wkb = context.readBinary()
        wkbs.append(wkb)

    geoData = []
    size = context.readI32()
    for i in range(size):
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
        for k in range(paramSize):
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
