"""one section of snake"""


class Section:
    section_size = 20
    section_x = 0
    section_y = 0

    def __init__(self, cords, size=20):
        """constructor"""
        self.section_x = cords[0]
        self.section_y = cords[1]
        self.section_size = size

    def is_here(self, cords):
        """chekout a sections collision"""
        if self.section_x == cords[0] and self.section_y == cords[1]:
            return True
        return False

    def get_cords(self):
        """return section cords"""
        return (self.section_x, self.section_y)

    def set_cords(self, cords):
        """set section cords"""
        self.section_x = cords[0]
        self.section_y = cords[1]
