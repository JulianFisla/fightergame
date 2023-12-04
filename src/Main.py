import pygame

from src import EventHandler
from src.Player1 import Player1
from src.Player2 import Player2

from PIL import Image

# Colours
BACKGROUND = (255, 255, 255)

# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('2D Fighter')

player1 = Player1(0, 0, 100, 5)
player2 = Player2(0, 0, 100, 5)


def load_images():

    standing_left = []

    for i in range(4):
        # Load the image into a Surface
        image = pygame.image.load("../assets/sprites/standing_left_" + str(i + 1) + ".png")

        # Calculate the new size
        new_size = (image.get_width() * 4, image.get_height() * 4)

        # Scale the image
        scaled_image = pygame.transform.scale(image, new_size)

        standing_left.append(scaled_image)

    player1.images["standing_left"] = standing_left

    standing_right = []

    for i in range(4):
        # Load the image into a Surface
        image = pygame.image.load("../assets/sprites/standing_right_" + str(i + 1) + ".png")

        # Calculate the new size
        new_size = (image.get_width() * 4, image.get_height() * 4)

        # Scale the image
        scaled_image = pygame.transform.scale(image, new_size)

        standing_left.append(scaled_image)

    player1.images["standing_right"] = standing_right

    running_left = []

    for i in range(7):
        # Load the image into a Surface
        image = pygame.image.load("../assets/sprites/running_left_" + str(i + 1) + ".png")

        # Calculate the new size
        new_size = (image.get_width() * 4, image.get_height() * 4)

        # Scale the image
        scaled_image = pygame.transform.scale(image, new_size)

        standing_left.append(scaled_image)

    player1.images["running_left"] = running_left

    running_right = []

    for i in range(8):
        # Load the image into a Surface
        image = pygame.image.load("../assets/sprites/running_right_" + str(i + 1) + ".png")

        # Calculate the new size
        new_size = (image.get_width() * 4, image.get_height() * 4)

        # Scale the image
        scaled_image = pygame.transform.scale(image, new_size)

        standing_left.append(scaled_image)

    player1.images["running_right"] = running_right


def update_game_state():
    global player1, player2

    # Get inputs
    for event in pygame.event.get():
        EventHandler.process_event(event, player1, player2)

    player1.update()
    player2.update()


def render_game():
    global player1, player2

    WINDOW.fill(BACKGROUND)
    player1.draw(WINDOW)
    player2.draw(WINDOW)
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
