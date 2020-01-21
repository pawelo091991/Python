import random


class Robot:
    name = ''

    def __init__(self):
        self.create_name()

    def reset(self):
        self.name = ''
        self.create_name()

    def create_name(self):
        random.seed()
        for i in range(2):
            self.name += str(chr(random.randrange(65, 90)))

        for i in range(3):
            self.name += str(random.randrange(0, 9))
