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


def get_datetime_str(record):
    """
    Get the datetime string for a record.

    Args:
            record: the record to get data for.

    Returns:
            datetime string.
    """
    return str(record.getDataTime())[0:19].replace(" ", "_") + ".0"


def get_data_type(azdat):
    """
    Get the radar file type (radial or raster).

    Args:
            azdat: Boolean.

    Returns:
            Radial or raster.
    """
    if azdat:
        return "radial"
    return "raster"


def get_hdf5_data(idra):
    rdat = []
    azdat = []
    depVals = []
    threshVals = []
    if idra:
        for item in idra:
            if item.getName() == "Data":
                rdat = item
            elif item.getName() == "Angles":
                azdat = item
                # dattyp = "radial"
            elif item.getName() == "DependentValues":
                depVals = item.getShortData()
            elif item.getName() == "Thresholds":
                threshVals = item.getShortData()

    return rdat, azdat, depVals, threshVals


def get_header(record, headerFormat, xLen, yLen, azdat, description):
    # Encode dimensions, time, mapping, description, tilt, and VCP
    mytime = get_datetime_str(record)
    dattyp = get_data_type(azdat)

    if headerFormat:
        msg = str(xLen) + " " + str(yLen) + " " + mytime + " " + \
            dattyp + " " + str(record.getLatitude()) + " " +  \
            str(record.getLongitude()) + " " +  \
            str(record.getElevation()) + " " +  \
            str(record.getElevationNumber()) + " " +  \
            description + " " + str(record.getTrueElevationAngle()) + " " + \
            str(record.getVolumeCoveragePattern()) + "\n"
    else:
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
    while j < nnn:
        lo = threshVals[j] % 256
        hi = threshVals[j] / 256
        msg += " "
        j += 1
        if hi < 0:
            if lo > 14:
                msg += "."
            else:
                msg += spec[lo]
            continue
        if hi % 16 >= 8:
            msg += ">"
        elif hi % 8 >= 4:
            msg += "<"
        if hi % 4 >= 2:
            msg += "+"
        elif hi % 2 >= 1:
            msg += "-"
        if hi >= 64:
            msg += "%.2f" % (lo*0.01)
        elif hi % 64 >= 32:
            msg += "%.2f" % (lo*0.05)
        elif hi % 32 >= 16:
            msg += "%.1f" % (lo*0.1)
        else:
            msg += str(lo)
    msg += "\n"
    return msg


def encode_dep_vals(depVals):
    nnn = len(depVals)
    j = 0
    msg = []
    while j < nnn:
        msg.append(str(depVals[j]))
        j += 1
    return msg


def encode_radial(azVals):
    azValsLen = len(azVals)
    j = 0
    msg = []
    while j < azValsLen:
        msg.append(azVals[j])
        j += 1
    return msg
