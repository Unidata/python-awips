##
# This software was developed and / or modified by Raytheon Company,
# pursuant to Contract DG133W-05-CQ-1067 with the US Government.
#
# U.S. EXPORT CONTROLLED TECHNICAL DATA
# This software product contains export-restricted data whose
# export/transfer/disclosure is restricted by U.S. law. Dissemination
# to non-U.S. persons whether in the United States or abroad requires
# an export license or other authorization.
#
# Contractor Name:        Raytheon Company
# Contractor Address:     6825 Pine Street, Suite 340
#                         Mail Stop B8
#                         Omaha, NE 68106
#                         402.291.0100
#
# See the AWIPS II Master Rights File ("Master Rights File.pdf") for
# further licensing information.
##

#
# Common methods for the a2gtrad and a2advrad scripts.
#
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    08/13/2014      3393          nabowle        Initial creation to contain common
#                                                 code for a2*radStub scripts.
#    03/15/2015                    mjames@ucar    Edited/added to awips package as RadarCommon
#
#

import argparse
import sys

from datetime import datetime
from datetime import timedelta
from awips import ThriftClient

from dynamicserialize.dstypes.com.raytheon.uf.common.time import TimeRange
from dynamicserialize.dstypes.com.raytheon.uf.common.dataplugin.radar.request import GetRadarDataRecordRequest

def get_datetime_str(record):
    return str(record.getDataTime())[0:19].replace(" ","_") + ".0"

def get_data_type(azdat):
    if azdat:
        dattyp = "radial"
    else :
        dattyp = "raster"
    return dattyp

def get_hdf5_data(idra):
    rdat = []
    azdat = []
    depVals = []
    threshVals = []
    if len(idra) > 0:
        for ii in range(len(idra)):
           if idra[ii].getName() == "Data":
              rdat = idra[ii]
           elif idra[ii].getName() == "Angles":
              azdat = idra[ii]
              dattyp = "radial"
           elif idra[ii].getName() == "DependentValues":
              depVals = idra[ii].getShortData()
           elif idra[ii].getName() == "Thresholds":
              threshVals = idra[ii].getShortData()

    return rdat,azdat,depVals,threshVals


def get_header(record, format, xLen, yLen, azdat, description):
    # Encode dimensions, time, mapping, description, tilt, and VCP
    mytime = get_datetime_str(record)
    dattyp = get_data_type(azdat)

    if format :
        msg = str(xLen) + " " + str(yLen) + " " + mytime + " " + \
            dattyp + " " + str(record.getLatitude()) + " " +  \
            str(record.getLongitude()) + " " +  \
            str(record.getElevation()) + " " +  \
            str(record.getElevationNumber()) + " " +  \
            description + " " + str(record.getTrueElevationAngle()) + " " + \
            str(record.getVolumeCoveragePattern()) + "\n"
#"%.1f"%
    else :
        msg = str(xLen) + " " + str(yLen) + " " + mytime + " " + \
            dattyp + " " + description + " " + \
            str(record.getTrueElevationAngle()) + " " + \
            str(record.getVolumeCoveragePattern()) + "\n"

    return msg


def encode_thresh_vals(threshVals):
    spec = [".", "TH", "ND", "RF", "BI", "GC", "IC", "GR", "WS", "DS",
            "RA", "HR", "BD", "HA", "UK"]
    nnn = len(threshVals)
    j = 0
    msg = ""
    while j<nnn :
        lo = threshVals[j] % 256
        hi = threshVals[j] / 256
        msg += " "
        j += 1
        if hi < 0 :
            if lo > 14 :
                msg += "."
            else :
                msg += spec[lo]
            continue
        if hi % 16 >= 8 :
            msg += ">"
        elif hi % 8 >= 4 :
            msg += "<"
        if hi % 4 >= 2 :
            msg += "+"
        elif hi % 2 >= 1 :
            msg += "-"
        if hi >= 64 :
            msg += "%.2f"%(lo*0.01)
        elif hi % 64 >= 32 :
            msg += "%.2f"%(lo*0.05)
        elif hi % 32 >= 16 :
            msg += "%.1f"%(lo*0.1)
        else :
            msg += str(lo)
    msg += "\n"
    return msg


def encode_dep_vals(depVals):
    nnn = len(depVals)
    j = 0
    msg = []
    while j<nnn :
        msg.append(str(depVals[j]))
        j += 1
    return msg


def encode_radial(azVals):
    azValsLen = len(azVals)
    j = 0
    msg = []
    while j<azValsLen :
        msg.append(azVals[j])
        j += 1
    return msg
