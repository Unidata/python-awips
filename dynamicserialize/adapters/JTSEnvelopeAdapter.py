#
# Adapter for com.vividsolutions.jts.geom.Envelope
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    05/29/13         2023         dgilling       Initial Creation.
#

from dynamicserialize.dstypes.com.vividsolutions.jts.geom import Envelope

ClassAdapter = 'com.vividsolutions.jts.geom.Envelope'


def serialize(context, envelope):
    context.writeDouble(envelope.getMinX())
    context.writeDouble(envelope.getMaxX())
    context.writeDouble(envelope.getMinY())
    context.writeDouble(envelope.getMaxY())


def deserialize(context):
    env = Envelope()
    env.setMinX(context.readDouble())
    env.setMaxX(context.readDouble())
    env.setMinY(context.readDouble())
    env.setMaxY(context.readDouble())
    return env
