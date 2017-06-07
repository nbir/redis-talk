import random
import sys
import time

from redis import Redis

CHOICES = [
    'apple', 'bananas', 'pear', 'peach', 'mango', 'chicken', 'pork', 'chips',
    'lasagna', 'cookies', 'cake', 'muffins', 'cupcakes', 'bread', 'butter',
    'salad', 'celery', 'cabbage', 'broccili', 'cucumber', 'tomatoes', 'carrot',
    'soup', 'noodles', 'tea', 'soda', 'water', 'zuccinii', 'orange', 'lemon',
    'lime', 'oats', 'cereal', 'milk', 'fries', 'burger', 'ice cream',
    'waffles', 'pancakes', 'french toast', 'ranch', 'macaroni and cheese',
    'fish', 'sushi', 'lobster', 'calamari', 'escargo', 'frog legs',
    'pineapple', 'borchts', 'mille-feuille', 'sio pao', 'guacomole', 'peas',
    'corn', 'turkey', 'ham', 'cheese', 'nachos', 'hot dog', 'fries',
    'milkshakes', 'peppers', 'coconuts', 'cocoa', 'watermelon', 'melon',
    'beef', 'nuts', 'peanuts', 'cashews', 'coffee', 'toast', 'lamp'
]


def publish(queue, message):
    r = Redis()

    r.lpush(queue, message)
    print('Produced... {}'.format(message))


while True:
    item = random.choice(CHOICES)
    publish(sys.argv[1], item)

    time.sleep(1)
