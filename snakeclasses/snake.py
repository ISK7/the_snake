"""full snake"""


from snakeclasses import garden, section


class Snake:
    sections = []
    one_segment_size = 20
    dirrection = (0, 0)

    def __init__(self, cords, len, direction, size=20):
        """constructor"""
        self.__clear__()
        self.one_segment_size = size
        self.dirrection = direction
        for i in range(len):
            self.add_section((cords[0] + direction[0] * (i - len),
                             cords[1] + direction[1] * (i - len)))

    def add_section(self, cords):
        """ads new segment to snake"""
        sect = section.Section(cords, self.one_segment_size)
        self.sections.append(sect)

    def change_dirrection(self, dir):
        """changes dirrection of snake"""
        self.dirrection = dir

    def get_direction(self):
        """retuns snake dirrection"""
        return self.dirrection

    def move(self):
        """to the next sell"""
        grdn = garden.Garden
        new_front = [self.sections[-1].get_cords()[0] + self.dirrection[0],
                     self.sections[-1].get_cords()[1] + self.dirrection[1]]
        """if snake move into border"""
        borders = grdn.get_borders()
        new_front[0] = new_front[0] % borders[0]
        new_front[1] = new_front[1] % borders[1]
        """if snake breaks itself"""
        for i in self.sections:
            if i.is_here(new_front):
                return 0
        """if snake get apple"""
        if grdn.is_apple_here(tuple(new_front)):
            self.add_section(tuple(new_front))
            return 1
        """default case"""
        for i in range(len(self.sections) - 1):
            self.sections[i].set_cords(self.sections[i + 1].get_cords())
        self.sections[-1].set_cords(new_front)
        return 2

    def get_sections(self):
        """returns all snace sections"""
        return self.sections

    def __clear__(self):
        self.sections.clear()
