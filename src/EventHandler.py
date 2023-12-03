import sys
import pygame
from pygame.locals import *


def process_event(event, player1, player2):
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == MOUSEBUTTONDOWN:
        pass
    keys = pygame.key.get_pressed()
    if keys[K_w]:
        player1.state = "jumping up"
    elif keys[K_a]:
        player1.state = "walking left"
    elif keys[K_s]:
        player1.state = "crouching"
    elif keys[K_d]:
        player1.state = "walking right"
    else:
        player1.state = "standing"
