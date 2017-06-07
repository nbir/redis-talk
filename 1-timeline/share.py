import os
import sys

from redis import Redis

MAX_POSTS = 5


def share(handle, message):
    r = Redis()

    r.lpush(handle, message)
    r.ltrim(handle, 0, MAX_POSTS - 1)


share(sys.argv[1], sys.argv[2])
