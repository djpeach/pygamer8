import pygame
import pygamer


class Paddle(pygamer.Object):

    root_speed = 0

    def __init__(self, rect, move_keys):
        super().__init__(rect)
        self.up_key, self.down_key = move_keys
        self.rect = rect
        self.color = (80, 134, 240)
        self.reset_x = 0

    def set_reset(self, x):
        self.reset_x = x

    def move_handler(self, event):
        if event.key == self.up_key:
            self.speed = (0, -Paddle.root_speed)
        elif event.key == self.down_key:
            self.speed = (0, Paddle.root_speed)

    def stop_moving(self, event):
        if event.key in [self.up_key, self.down_key]:
            self.speed = (0, 0)

    def check_bounds(self, screen):
        if self.top + self.speed[1] < screen.top:
            self.rect = pygame.rect.Rect(self.left, screen.top, self.width, self.height)
            self.speed = (0, 0)
        elif self.bottom + self.speed[1] > screen.bottom:
            self.rect = pygame.rect.Rect(self.left, screen.bottom - self.height, self.width, self.height)
            self.speed = (0, 0)

    def draw(self, surface_to_draw_on):
        pygame.draw.rect(surface_to_draw_on, self.color, self.rect)
