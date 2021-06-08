#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    05/29/13         2023         dgilling       Initial Creation.
#    06/29/15         4480         dgilling       Implement __hash__, __eq__
#                                                 and __str__.

import six


class MasterLevel(object):

    def __init__(self, name=None):
        self.name = name
        self.description = None
        self.unitString = None
        self.type = None
        self.identifier = None

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if not isinstance(self, type(other)):
            return False
        else:
            return self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        if six.PY2:
            retVal = "MasterLevel["
            retVal += "name=" + str(self.name) + ","
            retVal += "type=" + str(self.type) + ","
            retVal += "unit=" + str(self.unitString) + ","
            retVal += "description=" + str(self.description)
            retVal += "]"
        else:
            retVal = "MasterLevel["
            retVal += "name=" + str(self.name.decode('utf-8')) + ","
            retVal += "type=" + str(self.type.decode('utf-8')) + ","
            retVal += "unit=" + str(self.unitString.decode('utf-8')) + ","
            retVal += "description=" + str(self.description.decode('utf-8'))
            retVal += "]"
        return retVal

    def getName(self):
        if six.PY2:
            return self.name
        if (self.name is not None) and (not isinstance(self.name, str)):
            return self.name.decode('utf-8')
        return self.name

    def setName(self, name):
        self.name = name

    def getDescription(self):
        if six.PY2:
            return self.description
        if self.description is not None:
            return self.description.decode('utf-8')
        return self.description

    def setDescription(self, description):
        self.description = description

    def getUnitString(self):
        if six.PY2:
            return self.unitString
        if self.unitString is not None:
            return self.unitString.decode('utf-8')
        return self.unitString

    def setUnitString(self, unitString):
        self.unitString = unitString

    def getType(self):
        if six.PY2:
            return self.type
        if self.type is not None:
            return self.type.decode('utf-8')
        return self.type

    def setType(self, leveltype):
        self.type = leveltype

    def getIdentifier(self):
        if six.PY2:
            return self.identifier
        if self.identifier is not None:
            return self.identifier.decode('utf-8')
        return self.identifier

    def setIdentifier(self, identifier):
        self.identifier = identifier
