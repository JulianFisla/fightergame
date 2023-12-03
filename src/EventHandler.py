import sys
import pygame
from pygame.locals import *


def process_event(event):
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == MOUSEBUTTONDOWN:
        pass
    elif event.type == KEYDOWN:
        if event.key == K_w:
            pass
        elif event.key == K_a:
            pass
        elif event.key == K_s:
            pass
        elif event.key == K_d:
            pass
        elif event.key == K_UP:
            pass
        elif event.key == K_LEFT:
            pass
        elif event.key == K_DOWN:
            pass
        elif event.key == K_RIGHT:
            pass
        elif event.key == K_SPACE:
            pass
