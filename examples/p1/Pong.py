import pygame
import pygamer
from Ball import Ball


class Pong(pygamer.Game):

    def __init__(self, ball_speed, paddle_speed, ball_radius, window_size=(800, 600)):
        super().__init__(window_size=window_size, bg_color=(255, 255, 255))
        self.w, self.h = window_size
        self.ball = Ball(ball_speed, (150, 25, 200), ball_radius, (self.w // 2, self.h // 2))
        self.objects.append(self.ball)

    def update(self):
        x, y = self.ball.speed
        if self.ball.left < self.window.left:
            self.ball.rect = pygame.rect.Rect(0, self.ball.top, self.ball.width, self.ball.height)
            self.ball.speed = (-x, y)
        elif self.ball.right > self.window.right:
            self.ball.rect = pygame.rect.Rect(self.window.right - self.ball.width, self.ball.top, self.ball.width,
                                              self.ball.height)
            self.ball.speed = (-x, y)
        elif self.ball.top < self.window.top:
            self.ball.rect = pygame.rect.Rect(self.ball.left, 0, self.ball.width, self.ball.height)
            self.ball.speed = (x, -y)
        elif self.ball.bottom > self.window.bottom:
            self.ball.rect = pygame.rect.Rect(self.ball.left, self.window.bottom - self.ball.height, self.ball.width,
                                              self.ball.height)
            self.ball.speed = (x, -y)
        super().update()
