import os
import sys
import time

from redis import Redis

handle = sys.argv[1]

r = Redis()

while True:
    os.system('clear')
    print('{}\'s timeline...\n'.format(handle))

    items = r.lrange(handle, 0, -1)

    for item in items:
        print(item)

    time.sleep(1)
