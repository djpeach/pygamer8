import pygame

from .Object import Object


class Button(Object):
    def __init__(self, rect, color=(180, 180, 180), text=""):
        super().__init__(rect)
        pygame.font.init()
        self.color = color
        self.text = text
        self.font = pygame.font.SysFont("Sans Serif", 20, bold=True)

    def draw(self, surface_to_draw_on):
        text = self.font.render(self.text, False, (0, 0, 0))
        pygame.draw.rect(surface_to_draw_on, self.color, self.rect)
        surface_to_draw_on.blit(text, (self.rect.x + 10, self.rect.y + 10))
