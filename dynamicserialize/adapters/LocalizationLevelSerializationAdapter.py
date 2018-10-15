#
# Adapter for com.raytheon.uf.common.localization.LocalizationContext$LocalizationLevel
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    01/11/11                      dgilling       Initial Creation.
#

from dynamicserialize.dstypes.com.raytheon.uf.common.localization import LocalizationLevel

ClassAdapter = [
                 'com.raytheon.uf.common.localization.LocalizationContext$LocalizationLevel',
                 'com.raytheon.uf.common.localization.LocalizationLevel'
                ]


def serialize(context, level):
    context.writeString(level.getText())
    context.writeI32(level.getOrder())
    context.writeBool(level.isSystemLevel())


def deserialize(context):
    text = context.readString()
    order = context.readI32()
    systemLevel = context.readBool()
    level = LocalizationLevel(text, order, systemLevel=systemLevel)
    return level
