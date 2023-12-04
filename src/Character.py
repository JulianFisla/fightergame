from abc import ABC


class Character(ABC):

    x: int
    y: int
    screen_x: int
    screen_y: int
    health: int
    speed: int
    images: dict[str, list]
    state: str
    animation_tick: int
    facing: str

    def __init__(self, screen_x, screen_y, x, y, health, speed):
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.x = x
        self.y = y
        self.health = health
        self.speed = speed
        self.state = "standing"
        self.images = {}
        self.animation_tick = 0
        self.facing = "right"

    def update(self):
        raise NotImplementedError

    def draw(self, window):
        raise NotImplementedError
