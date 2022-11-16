import pygame
import time
from pygame.locals import *
import time

SIZE = 40

class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [SIZE] *length
        self.y = [SIZE] *length
        self.direction = "right"
    def draw(self):
        self.parent_screen.fill((255, 255, 255))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move_up(self):
        self.direction = "up"
    def move_down(self):
        self.direction = "down"
    def move_left(self):
        self.direction = "left"
    def move_right(self):
        self.direction = "right"
    def walk(self):
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        if self.direction == "right":
            self.x[0] += SIZE
        if self.direction == "left":
            self.x[0] -= SIZE
        if self.direction == "down":
            self.y[0] += SIZE
        if self.direction == "up":
            self.y[0] -= SIZE
        self.draw()
class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 800))
        self.surface.fill((255, 255, 255))
        self.snake = Snake(self.surface, 6)
        self.snake.draw()
    def run(self):
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        run = False
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                elif event.type == QUIT:
                    run = False

            self.snake.walk()
            time.sleep(0.5)


if __name__ == "__main__":
    game = Game()
    game.run()