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

# File auto-generated against equivalent DynamicSerialize Java class
# and then modified by mapeters

class DataUriMetadataIdentifier(object):

    def __init__(self):
        self.traceId = None
        self.dataUri = None
        self.specificity = 'GROUP'

    def getTraceId(self):
        return self.traceId

    def setTraceId(self, traceId):
        self.traceId = traceId

    def getDataUri(self):
        return self.dataUri

    def setDataUri(self, dataUri):
        self.dataUri = dataUri

    def getSpecificity(self):
        return self.specificity

    def setSpecificity(self, specificity):
        self.specificity = specificity

