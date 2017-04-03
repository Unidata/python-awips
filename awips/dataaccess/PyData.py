##
##

#
# Implements IData for use by native Python clients to the Data Access
# Framework.
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    06/03/13                      dgilling      Initial Creation.
#
#

from awips.dataaccess import IData

class PyData(IData):

    def __init__(self, dataRecord):
        self.__time = dataRecord.getTime()
        self.__level = dataRecord.getLevel()
        self.__locationName = dataRecord.getLocationName()
        self.__attributes = dataRecord.getAttributes()

    def getAttribute(self, key):
        return self.__attributes[key]

    def getAttributes(self):
        return list(self.__attributes.keys())

    def getDataTime(self):
        return self.__time

    def getLevel(self):
        return self.__level

    def getLocationName(self):
        return self.__locationName
