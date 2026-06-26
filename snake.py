import pygame

def create_snake(screen : pygame.Surface, cell_size : int) -> list[list[int]]:
    snake = [[int(screen.get_width() / 2), int(screen.get_height() / 2)],
             [int(screen.get_width() / 2), int(screen.get_height() / 2) + cell_size],
             [int(screen.get_width() / 2), int(screen.get_height() / 2) + cell_size * 2],
             [int(screen.get_width() / 2), int(screen.get_height() / 2) + cell_size * 3]]
    return snake

def draw_snake(screen : pygame.Surface, snake : list[list[int]], cell_size : int) -> None:
    body_inner = (50, 175, 25)
    body_outer = (100, 100, 200)
    head = 1
    for x in snake:
        if head == 0:
            pygame.draw.rect(screen, body_outer, (x[0], x[1], cell_size, cell_size))
            pygame.draw.rect(screen, body_inner, (x[0] + 1, x[1] + 1, cell_size - 2, cell_size - 2))
        elif head == 1:
            pygame.draw.rect(screen, body_outer, (x[0], x[1], cell_size, cell_size))
            pygame.draw.rect(screen, (255, 0, 0), (x[0] + 1, x[1] + 1, cell_size - 2, cell_size - 2))
            head = 0