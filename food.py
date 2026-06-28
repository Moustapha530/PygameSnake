import random
import pygame

def create_food(screen : pygame.Surface, cell_size : int, snake : list[list[int]]) -> list[int]:
    columns = screen.get_width() // cell_size
    rows = screen.get_height() // cell_size
    while True:
        food_x = random.randrange(columns) * cell_size
        food_y = random.randrange(rows) * cell_size
        food = [food_x, food_y]
        if food not in snake:
            return food
        
def draw_food(screen : pygame.Surface, food : list[int], cell_size : int) -> None:
    pygame.draw.rect(screen, (255, 0, 0), (food[0], food[1], cell_size, cell_size))
