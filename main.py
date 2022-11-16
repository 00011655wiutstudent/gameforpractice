import pygame
import time
from pygame.locals import *

if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((1000, 500))
    surface.fill((255, 255, 255))

    block = pygame.image.load()

    pygame.display.update()

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_q:
                    run = False

            elif event.type == QUIT:
                run = False



