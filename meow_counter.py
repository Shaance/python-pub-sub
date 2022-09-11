from pubsub import Pubsub
from events import MEOW_EVENT

class MeowCounter:
    def __init__(self):
        self.count = 0
        Pubsub.instance().subscribe(MEOW_EVENT, self.on_cat_meow)

    def on_cat_meow(self, cat_name):
        print(
            "Cat {} meowed! Old count: {}, new count: {}".format(
                cat_name, self.count, self.count + 1
            )
        )
        self.count += 1

    def get_count(self):
        return self.count
