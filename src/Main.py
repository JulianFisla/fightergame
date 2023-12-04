import pygame

from src import EventHandler
from src.Player1 import Player1
from src.Player2 import Player2

from PIL import Image

# Colours
background = []
background_animation_tick = 0

background_offset_x = 0
background_offset_y = 0

# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('2D Fighter')

player1 = Player1(100, 520, 500, 520, 100, 7)
player2 = Player2(0, 0, 0, 0, 100, 5)

player1_start_x = player1.x
player1_start_y = player1.y


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
        image = standing_left[i]

        flipped_image = pygame.transform.flip(image, True, False)

        standing_right.append(flipped_image)

    player1.images["standing_right"] = standing_right

    running_left = []

    for i in range(7):
        # Load the image into a Surface
        image = pygame.image.load("../assets/sprites/running_left_" + str(i + 1) + ".png")

        # Calculate the new size
        new_size = (image.get_width() * 4, image.get_height() * 4)

        # Scale the image
        scaled_image = pygame.transform.scale(image, new_size)

        running_left.append(scaled_image)

    player1.images["running_left"] = running_left

    running_right = []

    for i in range(8):
        # Load the image into a Surface
        image = pygame.image.load("../assets/sprites/running_right_" + str(i + 1) + ".png")

        # Calculate the new size
        new_size = (image.get_width() * 4, image.get_height() * 4)

        # Scale the image
        scaled_image = pygame.transform.scale(image, new_size)

        running_right.append(scaled_image)

    player1.images["running_right"] = running_right

    for i in range(9):
        # Load the image into a Surface
        image = pygame.image.load("../assets/background/background_" + str(i + 1) + ".png")

        # Calculate the new size
        new_size = (image.get_width() * 0.75, image.get_height() * 0.75)

        # Scale the image
        scaled_image = pygame.transform.scale(image, new_size)

        background.append(scaled_image)


def update_game_state():
    global player1, player2

    # Get inputs
    for event in pygame.event.get():
        EventHandler.process_event(event, player1, player2)

    player1.update()
    player2.update()


def update_background():
    global background_animation_tick, background_offset_x, background_offset_y

    if background_animation_tick == 10000:
        background_animation_tick = 0

    background_animation_tick += 1

    background_animation_clock = background_animation_tick % 54

    background_offset_x = -(player1.x - player1_start_x) * 1.5 - 380
    background_offset_y = -(player1.y - player1_start_y) * 1.5

    background_offset = (background_offset_x, background_offset_y)

    if background_animation_clock < 6:
        WINDOW.blit(background[0], background_offset)
    elif background_animation_clock < 12:
        WINDOW.blit(background[1], background_offset)
    elif background_animation_clock < 18:
        WINDOW.blit(background[2], background_offset)
    elif background_animation_clock < 24:
        WINDOW.blit(background[3], background_offset)
    elif background_animation_clock < 30:
        WINDOW.blit(background[4], background_offset)
    elif background_animation_clock < 36:
        WINDOW.blit(background[5], background_offset)
    elif background_animation_clock < 42:
        WINDOW.blit(background[6], background_offset)
    elif background_animation_clock < 48:
        WINDOW.blit(background[7], background_offset)
    elif background_animation_clock < 54:
        WINDOW.blit(background[8], background_offset)


def render_game():
    update_background()
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
