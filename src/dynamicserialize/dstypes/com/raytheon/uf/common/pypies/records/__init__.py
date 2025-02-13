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
# Package definition for com.raytheon.uf.common.datastorage.records
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    08/31/10                      njensen        Initial Creation.
#    Apr 24, 2015    4425          nabowle        Add DoubleDataRecord
#    Oct 04, 2018    7435          ksunil         Added Chunked records
#    Jan 28, 2020    7985          ksunil         Removed the compression changes introduced in 7985 
#
#


__all__ = [
            'CompressedDataRecord'
          ]
from .CompressedDataRecord import CompressedDataRecord

