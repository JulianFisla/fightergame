import sys
import pygame
from pygame.locals import *

attack = False
jump_attack = False


def process_event(event, player1, player2):
    global attack, jump_attack

    # if player has quit the application
    if event is not None and event.type == QUIT:
        pygame.quit()
        sys.exit()
    elif event is not None and event.type == MOUSEBUTTONDOWN:
        pass

    # store keys pressed
    keys = pygame.key.get_pressed()

    # what direction the player is moving in
    if keys[K_a] and keys[K_d]:
        player1.moving = "none"
    elif keys[K_a]:
        player1.moving = "left"
    elif keys[K_d]:
        player1.moving = "right"
    else:
        player1.moving = "none"

    if keys[K_SPACE] and keys[K_d] and player1.grounded and not player1.attack and not jump_attack:
        # print("key hit right")
        player1.state = "jumping right"
        attack = True

    elif keys[K_SPACE] and keys[K_a] and player1.grounded and not player1.attack and not jump_attack:
        # print("key hit left")
        player1.state = "jumping left"
        attack = True
    elif keys[K_SPACE] and player1.grounded and not player1.attack and not jump_attack:
        player1.state = "jumping up"
    elif keys[K_w]:
        pass
        # player1.state = "jumping up"

    # attacking jumping left
    elif (event is not None and event.type == KEYDOWN
          and keys[K_LEFT] and not player1.attack and not player1.grounded and not jump_attack):

        # print("key hit left")
        player1.jump_attack = True
        player1.jumping_attack_left_animation_clock = 0
        player1.state = "jumping attack left"
        player1.facing = "left"
        jump_attack = True

    # attacking jumping right
    elif (event is not None and event.type == KEYDOWN
          and keys[K_RIGHT] and not player1.attack and not player1.grounded and not jump_attack):

        # print("key hit right")
        player1.jump_attack = True
        player1.jumping_attack_right_animation_clock = 0
        player1.state = "jumping attack right"
        player1.facing = "right"
        jump_attack = True

    elif (event is not None and event.type == KEYDOWN
          and keys[K_RIGHT] and not player1.attack and player1.grounded and not attack):

        player1.attack = True
        player1.light_right_animation_clock = 0
        player1.state = "light right"
        player1.facing = "right"
        attack = True

        if player1.light_attack_option == 1:
            player1.light_attack_option = 2
        elif player1.light_attack_option == 2:
            player1.light_attack_option = 1

    elif (event is not None and event.type == KEYDOWN
          and keys[K_LEFT] and not player1.attack and player1.grounded and not attack):

        player1.attack = True
        player1.light_left_animation_clock = 0
        player1.state = "light left"
        player1.facing = "left"
        attack = True

        if player1.light_attack_option == 1:
            player1.light_attack_option = 2
        elif player1.light_attack_option == 2:
            player1.light_attack_option = 1

    elif keys[K_a] and not player1.attack and not jump_attack:

        player1.state = "walking left"
        player1.facing = "left"
    elif keys[K_s] and not player1.attack:
        pass
        # player1.state = "crouching"
    elif keys[K_d] and not player1.attack and not jump_attack:

        player1.state = "walking right"
        player1.facing = "right"

    elif player1.attack:
        if player1.facing == "right":
            player1.state = "light right"
        elif player1.facing == "left":
            player1.state = "light left"
    elif player1.jump_attack:
        if player1.facing == "right":
            player1.state = "jumping attack right"
        elif player1.facing == "left":
            player1.state = "jumping attack left"

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
