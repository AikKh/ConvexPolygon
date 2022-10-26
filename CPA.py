import pygame
from math import cos, pi, sin
from random import random, randrange

class Polygon:

    def __init__(self):
        self._cors = []

    def is_in(self, point: tuple[int, int]):
        area = 0
        s_area = int(self.self_area())
        l = len(self._cors)

        for i in range(l):
            f = self._cors[i]
            s = self._cors[(i + 1) % l]

            area += Polygon.area(f, s, point)

        area = int(area)
        return area == s_area

    def self_area(self):
        n = len(self._cors)
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += self._cors[i][0] * self._cors[j][1]
            area -= self._cors[j][0] * self._cors[i][1]

        area = abs(area) / 2.0
        return area

    def area(p1: tuple[int, int], p2: tuple[int, int], p3: tuple[int, int]):
        return abs((p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) / 2.0)


    def draw(self, screen):
        l = len(self._cors)

        for i in range(l):
            pygame.draw.circle(screen, (100, 255, 200), self._cors[i], 6)
            pygame.draw.line(screen, (255, 0, 0), self._cors[i], self._cors[(i + 1) % l], 3)


class CPA:

    def __init__(self, sides: int):
        self._sides = sides

    def generate(self, radius: int):
        angles = [random() * pi * 2 for _ in range(self._sides)]
        angles.sort()
        
        r = randrange(radius // 3, radius)
        cp = Polygon()

        for a in angles:
            sx = cos(a) * r + radius
            sy = sin(a) * r + radius

            cp._cors.append((sx, sy))

        return cp