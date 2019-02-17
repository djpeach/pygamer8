import pygame
import pygamer
import time


class Ball(pygamer.Object):
    def __init__(self, speed, color, radius, center_position):
        rect = pygame.rect.Rect(center_position[0] - radius, center_position[1] - radius, radius * 2, radius * 2)
        super().__init__(rect, speed)
        self.color = color
        self.radius = radius
        self.diameter = radius * 2
        self.initital_position = center_position
        self.scored = False

    def check_bounds(self, screen):
        x, y = self.speed
        if self.left < screen.left:
            self.rect = pygame.rect.Rect(0, self.top, self.width, self.height)
            self.speed = (0, 0)
            self.scored = True
        elif self.right > screen.right:
            self.rect = pygame.rect.Rect(screen.right - self.width, self.top, self.width, self.height)
            self.speed = (0, 0)
            self.scored = True
        elif self.top < screen.top:
            self.rect = pygame.rect.Rect(self.left, 0, self.width, self.height)
            self.speed = (x, -y)
        elif self.bottom > screen.bottom:
            self.rect = pygame.rect.Rect(self.left, screen.bottom - self.height, self.width, self.height)
            self.speed = (x, -y)

    def check_paddle_collisions(self, paddle, reset_x):
        x, y = self.speed
        if paddle.rect.colliderect(self):
            if abs(x) < 15:
                x *= 1.3
            self.rect = pygame.rect.Rect(reset_x, self.top, self.width, self.height)
            self.speed = (-x, y)

    def draw(self, surface_to_draw_on):
        pygame.draw.circle(surface_to_draw_on, self.color, (self.rect.x + self.radius, self.rect.y + self.radius), self.radius)
