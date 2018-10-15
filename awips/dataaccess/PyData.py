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
#    10/05/18                      mjames@ucar   Encode/decode attribute names.
#
#

from awips.dataaccess import IData
import six


class PyData(IData):

    def __init__(self, dataRecord):
        self.__time = dataRecord.getTime()
        self.__level = dataRecord.getLevel()
        self.__locationName = dataRecord.getLocationName()
        self.__attributes = dataRecord.getAttributes()

    def getAttribute(self, key):
        return self.__attributes[key]

    def getAttributes(self):
        return self.__attributes.keys()

    def getDataTime(self):
        return self.__time

    def getLevel(self):
        if six.PY2:
            return self.__level
        if not isinstance(self.__level, str):
            return self.__level.decode('utf-8')
        return self.__level

    def getLocationName(self):
        return self.__locationName
