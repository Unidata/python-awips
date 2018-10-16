import sys


class Record():
    def __init__(self, level=0, msg='Test Message'):
        self.levelno = level
        self.message = msg
        self.exc_info = sys.exc_info()
        self.exc_text = "TEST"

    def getMessage(self):
        return self.message
