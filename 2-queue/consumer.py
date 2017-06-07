import sys

from redis import Redis

queue_name = sys.argv[1]

r = Redis()

while True:
    (_, message) = r.blpop(queue_name)

    print('Consumed... {}'.format(message))
