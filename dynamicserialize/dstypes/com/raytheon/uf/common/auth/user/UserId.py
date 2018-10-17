import os
try:
    import pwd
    pwd_error = False
except ImportError:
    pwd_error = True


class UserId(object):

    def __init__(self, userid=None):
        if userid is None:
            if not pwd_error:
                self.id = pwd.getpwuid(os.getuid()).pw_name
            else:
                self.id = "GenericUsername"
        else:
            self.id = userid

    def getId(self):
        return self.id

    def setId(self, userid):
        self.id = userid
