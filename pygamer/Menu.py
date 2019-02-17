import pygame
import sys

from collections import defaultdict

class Menu:
    def __init__(self, screen, fps=15):
        self.active = False
        self.screen = screen
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.handlers = defaultdict(list)
        self.objects = []

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                for handler in self.handlers[event.type]:
                    handler(event)


    def update(self):
        for object in self.objects:
            object.update()

    def draw(self):
        for object in self.objects:
            object.draw(self.screen.surface)

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def take_over(self):
        self.screen.surface.fill((255, 0, 0))
        self.handle_events()
        self.update()
        self.draw()

        pygame.display.update()
        self.clock.tick(self.fps)
