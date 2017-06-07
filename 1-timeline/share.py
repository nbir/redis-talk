import os
import sys

from redis import Redis

MAX_POSTS = 5

handle = sys.argv[1]
message = sys.argv[2]

r = Redis()

r.lpush(handle, message)
r.ltrim(handle, 0, MAX_POSTS - 1)
