#
# Adapter for java.awt.Point
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    08/31/10                      njensen       Initial Creation.
#

from dynamicserialize.dstypes.java.awt import Point

ClassAdapter = 'java.awt.Point'


def serialize(context, point):
    context.writeI32(point.getX())
    context.writeI32(point.getY())


def deserialize(context):
    x = context.readI32()
    y = context.readI32()
    point = Point()
    point.setX(x)
    point.setY(y)
    return point
