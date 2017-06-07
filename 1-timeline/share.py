import os
import sys

from redis import Redis

r = Redis()

r.lpush(sys.argv[1], sys.argv[2])
r.ltrim(sys.argv[1], 0, 4)
