import pygame
from snake import create_snake, draw_snake

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake Game")
screen.fill((255, 255, 150))

cell_size = 10
snake = create_snake(screen, cell_size)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_snake(screen, snake, cell_size)

    pygame.display.flip()

pygame.quit()