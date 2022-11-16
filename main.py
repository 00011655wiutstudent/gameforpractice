import pygame
import time
from pygame.locals import *

if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((1000, 500))
    block = pygame.image.load("resources/block.jpg").convert()
    block_x = 100
    block_y = 100
    def draw_block():
        surface.fill((255, 255, 255))
        surface.blit(block, (block_x, block_y ))
        pygame.display.flip()


    pygame.display.update()


    run = True

    while run:
        draw_block()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_q:
                    run = False
                if event.key == K_UP:
                    block_y -=10
                if event.key == K_DOWN:
                    block_y +=10
                if event.key == K_RIGHT:
                    block_x +=10
                if event.key == K_LEFT:
                    block_x -=10

            elif event.type == QUIT:
                run = False



