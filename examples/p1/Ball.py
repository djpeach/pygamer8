import pygame
from pygamer import Object

class Ball(Object):
    def __init__(self, speed, color, radius, center_position):
        rect = pygame.rect.Rect(center_position[0] - radius, center_position[1] - radius, radius * 2, radius * 2)
        super().__init__(rect, speed)
        self.color = color
        self.radius = radius
        self.diameter = radius * 2
        self.initital_position = center_position

    def draw(self, surface_to_draw_on):
        pygame.draw.circle(surface_to_draw_on, self.color, (self.rect.x + self.radius, self.rect.y + self.radius), self.radius)
