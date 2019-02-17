import pygame
import pygamer


class PongPlayer(pygamer.Player):
    def __init__(self, paddle, score=0, name=""):
        super().__init__(score)
        self.paddle = paddle
        self.objects = [paddle]
        pygame.font.init()
        self.font = pygame.font.SysFont("Sans Serif", 30, bold=True)
        self.name = name

    def draw(self, surface_to_draw_on):
        score_label = self.font.render("{}".format(self.score), False, (0, 0, 0))
        super().draw(surface_to_draw_on)
        surface_to_draw_on.blit(score_label, (self.paddle.left, 25))
