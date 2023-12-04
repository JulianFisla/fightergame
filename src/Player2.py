from src.Character import Character


class Player2(Character):

    def __init__(self, screen_x, screen_y, x, y, health, speed):
        super().__init__(screen_x, screen_y, x, y, health, speed)

    def update(self):
        pass
        # print("Player 2:", self.state)

    def draw(self, window):
        pass

