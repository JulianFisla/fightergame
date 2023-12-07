import sys
import pygame
from pygame.locals import *

attack = False


def process_event(event, player1, player2):
    global attack
    key_down = None
    if event is not None and event.type == QUIT:
        pygame.quit()
        sys.exit()
    elif event is not None and event.type == MOUSEBUTTONDOWN:
        pass
    elif event is not None and event.type == KEYDOWN:
        key_down = event

    keys = pygame.key.get_pressed()

    if keys[K_SPACE] and keys[K_d] and player1.grounded and not player1.attack:
        player1.state = "jumping right"
        attack = True

    elif keys[K_SPACE] and keys[K_a] and player1.grounded and not player1.attack:
        player1.state = "jumping left"
        attack = True
    elif keys[K_SPACE] and player1.grounded and not player1.attack:
        player1.state = "jumping up"
    elif keys[K_w]:
        pass
        # player1.state = "jumping up"

    elif event is not None and event.type == KEYDOWN and keys[K_RIGHT] and not player1.attack and player1.grounded and not attack:

        player1.attack = True
        player1.light_right_animation_clock = 0
        player1.state = "light right"
        player1.facing = "right"
        attack = True

    elif event is not None and event.type == KEYDOWN and keys[K_LEFT] and not player1.attack and player1.grounded and not attack:

        player1.attack = True
        player1.light_left_animation_clock = 0
        player1.state = "light left"
        player1.facing = "left"
        attack = True

    elif keys[K_a] and not player1.attack:

        player1.state = "walking left"
        player1.facing = "left"
    elif keys[K_s] and not player1.attack:
        pass
        # player1.state = "crouching"
    elif keys[K_d] and not player1.attack:

        player1.state = "walking right"
        player1.facing = "right"

    elif player1.attack:
        if player1.facing == "right":
            player1.state = "light right"
        elif player1.facing == "left":
            player1.state = "light left"

    else:
        player1.state = "standing"

    if event is not None and event.type == KEYUP:
        if event.key == K_RIGHT or event.key == K_LEFT:
            attack = False

    # print(attack)
    # if event is not None and event.type == KEYUP:
    #     if event.key in (K_RIGHT, K_LEFT):
    #         dont_attack = False
    #     else:
    #         dont_attack = True
