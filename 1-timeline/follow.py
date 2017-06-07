import os
import sys
import time

from redis import Redis

r = Redis()


def display_timeline(handle):
    os.system('clear')
    print('{}\'s timeline...\n'.format(handle))

    items = r.lrange(handle, 0, -1)

    for item in items:
        print(item)


while True:
    display_timeline(sys.argv[1])
    time.sleep(1)
