from asyncio import sleep
from random import randrange
import pygame, sys
from CPA import CPA
from point import Point

class Screen:
    
    width = height = 800
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Task")
    
    clock = pygame.time.Clock()
    fps = 30

    radius = 399
    
    def __init__(self):
        self._sides = 4
        self._cp = CPA(self._sides).generate(self.radius)
        self._points = []

    def reset(self):
        self.screen.fill((0, 0, 0))
        self._cp = CPA(self._sides).generate(self.radius)
        self._cp.draw(self.screen)

        for p in self._points:
            p.draw(self.screen)


    def run(self):
        self._cp.draw(self.screen)
        while True:
            pygame.display.flip()
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif pygame.mouse.get_pressed()[0]:
                    self.reset()
                    
                elif pygame.mouse.get_pressed()[1]:
                    x, y = pygame.mouse.get_pos()
                    Point(x, y, self._cp.is_in((x, y))).draw(self.screen)

                elif pygame.mouse.get_pressed()[2]:
                    self._sides += 1
                    self.reset()


    