class Player:
    def __init__(self, score=0):
        self.score = score
        self.objects = []

    def update(self):
        for obj in self.objects:
            obj.update()

    def draw(self, surface_to_draw_on):
        for obj in self.objects:
            obj.draw(surface_to_draw_on)

    def scored(self, points=1):
        self.score += points
