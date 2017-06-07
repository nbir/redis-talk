import sys

from redis import Redis


def consume(consumer, queue):
    r = Redis()

    consumer_queue = 'consumer.{}'.format(consumer)

    r.brpoplpush(queue, consumer_queue)
    (_, message) = r.blpop(consumer_queue)

    print('Consumed by {}... {}'.format(consumer, message))


while True:
    consume(sys.argv[1], sys.argv[2])
