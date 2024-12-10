import pygame
from snakeclasses import snake, garden

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


# Функция обработки действий пользователя
def handle_keys(plr):
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
    rect = pygame.Rect(cords[0], cords[1], GRID_SIZE, GRID_SIZE)
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


def draw_field(apples, snake):
    for a in apples:
        draw_rect(APPLE_COLOR, a)
    for s in snake:
        draw_rect(SNAKE_COLOR, s.get_cords())


def main():
    # Инициализация PyGame:
    pygame.init()
    # Тут нужно создать экземпляры классов.
    player = snake.snake((15, 15), 3, LEFT, GRID_SIZE)
    gard = garden.garden
    gard.set_borders((GRID_WIDTH, GRID_HEIGHT))

    while True:
        clock.tick(SPEED)
        gard.generate_apple(player.get_sections())
        code = player.move()
        if code == 1:
            gard.generate_apple(player.get_sections())
        if code == 0:
            break
        code = player.move()
        draw_field(gard.get_apples(), player.get_sections())
        handle_keys(player)


if __name__ == '__main__':
    main()
