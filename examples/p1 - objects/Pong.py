import pygame
from src import Game
from examples.basic.Ball import Ball

class Pong(Game):
    def __init__(self, ball_speed, paddle_speed, ball_radius, window_size=(800, 600)):
        super().__init__(window_size=window_size, bg_color=(255, 255, 255))

        self.ball = Ball(ball_speed, (150, 25, 200), ball_radius, (self.window.width // 2, self.window.height // 2))
        self.objects.append(self.ball)

    def update(self):
        x, y = self.ball.speed
        if self.ball.left < self.window.left:
            self.ball.rect = pygame.rect.Rect(0, self.ball.top, self.ball.width, self.ball.height)
            self.ball.speed = (-x, y)
        elif self.ball.right > self.window.right:
            self.ball.rect = pygame.rect.Rect(self.window.right - self.ball.width, self.ball.top, self.ball.width, self.ball.height)
            self.ball.speed = (-x, y)
        elif self.ball.top < self.window.top:
            self.ball.rect = pygame.rect.Rect(self.ball.left, 0, self.ball.width, self.ball.height)
            self.ball.speed = (x, -y)
        elif self.ball.bottom > self.window.bottom:
            self.ball.rect = pygame.rect.Rect(self.ball.left, self.window.bottom - self.ball.height, self.ball.width, self.ball.height)
            self.ball.speed = (x, -y)
        super().update()

# size = width, height = 320, 240
# speed = [2, 2]
# black = 0, 0, 0
#
# screen = pygame.display.set_mode(size)
#
# ball = pygame.image.load("intro_ball.gif")
# ballrect = ball.get_rect()
#
# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: sys.exit()
#
#     ballrect = ballrect.move(speed)
#     if ballrect.left < 0 or ballrect.right > width:
#         speed[0] = -speed[0]
#     if ballrect.top < 0 or ballrect.bottom > height:
#         speed[1] = -speed[1]
#
#     screen.fill(black)
#     screen.blit(ball, ballrect)
#     pygame.display.flip()
