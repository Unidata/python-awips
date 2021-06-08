##
# NOTE: Please do not ever use this class unless you really must. It is not
# designed to be directly accessed from client code. Hide its use from end-
# users as best as you can.
##

##
# IMPLEMENTATION DETAILS:
# This class is an attempt to simulate Java's EnumSet class. When creating
# a new instance of this class, you must specify the name of the Java enum
# contained within as this is needed for serialization. Do not append the
# "dynamicserialize.dstypes" portion of the Python package to the supplied
# class name as Java won't know what class that is when deserializing.
#
# Since Python has no concept of enums, this class cannot provide the value-
# checking that Java class does. Be very sure that you add only valid enum
# values to your EnumSet.
##

import collections


class EnumSet(collections.MutableSet):

    def __init__(self, enumClassName, iterable=[]):
        self.__enumClassName = enumClassName
        self.__set = set(iterable)

    def __repr__(self):
        return "EnumSet({0})".format(list(self.__set))

    def __len__(self):
        return len(self.__set)

    def __contains__(self, key):
        return key in self.__set

    def __iter__(self):
        return iter(self.__set)

    def add(self, value):
        self.__set.add(value)

    def discard(self, value):
        self.__set.discard(value)

    def getEnumClass(self):
        return self.__enumClassName
