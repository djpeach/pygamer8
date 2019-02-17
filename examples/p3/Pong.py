import pygame
import pygamer
from PauseMenu import PauseMenu
from GameOverMenu import GameOverMenu
from Ball import Ball
from Paddle import Paddle
from PongPlayer import PongPlayer


class Pong(pygamer.Game):

    def __init__(self, ball_speed, paddle_speed, ball_radius, window_size=(0, 0)):
        super().__init__(window_size=window_size, bg_color=(255, 255, 255))
        self.paddle_speed = paddle_speed
        Paddle.root_speed = paddle_speed
        self.w, self.h = window_size
        self.initial_ball_speed = ball_speed
        self.ball = Ball(ball_speed, (150, 25, 200), ball_radius, (self.w // 2, self.h // 2))
        self.objects.append(self.ball)
        self.add_menus()
        self.add_players()
        self.game_over_screen = GameOverMenu(self.window, self)
        self.menus = [self.game_over_screen]

    def update(self):
        if self.ball.scored:
            if self.ball.left < self.window.centerx:
                self.players[1].scored()
            else:
                self.players[0].scored()

            self.ball.rect = pygame.rect.Rect(self.window.centerx - self.ball.radius, self.window.centery - self.ball.radius, self.ball.radius * 2, self.ball.radius * 2)
            self.ball.speed = self.initial_ball_speed
            self.ball.scored = False

        self.ball.check_bounds(self.window)
        for player in self.players:
            if player.score >= 3:
                GameOverMenu.winner = player.name
                self.game_over_screen.activate()
            player.paddle.check_bounds(self.window)
            self.ball.check_paddle_collisions(player.paddle, player.paddle.reset_x)
        super().update()

    def add_menus(self):
        pause_menu = PauseMenu(self.window)
        self.menus.append(pause_menu)

        def menu_handler(event):
            if event.key == pygame.K_SLASH:
                pause_menu.activate()

        self.handlers[pygame.KEYDOWN].append(menu_handler)

    def add_players(self):
        paddle_w = 50
        paddle_h = 200
        paddle_y = self.window.centery - (paddle_h // 2)
        paddle_1 = Paddle(pygame.rect.Rect(100, paddle_y, paddle_w, paddle_h), (pygame.K_w, pygame.K_s))
        paddle_1.set_reset(paddle_1.right)
        paddle_2 = Paddle(pygame.rect.Rect(self.window.right - 100 - paddle_w, paddle_y, paddle_w, paddle_h), (pygame.K_i, pygame.K_k))
        paddle_2.set_reset(paddle_2.left - (self.ball.radius * 2))

        for paddle in [paddle_1, paddle_2]:
            self.handlers[pygame.KEYDOWN].append(paddle.move_handler)
            self.handlers[pygame.KEYUP].append(paddle.stop_moving)

        player_1 = PongPlayer(paddle_1, score=0, name="Player 1")
        player_2 = PongPlayer(paddle_2, score=-1, name="Player 2")

        self.players += [player_1, player_2]

    def reset(self):
        self.__init__(self.initial_ball_speed, self.paddle_speed, self.ball.radius, window_size=(self.w, self.h))
