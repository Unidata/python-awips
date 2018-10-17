# ----------------------------------------------------------------------------
# This software is in the public domain, furnished "as is", without technical
# support, and with no warranty, express or implied, as to its usefulness for
# any purpose.
#
# offsetTime.py
# Handles Displaced Real Time for various applications
#
# Author: hansen/romberg
# ----------------------------------------------------------------------------

import string
import time

# Given the timeStr, return the offset (in seconds)
# from the current time.
# Also return the launchStr i.e. Programs launched from this
# offset application will use the launchStr as the -z argument.
# The offset will be positive for time in the future,
# negative for time in the past.
#
# May still want it to be normalized to the most recent midnight.
#
# NOTES about synchronizing:
# --With synchronizing on, the "current time" for all processes started
#   within a given hour will be the same.
#   This guarantees that GFE's have the same current time and ISC grid
#   time stamps are syncrhonized and can be exchanged.
#   Formatters launched from the GFE in this mode will be synchronized as
#   well by setting the launchStr to use the time difference format
#   (YYYYMMDD_HHMM,YYYYMMDD_HHMM).
#   --This does not solve the problem in the general case.
#     For example, if someone starts the GFE at 12:59 and someone
#     else starts it at 1:01, they will have different offsets and
#     current times.
# --With synchronizing off, when the process starts, the current time
#   matches the drtTime in the command line.  However, with synchronizing
#   on, the current time will be offset by the fraction of the hour at
#   which the process was started. Examples:
#     Actual Starting time:             20040617_1230
#     drtTime                           20040616_0000
#     Synchronizing off:
#        GFE Spatial Editor at StartUp: 20040616_0000
#     Synchronizing on:
#        GFE Spatial Editor at StartUp: 20040616_0030
#


def determineDrtOffset(timeStr):
    launchStr = timeStr
    # Check for time difference
    if timeStr.find(",") >= 0:
        times = timeStr.split(",")
        t1 = makeTime(times[0])
        t2 = makeTime(times[1])
        return t1-t2, launchStr
    # Check for synchronized mode
    synch = 0
    if timeStr[0] == "S":
        timeStr = timeStr[1:]
        synch = 1
    drt_t = makeTime(timeStr)
    gm = time.gmtime()
    cur_t = time.mktime(gm)

    # Synchronize to most recent hour
    # i.e. "truncate" cur_t to most recent hour.
    if synch:
        cur_t = time.mktime((gm[0], gm[1], gm[2], gm[3], 0, 0, 0, 0, 0))
        curStr = '%4s%2s%2s_%2s00\n' % (repr(gm[0]), repr(gm[1]),
                                        repr(gm[2]), repr(gm[3]))
        curStr = curStr.replace(' ', '0')
        launchStr = timeStr + "," + curStr

    offset = drt_t - cur_t
    return int(offset), launchStr


def makeTime(timeStr):
    year = string.atoi(timeStr[0:4])
    month = string.atoi(timeStr[4:6])
    day = string.atoi(timeStr[6:8])
    hour = string.atoi(timeStr[9:11])
    minute = string.atoi(timeStr[11:13])
    # Do not use daylight savings because gmtime is not in daylight
    # savings time.
    return time.mktime((year, month, day, hour, minute, 0, 0, 0, 0))
