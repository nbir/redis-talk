import sys

from redis import Redis


def consume(queue):
    r = Redis()

    (_, message) = r.blpop(queue)
    print('Consumed... {}'.format(message))


while True:
    consume(sys.argv[1])
