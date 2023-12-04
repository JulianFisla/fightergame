from abc import ABC


class Character(ABC):

    x: int
    y: int
    health: int
    speed: int
    images: dict[str, list]
    state: str

    def __init__(self, x, y, health, speed):
        self.x = x
        self.y = y
        self.health = health
        self.speed = speed
        self.state = "standing"
        self.images = {}

    def update(self):
        raise NotImplementedError

    def draw(self):
        raise NotImplementedError
