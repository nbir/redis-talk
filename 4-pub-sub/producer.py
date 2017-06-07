import random
import time

from redis import Redis

MESSAGE_TYPES = ['command', 'error']
COMPONENT_NAMES = ['fuel', 'control-rod', 'turbine', 'water-supply']
PRIORITIES = ['normal', 'critical']


def publish(channel, message):
    r = Redis()

    r.publish(channel, message)
    print('Published... {}'.format(message))


while True:
    message_type = random.choice(MESSAGE_TYPES)
    component_name = random.choice(COMPONENT_NAMES)
    priority = random.choice(PRIORITIES)

    channel = '{}.{}.{}'.format(message_type, component_name, priority)
    message = 'Message {}'.format(channel)

    publish(channel, message)

    time.sleep(1)
