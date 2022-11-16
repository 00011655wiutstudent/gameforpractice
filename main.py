import pygame
import time
from pygame.locals import *
import time
import random

SIZE = 40


class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(0, 24) * SIZE
        self.y = random.randint(0, 14) * SIZE


class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = "right"

    def draw(self):
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def move_up(self):
        self.direction = "up"

    def move_down(self):
        self.direction = "down"

    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"

    def walk(self):
        for i in range(self.length - 1, 0, -1):
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
        self.surface = pygame.display.set_mode((1000, 600))
        self.surface.fill((255, 255, 255))
        self.snake = Snake(self.surface, 7)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
        pygame.mixer.init()

    # snake eats apple
    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def play_music(self):
        pygame.mixer.music.load("resources/bg_music_1.mp3")
        pygame.mixer.music.play()
    def render_backgroud(self):
        bg = pygame.image.load("resources/background.jpg")
        self.surface.blit(bg, (0, 0))
    def play_sound(self, sound):
        sound = pygame.mixer.Sound(f"resources/{sound}.mp3")
        pygame.mixer.Sound.play(sound)

    def play(self):
        self.render_backgroud()
        self.play_music()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.play_sound("crash")
            self.apple.move()
            self.snake.increase_length()
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                sound_crash = pygame.mixer.Sound("resources/1_snake_game_resources_crash.mp3")
                pygame.mixer.Sound.play(sound_crash)
                print("Game Over")
                exit(0)

    def display_score(self):
        font = pygame.font.SysFont("aria", 30)
        score = font.render(f"Score:{self.snake.length}", True, (200, 200, 200))
        self.surface.blit(score, (800, 10))

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
            self.play()

            time.sleep(0.3)


if __name__ == "__main__":
    game = Game()
    game.run()
