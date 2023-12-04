from src.Character import Character


class Player1(Character):

    def __init__(self, x, y, health, speed):
        super().__init__(x, y, health, speed)

    def update(self):
        pass
        # print("Player 1:", self.state)

    def draw(self):
        pass
