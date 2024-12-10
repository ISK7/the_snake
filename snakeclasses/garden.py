"""game map"""
from random import randint


class Garden:
    apples = set()
    borders = (640, 480)

    @classmethod
    def set_borders(cls, borders):
        """set borders"""
        cls.borders = borders

    @classmethod
    def get_borders(cls):
        """get borders"""
        return cls.borders

    @classmethod
    def generate_apple(cls, blacklist):
        """generate apple, that not lands in blacklis"""
        while True:
            x = randint(0, cls.borders[0])
            y = randint(0, cls.borders[1])
            if not (x, y) in blacklist:
                cls.add_apple((x, y))
                break

    @classmethod
    def add_apple(cls, cords):
        """adds apple to set"""
        cls.apples.add(cords)

    @classmethod
    def is_apple_here(cls, cords):
        """chekout if there apple in cords"""
        return cords in cls.apples

    @classmethod
    def get_apples(cls):
        """return all apples"""
        return cls.apples
