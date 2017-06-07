import sys
import time

from redis import Redis

queue_name = sys.argv[1]

r = Redis()

counter = 0

while True:
    message = 'Message {}'.format(counter)
    r.rpush(queue_name, message)

    print('Published... {}'.format(message))

    time.sleep(1)
    counter += 1
