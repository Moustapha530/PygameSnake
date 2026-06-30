from pygame import init, QUIT, KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT
from pygame.display import set_mode, set_caption, update
from pygame.event import get
from pygame.font import SysFont

from snake import create_snake, draw_snake, has_collision
from food import create_food, draw_food
from score import draw_score
from enum import Enum

class Directions(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

class Game:
    def __init__(self):
        init()
        self.screen = set_mode((800, 600))
        set_caption("Snake Game")

        self.score = 0
        self.font = SysFont(None, 36)

        self.cell_size = 10
        self.snake_direction = Directions.UP
        self.update_snake = 0

        self.snake = create_snake(self.screen, self.cell_size)
        self.food = create_food(self.screen, self.cell_size, self.snake)

    def draw(self) -> None:
        self.screen.fill((255, 200, 150))
        draw_snake(self.screen, self.snake, self.cell_size)
        draw_food(self.screen, self.food, self.cell_size)
        draw_score(self.screen, self.score, self.font)

    def run(self):
        running = True
        while running:

            self.draw()
            self.update()

            for event in get():

                if event.type == QUIT:
                    running = False

                elif event.type == KEYDOWN:
                    # Up
                    if event.key == K_UP and self.snake_direction != Directions.DOWN:
                        self.snake_direction = Directions.UP
                    # Down
                    elif event.key == K_DOWN and self.snake_direction != Directions.UP:
                        self.snake_direction = Directions.DOWN
                    # Left
                    elif event.key == K_LEFT and self.snake_direction != Directions.RIGHT:
                        self.snake_direction = Directions.LEFT
                    # Right
                    elif event.key == K_RIGHT and self.snake_direction != Directions.LEFT:
                        self.snake_direction = Directions.RIGHT

    
    def update(self) -> None:
        # Update the snake
        if self.update_snake > 99:
            self.update_snake = 0

            if self.snake[0] == self.food:
                self.snake = [self.food] + self.snake
                self.score += 1
                self.food = create_food(self.screen, self.cell_size, self.snake)
            else:
                self.snake = self.snake[-1:] + self.snake[:-1]

            if self.snake_direction == Directions.UP:
                self.snake[0][0] = self.snake[1][0]
                self.snake[0][1] = self.snake[1][1] - self.cell_size
            elif self.snake_direction == Directions.DOWN:
                self.snake[0][0] = self.snake[1][0]
                self.snake[0][1] = self.snake[1][1] + self.cell_size
            elif self.snake_direction == Directions.RIGHT:
                self.snake[0][1] = self.snake[1][1]
                self.snake[0][0] = self.snake[1][0] + self.cell_size
            elif self.snake_direction == Directions.LEFT:
                self.snake[0][1] = self.snake[1][1]
                self.snake[0][0] = self.snake[1][0] - self.cell_size

        update()
        self.update_snake += 1

        # Check for collisions
        if has_collision(self.screen, self.snake):
            self.snake = create_snake(self.screen, self.cell_size)
            self.snake_direction = Directions.UP
            self.score = 0