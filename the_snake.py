import pygame
from random import randint

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки:
SPEED = 20

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption('Змейка')

# Настройка времени:
clock = pygame.time.Clock()


class GameObject:
    """Plug for tests"""

    attr = None


class Section(GameObject):
    """One section of snake."""

    section_size = 20
    section_x = 0
    section_y = 0

    def __init__(self, cords=(0, 0), size=20):
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


class Apple(GameObject):
    """Apple"""

    cords = [0, 0]


class Garden(GameObject):
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
    def dell_apple(cls, cords):
        """Delets apple from the set"""
        cls.apples.remove(cords)

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


class Snake(GameObject):
    """Full snake."""

    sections = []
    one_segment_size = 20
    dirrection = (0, 0)

    def __init__(self, cords=(15, 15), len=3, direction=RIGHT, size=20):
        """Constructor."""
        self.__clear__()
        self.one_segment_size = size
        self.dirrection = direction
        for i in range(len):
            self.add_section((cords[0] + direction[0] * (i - len),
                             cords[1] + direction[1] * (i - len)))

    def add_section(self, cords):
        """Ads new segment to snake."""
        sect = Section(cords, self.one_segment_size)
        self.sections.append(sect)

    def change_dirrection(self, dir):
        """Changes dirrection of snake."""
        self.dirrection = dir

    def get_direction(self):
        """Retuns snake dirrection."""
        return self.dirrection

    def move(self):
        """To the next sell."""
        grdn = Garden
        new_front = [self.sections[-1].get_cords()[0] + self.dirrection[0],
                     self.sections[-1].get_cords()[1] + self.dirrection[1]]
        """If snake move into border."""
        borders = grdn.get_borders()
        new_front[0] = new_front[0] % borders[0]
        new_front[1] = new_front[1] % borders[1]
        """If snake breaks itself."""
        for i in self.sections:
            if i.is_here(new_front):
                return 0
        """If snake get apple."""
        if grdn.is_apple_here(tuple(new_front)):
            self.add_section(tuple(new_front))
            grdn.dell_apple(tuple(new_front))
            return 1
        """Default case."""
        for i in range(len(self.sections) - 1):
            self.sections[i].set_cords(self.sections[i + 1].get_cords())
        self.sections[-1].set_cords(new_front)
        return 2

    def get_sections(self):
        """Returns all snace sections."""
        return self.sections

    def __clear__(self):
        """Delete all sections"""
        self.sections.clear()


def handle_keys(plr):
    """Функция обработки действий пользователя."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and plr.get_direction() != DOWN:
                plr.change_dirrection(UP)
            elif event.key == pygame.K_DOWN and plr.get_direction() != UP:
                plr.change_dirrection(DOWN)
            elif event.key == pygame.K_LEFT and plr.get_direction() != RIGHT:
                plr.change_dirrection(LEFT)
            elif event.key == pygame.K_RIGHT and plr.get_direction() != LEFT:
                plr.change_dirrection(RIGHT)


def draw_rect(color, cords):
    """Draw a rectangle."""
    rect = pygame.Rect(cords[0], cords[1], GRID_SIZE, GRID_SIZE)
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


def draw_field(apples, snake):
    """Draw full game field."""
    for a in apples:
        draw_rect(APPLE_COLOR, a)
    for s in snake:
        draw_rect(SNAKE_COLOR, s.get_cords())


def main():
    """Main."""
    # Инициализация PyGame:
    pygame.init()
    # Тут нужно создать экземпляры классов.
    player = Snake((15, 15), 3, LEFT, GRID_SIZE)
    gard = Garden
    gard.set_borders((GRID_WIDTH, GRID_HEIGHT))

    while True:
        clock.tick(SPEED)
        gard.generate_apple(player.get_sections())
        code = player.move()
        if code == 1:
            gard.generate_apple(player.get_sections())
        if code == 0:
            player = Snake((15, 15), 3, LEFT, GRID_SIZE)
            gard.clear()
        code = player.move()
        draw_field(gard.get_apples(), player.get_sections())
        handle_keys(player)


if __name__ == '__main__':
    main()
