from collections import defaultdict

# singleton class
class Pubsub(object):

    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            print('Creating unique instance of Pubsub')
            cls._instance = cls.__new__(cls)
            cls._instance.subscribers = defaultdict(set)
        return cls._instance

    def subscribe(cls, topic, callback):
        cls.subscribers[topic].add(callback)

    def publish(cls, topic, *args, **kwargs):
        if topic in cls.subscribers:
            for callback in cls.subscribers[topic]:
                callback(*args, **kwargs)

    def unsubscribe(cls, topic, callback):
        if topic in cls.subscribers:
            cls.subscribers[topic].remove(callback)
