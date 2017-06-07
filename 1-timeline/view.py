import os
import sys
import time

from redis import Redis


def view(handle):
    r = Redis()

    print('{}\'s timeline...\n'.format(handle))
    items = r.lrange(handle, 0, -1)

    for item in items:
        print(item)


while True:
    os.system('clear')
    view(sys.argv[1])
    time.sleep(1)
