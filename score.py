import pygame


def draw_score(screen : pygame.Surface, score : int, font : pygame.font.Font) -> None:
    score_surface = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_surface, (10, 10))
