#
# Adapter for com.vividsolutions.jts.geom.Coordinate
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    01/20/11                      dgilling      Initial Creation.
#

from dynamicserialize.dstypes.com.vividsolutions.jts.geom import Coordinate

ClassAdapter = 'com.vividsolutions.jts.geom.Coordinate'


def serialize(context, coordinate):
    context.writeDouble(coordinate.getX())
    context.writeDouble(coordinate.getY())


def deserialize(context):
    x = context.readDouble()
    y = context.readDouble()
    coord = Coordinate()
    coord.setX(x)
    coord.setY(y)
    return coord
