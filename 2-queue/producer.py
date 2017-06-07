import sys
import time

from redis import Redis


def publish(queue, message):
    r = Redis()

    r.lpush(queue, message)
    print('Published... {}'.format(message))


counter = 0
while True:
    publish(sys.argv[1], 'Message {}'.format(counter))

    time.sleep(1)
    counter += 1
