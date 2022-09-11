from pubsub import Pubsub
from events import DOG_BARK_EVENT

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Woof!")
        Pubsub.instance().publish(DOG_BARK_EVENT, self.name)
