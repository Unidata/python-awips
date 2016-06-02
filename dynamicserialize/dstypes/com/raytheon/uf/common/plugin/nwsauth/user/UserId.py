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

import os

try:
    import pwd
    pwd_error = False
except ImportError:
    pwd_error = True

class UserId(object):

    def __init__(self, id = None):
        if id is None:
           if not pwd_error:
              self.id = pwd.getpwuid(os.getuid()).pw_name
           else:
              self.id = "GenericUsername"
        else:
           self.id = id

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

