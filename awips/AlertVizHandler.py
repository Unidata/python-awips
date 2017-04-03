##
##


#
# Pure python logging mechanism for logging to AlertViz from
# pure python (ie not JEP).  DO NOT USE IN PYTHON CALLED
# FROM JAVA.
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    08/18/10                      njensen       Initial Creation.
#
#
#

import logging
from . import NotificationMessage

class AlertVizHandler(logging.Handler):

    def __init__(self, host='localhost', port=61999, category='LOCAL', source='ANNOUNCER', level=logging.NOTSET):
        logging.Handler.__init__(self, level)
        self._category = category
        self._host = host
        self._port = port
        self._source = source

    def emit(self, record):
        "Implements logging.Handler's interface.  Record argument is a logging.LogRecord."
        priority = None
        if record.levelno >= 50:
            priority = 'CRITICAL'
        elif record.levelno >= 40:
            priority = 'SIGNIFICANT'
        elif record.levelno >= 30:
            priority = 'PROBLEM'
        elif record.levelno >= 20:
            priority = 'EVENTA'
        elif record.levelno >= 10:
            priority = 'EVENTB'
        else:
            priority = 'VERBOSE'

        msg = self.format(record)

        notify = NotificationMessage.NotificationMessage(self._host, self._port, msg, priority, self._category, self._source)
        notify.send()

