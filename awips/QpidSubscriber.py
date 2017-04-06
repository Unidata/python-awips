##
##

#
# Provides a Python-based interface for subscribing to qpid queues and topics.
#
#
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    11/17/10                      njensen       Initial Creation.
#    08/15/13        2169          bkowal        Optionally gzip decompress any data that is read.
#
#

import qpid
import zlib

from queue import Empty
from qpid.exceptions import Closed

class QpidSubscriber:

    def __init__(self, host='127.0.0.1', port=5672, decompress=False):
        self.host = host
        self.port = port
        self.decompress = decompress;
        socket = qpid.util.connect(host, port)
        self.__connection = qpid.connection.Connection(sock=socket, username='guest', password='guest')
        self.__connection.start()
        self.__session = self.__connection.session(str(qpid.datatypes.uuid4()))
        self.subscribed = True

    def topicSubscribe(self, topicName, callback):
        # if the queue is edex.alerts, set decompress to true always for now to
        # maintain compatibility with existing python scripts.
        if (topicName == 'edex.alerts'):
            self.decompress = True

        print("Establishing connection to broker on", self.host)
        queueName = topicName + self.__session.name
        self.__session.queue_declare(queue=queueName, exclusive=True, auto_delete=True, arguments={'qpid.max_count':100, 'qpid.policy_type':'ring'})
        self.__session.exchange_bind(exchange='amq.topic', queue=queueName, binding_key=topicName)
        self.__innerSubscribe(queueName, callback)

    def __innerSubscribe(self, serverQueueName, callback):
        local_queue_name = 'local_queue_' + serverQueueName
        queue = self.__session.incoming(local_queue_name)
        self.__session.message_subscribe(serverQueueName, destination=local_queue_name)
        queue.start()
        print("Connection complete to broker on", self.host)

        while self.subscribed:
            try:
                message = queue.get(timeout=10)
                content = message.body
                self.__session.message_accept(qpid.datatypes.RangedSet(message.id))
                if (self.decompress):
                    print("Decompressing received content")
                    try:
                        # http://stackoverflow.com/questions/2423866/python-decompressing-gzip-chunk-by-chunk
                        d = zlib.decompressobj(16+zlib.MAX_WBITS)
                        content = d.decompress(content)
                    except:
                        # decompression failed, return the original content
                        pass
                callback(content)
            except Empty:
                pass
            except Closed:
                self.close()

    def close(self):
        self.subscribed = False
        try:
            self.__session.close(timeout=10)
        except:
            pass
