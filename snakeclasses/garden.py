from random import randint


class Garden:
    """Game map."""

    apples = set()
    borders = (640, 480)

    @classmethod
    def set_borders(cls, borders):
        """Set borders."""
        cls.borders = borders

    @classmethod
    def get_borders(cls):
        """Get borders."""
        return cls.borders

    @classmethod
    def generate_apple(cls, blacklist):
        """Generate apple, that not lands in blacklis."""
        while True:
            x = randint(0, cls.borders[0])
            y = randint(0, cls.borders[1])
            if not (x, y) in blacklist:
                cls.add_apple((x, y))
                break

    @classmethod
    def add_apple(cls, cords):
        """Adds apple to set."""
        cls.apples.add(cords)

    @classmethod
    def is_apple_here(cls, cords):
        """Chekout if there apple in cords."""
        return cords in cls.apples

    @classmethod
    def get_apples(cls):
        """Return all apples."""
        return cls.apples

    @classmethod
    def clear(cls):
        """Clear field from apples."""
        cls.apples.clear()
