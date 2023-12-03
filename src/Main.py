import pygame

from src.EventHandler import process_event

# Colours
BACKGROUND = (255, 255, 255)

# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('2D Fighter')


def load_images():
    pass


def update_game_state():
    # Get inputs
    for event in pygame.event.get():
        process_event(event)


def render_game():

    WINDOW.fill(BACKGROUND)
    pygame.display.update()


def game_loop():

    load_images()

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
