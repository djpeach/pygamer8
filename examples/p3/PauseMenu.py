import pygame
import sys
import pygamer


class PauseMenu(pygamer.Menu):
    def __init__(self, screen_to_take_over):
        super().__init__(screen_to_take_over)
        self.add_buttons()

    def add_buttons(self):
        continue_rect = pygame.rect.Rect(200, 400, 100, 50)
        continue_button = pygamer.Button(continue_rect, color=(50, 255, 50), text="Continue")
        quit_rect = pygame.rect.Rect(500, 400, 100, 50)
        quit_button = pygamer.Button(quit_rect, color=(255, 50, 50), text="Quit")
        self.objects += [continue_button, quit_button]

        def button_handler(event):
            if event.key == pygame.K_SLASH:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_p or event.key == pygame.K_n:
                self.deactivate()

        self.handlers[pygame.KEYDOWN].append(button_handler)
