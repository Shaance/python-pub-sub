#!/usr/bin/env python3

from dog import Dog
from cat import Cat
from meow_counter import MeowCounter
from pubsub import Pubsub
from events import DOG_BARK_EVENT

def main():
    # counter will print old and new count every time a cat meows
    counter = MeowCounter()
    dog = Dog("Rex")
    # cats are subscribed to dog barks and will meow when a dog barks
    titi = Cat("Titi")
    luna = Cat("Luna")
    # dog barks, both cats meow, counter increments and prints old and new count
    dog.bark()
    pubsub = Pubsub.instance()
    # unsubscribes Titi from dog barks
    pubsub.unsubscribe(DOG_BARK_EVENT, titi.on_dog_bark)
    # dog barks, only Luna meows, counter increments and prints old and new count
    dog.bark()
    # titi meows, counter increments and prints old and new count
    titi.meow()


if __name__ == "__main__":
    main()
