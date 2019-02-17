import pygame
from .Object import Object


class Button(Object):
    def __init__(self, rect, color=(180, 180, 180), text=""):
        super().__init__(rect)
        self.color = color
        self.text = text

    def draw(self, surface_to_draw_on):
        pygame.draw.rect(surface_to_draw_on, self.color, self.rect)
