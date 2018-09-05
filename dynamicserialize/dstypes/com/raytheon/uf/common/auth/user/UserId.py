##
##

# File auto-generated against equivalent DynamicSerialize Java class

import os, pwd

class UserId(object):

    def __init__(self, id = None):
        if id is None:
           self.id = pwd.getpwuid(os.getuid()).pw_name
        else:
           self.id = id

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

