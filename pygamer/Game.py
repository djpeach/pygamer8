import pygame
import sys
from collections import defaultdict
from .Window import Window

class Game:
    def __init__(self, fps=120, window_size=(0, 0), bg_color=(180, 180, 180)):
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
        # for menu in self.menus:
        #     while menu.active:
        #         menu.run()
        for object in self.objects:
            object.update()
        # for object in [player.objects for player in self.players]:
        #     object.update()

    def draw(self):
        for object in self.objects:
            object.draw(self.window.surface)
        # for object in [player.objects for player in self.players]:
        #     object.draw(self.window.surface)

    def run(self):
        while not self.game_over:
            self.window.surface.fill(self.bg_color)

            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.fps)
