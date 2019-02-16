import pygame
import sys
import pygamer
from Ball import Ball


screen = pygame.display.set_mode((0, 0))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.quit()
        else:
            screen.fill((100, 143, 12))
            ball = pygame.draw.circle(screen, (35, 190, 214), (100, 100), 20)
            ball = ball.move(ball.centerx + 5, ball.centery + 5)

            pygame.display.update()
            clock.tick(60)




