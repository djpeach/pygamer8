import pygame


class Window:
    def __init__(self, size):
        self.surface = pygame.display.set_mode(size)

    @property
    def left(self):
        return self.surface.get_rect().left

    @property
    def right(self):
        return self.surface.get_rect().right

    @property
    def top(self):
        return self.surface.get_rect().top

    @property
    def bottom(self):
        return self.surface.get_rect().bottom

    @property
    def width(self):
        return self.surface.get_rect().width

    @property
    def height(self):
        return self.surface.get_rect().height

    @property
    def center(self):
        return self.surface.get_rect().center

    @property
    def centerx(self):
        return self.surface.get_rect().centerx

    @property
    def centery(self):
        return self.surface.get_rect().centery

    def set_caption(self, caption):
        self.caption = caption
        pygame.display.set_caption(caption)
