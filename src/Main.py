import pygame

from src import EventHandler
from src.Player1 import Player1
from src.Player2 import Player2

# Colours
BACKGROUND = (255, 255, 255)

# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('2D Fighter')

player1 = Player1(0, 0, 100, 5)
player2 = Player2(0, 0, 100, 5)


def load_images():
    pass


def update_game_state():
    global player1, player2

    # Get inputs
    for event in pygame.event.get():
        EventHandler.process_event(event, player1, player2)

    player1.update()
    player2.update()


def render_game():
    WINDOW.fill(BACKGROUND)
    pygame.display.update()


def start_game():

    load_images()


def game_loop():
    start_game()

    # The main game loop
    while True:
        # Update game state
        update_game_state()

        # Render elements of the game
        render_game()
        fpsClock.tick(FPS)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game_loop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
