import pygame

class Point:

    def __init__(self, x, y, isin: bool):
        self._x = x
        self._y = y

        self._color = (0, 255, 0) if isin else (255, 0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, self._color, (self._x, self._y), 8)
