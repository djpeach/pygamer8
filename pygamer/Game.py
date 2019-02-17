import sys
from collections import defaultdict

import pygame

from .Window import Window


class Game:
    def __init__(self, fps=60, window_size=(0, 0), bg_color=(180, 180, 180)):
        self.game_over = False
        self.window = Window(window_size)
        self.fps = fps
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()
        self.handlers = defaultdict(list)
        self.players = []
        self.objects = []
        self.menus = []

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                for handler in self.handlers[event.type]:
                    handler(event)

    def update(self):
        for menu in self.menus:
            while menu.active:
                menu.take_over()
        for obj in self.objects:
            obj.update()
        for player in self.players:
            player.update()

    def draw(self):
        for obj in self.objects:
            obj.draw(self.window.surface)
        for player in self.players:
            player.draw(self.window.surface)

    def run(self):
        while not self.game_over:
            self.window.surface.fill(self.bg_color)

            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.fps)
