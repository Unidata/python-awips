#
# Adapter for com.raytheon.uf.common.localization.LocalizationContext$LocalizationType
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    01/11/11                      dgilling       Initial Creation.
#

from dynamicserialize.dstypes.com.raytheon.uf.common.localization import LocalizationType

ClassAdapter = [
                'com.raytheon.uf.common.localization.LocalizationContext$LocalizationType',
                'com.raytheon.uf.common.localization.LocalizationType'
                ]


def serialize(context, ltype):
    context.writeString(ltype.getText())


def deserialize(context):
    typeString = context.readString()
    return LocalizationType(typeString)
