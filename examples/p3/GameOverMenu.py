import pygame
import sys
import pygamer
# from main import run as restart


class GameOverMenu(pygamer.Menu):

    winner = None

    def __init__(self, screen_to_take_over, game):
        super().__init__(screen_to_take_over)
        pygame.font.init()
        self.big_font = pygame.font.SysFont("Sans Serif", 50, True)
        self.font = pygame.font.SysFont("Sans Serif", 30, True)
        self.add_handlers()
        self.game = game

    def draw(self):
        super().draw()
        title = self.big_font.render("Game Over, {} wins!".format(GameOverMenu.winner), False, (0, 0, 0))
        label = self.font.render("Press Blue to play again", False, (0, 0, 0))
        self.screen.surface.blit(title, (200, 200))
        self.screen.surface.blit(label, (225, 280))

    def add_handlers(self):

        def button_handler(event):
            if event.key == pygame.K_SLASH:
                pygame.quit()
                sys.exit()
            elif event.key in [pygame.K_r, pygame.K_z]:
                for player in self.game.players:
                    paddle_h = player.paddle.rect.height
                    paddle_y = self.game.window.centery - (paddle_h // 2)
                    player.paddle.rect = pygame.rect.Rect(player.paddle.rect.left, paddle_y, player.paddle.rect.width, player.paddle.rect.height)
                    player.paddle.speed = (0, 0)
                    player.score = 0
                self.deactivate()

        self.handlers[pygame.KEYDOWN].append(button_handler)


