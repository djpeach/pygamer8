class Object:
    def __init__(self, rect, speed=(0, 0)):
        self.rect = rect
        self.speed = speed

    @property
    def left(self):
        return self.rect.left

    @property
    def right(self):
        return self.rect.right

    @property
    def top(self):
        return self.rect.top

    @property
    def bottom(self):
        return self.rect.bottom

    @property
    def width(self):
        return self.rect.width

    @property
    def height(self):
        return self.rect.height

    @property
    def center(self):
        return self.rect.center

    @property
    def centerx(self):
        return self.rect.centerx

    @property
    def centery(self):
        return self.rect.centery

    def move(self, speed):
        dx, dy = speed
        self.rect = self.rect.move(dx, dy)

    def update(self):
        if self.speed != [0, 0]:
            self.move(self.speed)

    def draw(self, surface_to_draw_on):
        pass
