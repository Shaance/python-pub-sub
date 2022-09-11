from pubsub import Pubsub
from events import MEOW_EVENT, DOG_BARK_EVENT

class Cat:
    def __init__(self, name):
        self.name = name
        Pubsub.instance().subscribe(DOG_BARK_EVENT, self.on_dog_bark)

    def meow(self):
        print("Meow!")
        Pubsub.instance().publish(MEOW_EVENT, self.name)

    def on_dog_bark(self, dog_name):
        print(
            "Dog {} barked! Subscribed cat {} will now meow".format(dog_name, self.name)
        )
        self.meow()
    
