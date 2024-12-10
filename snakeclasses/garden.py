"""game map"""
from random import randint


class garden:
    apples = set()
    borders = (640, 480)

    @classmethod
    def set_borders(cls, borders):
        cls.borders = borders

    @classmethod
    def get_borders(cls):
        return cls.borders

    @classmethod
    def generate_apple(cls, blacklist):
        while True:
            x = randint(0, cls.borders[0])
            y = randint(0, cls.borders[1])
            if not (x, y) in blacklist:
                cls.add_apple((x, y))
                break

    @classmethod
    def add_apple(cls, cords):
        cls.apples.add(cords)

    @classmethod
    def is_apple_here(cls, cords):
        return cords in cls.apples

    @classmethod
    def get_apples(cls):
        return cls.apples
