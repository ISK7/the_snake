class Section:
    """One section of snake."""
    
    section_size = 20
    section_x = 0
    section_y = 0

    def __init__(self, cords, size=20):
        """Constructor."""
        self.section_x = cords[0]
        self.section_y = cords[1]
        self.section_size = size

    def is_here(self, cords):
        """Chekout a sections collision."""
        if self.section_x == cords[0] and self.section_y == cords[1]:
            return True
        return False

    def get_cords(self):
        """Return section cords."""
        return (self.section_x, self.section_y)

    def set_cords(self, cords):
        """Set section cords."""
        self.section_x = cords[0]
        self.section_y = cords[1]
