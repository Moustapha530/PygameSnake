import pygame
from snake import create_snake, draw_snake, has_collision
from food import create_food, draw_food
from score import draw_score
from enum import Enum

class Directions(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake Game")

score = 0
font = pygame.font.SysFont(None, 36)

cell_size = 10
snake_direction = Directions.UP
update_snake = 0

snake = create_snake(screen, cell_size)
food = create_food(screen, cell_size, snake)

running = True
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            # Up
            if event.key == pygame.K_UP and snake_direction != Directions.DOWN:
                snake_direction = Directions.UP
            # Down
            elif event.key == pygame.K_DOWN and snake_direction != Directions.UP:
                snake_direction = Directions.DOWN
            # Left
            elif event.key == pygame.K_LEFT and snake_direction != Directions.RIGHT:
                snake_direction = Directions.LEFT
            # Right
            elif event.key == pygame.K_RIGHT and snake_direction != Directions.LEFT:
                snake_direction = Directions.RIGHT

    # Update the snake
    if update_snake > 99:
        update_snake = 0

        if snake[0] == food:
            snake = [food] + snake
            score += 1
            food = create_food(screen, cell_size, snake)
        else:
            snake = snake[-1:] + snake[:-1]

        if snake_direction == Directions.UP:
            snake[0][0] = snake[1][0]
            snake[0][1] = snake[1][1] - cell_size
        elif snake_direction == Directions.DOWN:
            snake[0][0] = snake[1][0]
            snake[0][1] = snake[1][1] + cell_size
        elif snake_direction == Directions.RIGHT:
            snake[0][1] = snake[1][1]
            snake[0][0] = snake[1][0] + cell_size
        elif snake_direction == Directions.LEFT:
            snake[0][1] = snake[1][1]
            snake[0][0] = snake[1][0] - cell_size

    screen.fill((255, 200, 150))
    draw_snake(screen, snake, cell_size)
    draw_food(screen, food, cell_size)
    draw_score(screen, score, font)


    pygame.display.update()
    update_snake += 1

    # Check for collisions
    if has_collision(screen, snake):
        snake = create_snake(screen, cell_size)
        snake_direction = Directions.UP
        score = 0

pygame.quit()