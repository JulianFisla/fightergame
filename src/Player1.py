from src.Character import Character


class Player1(Character):

    def __init__(self, x, y, health, speed):
        super().__init__(x, y, health, speed)

    def update(self):
        if self.animation_tick == 60:
            self.animation_tick = 0
        self.animation_tick += 1
        pass
        print("Player 1:", self.animation_tick)

    def draw(self, window):
        if self.state == "standing":
            if self.animation_tick < 15:
                window.blit(self.images["standing_left"][0], (self.x, self.y))
            elif self.animation_tick < 30:
                window.blit(self.images["standing_left"][1], (self.x, self.y))
            elif self.animation_tick < 45:
                window.blit(self.images["standing_left"][2], (self.x, self.y))
            else:
                window.blit(self.images["standing_left"][3], (self.x, self.y))
