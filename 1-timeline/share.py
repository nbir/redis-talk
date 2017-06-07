import os
import sys

from redis import Redis

handle = sys.argv[1]
message = sys.argv[2]
max_posts = 5

r = Redis()

r.lpush(handle, message)
r.ltrim(handle, 0, max_posts - 1)
