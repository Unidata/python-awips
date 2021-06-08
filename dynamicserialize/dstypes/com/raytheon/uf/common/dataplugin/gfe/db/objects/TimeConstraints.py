#
# 03/20/2013     #1774    randerso  Removed setters, added isValid.


import logging

HOUR = 3600
DAY = 24 * HOUR


class TimeConstraints(object):

    def __init__(self, duration=0, repeatInterval=0, startTime=0):
        duration = int(duration)
        repeatInterval = int(repeatInterval)
        startTime = int(startTime)

        self.valid = False
        if duration == 0 and repeatInterval == 0 and startTime == 0:
            self.valid = True
        else:
            if self.isInvalidInterval(repeatInterval, duration, startTime):
                logging.warning("Bad init values for TimeConstraints: "
                                + str(duration) + ", "
                                + str(repeatInterval) + ", "
                                + str(startTime))
                self.valid = False
                duration = 0
                repeatInterval = 0
                startTime = 0
            else:
                self.valid = True

        self.duration = duration
        self.repeatInterval = repeatInterval
        self.startTime = startTime

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        if not self.isValid():
            return "<Invalid>"
        elif not self.anyConstraints():
            return "<NoConstraints>"
        else:
            return "[s=" + str(self.startTime / HOUR) + "h, i=" + \
                   str(self.repeatInterval / HOUR) + "h, d=" + \
                   str(self.duration / HOUR) + "h]"

    def __eq__(self, other):
        if not isinstance(other, TimeConstraints):
            return False
        if self.isValid() != other.isValid():
            return False
        if self.duration != other.duration:
            return False
        if self.repeatInterval != other.repeatInterval:
            return False
        return self.startTime == other.startTime

    def __ne__(self, other):
        return not self.__eq__(other)

    def anyConstraints(self):
        return self.duration != 0

    def isValid(self):
        return self.valid

    def getDuration(self):
        return self.duration

    def getRepeatInterval(self):
        return self.repeatInterval

    def getStartTime(self):
        return self.startTime

    def isInvalidInterval(self, interval, duration, startTime):
        if interval <= 0 or interval > DAY or interval < duration:
            return False
        if startTime < 0 or startTime > DAY:
            return False
        if duration < 0 or duration > DAY:
            return False
        if DAY % interval != 0:
            return False
        return True
