import pygame
import time
import random
from enum import Enum
from collections import namedtuple
import numpy as np

pygame.init()

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

green = pygame.Color(80, 255, 80)
pink = pygame.Color(255, 150, 150)
black = pygame.Color(10, 10, 10)
white = pygame.Color(255, 255, 255)
background = pygame.Color(100, 40, 40)

Point = namedtuple('Point', 'x, y')
font = pygame.font.SysFont('comic sans', 30)

BLOCK_SIZE = 20
SPEED = 20

class SnakeGameAI:
    def update_ui(self):
        self.display.fill(background)
        for pt in self.snake:
            pygame.draw.rect(self.display, green, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, green, pygame.Rect(pt.x + 4, pt.y + 4, 12, 12))

        pygame.draw.rect(self.display, pink, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

        text = font.render("Score: " + str(self.score), True, pink)
        self.display.blit(text, [0, 0])
        pygame.display.flip()

    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('snakey snake')
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        self.direction = Direction.RIGHT
        self.head = Point(self.w / 2, self.h / 2)
        self.snake = [self.head,
                      Point(self.head.x - BLOCK_SIZE, self.head.y),
                      Point(self.head.x - (2 * BLOCK_SIZE), self.head.y)]
        self.score = 0
        self.food = None
        self.place_food()
        self.frame_iteration = 0

    def place_food(self):
     x = random.randint(0, (self.w - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
     y = random.randint(0, (self.h - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
     self.food = Point(x, y)
     if self.food in self.snake:
           self.place_food()

    def is_collision(self, pt=None):
      if pt is None:
            pt = self.head
      #snake hitting the wall
      if pt.x > self.w - BLOCK_SIZE or pt.x < 0 or pt.y > self.h - BLOCK_SIZE or pt.y < 0:
          return True
      #snake hitting itself
      if pt in self.snake[1:]:
         return True
      return False

    def play_step(self, action):
            self.frame_iteration += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.move(action)  
            self.snake.insert(0, self.head)
            reward = 0
            game_over = False
            if self.is_collision() or self.frame_iteration > 100 * len(self.snake):
                game_over = True
                reward = -10
                return reward, game_over, self.score
            if self.head == self.food:
                self.score += 1
                reward = 10
                self.place_food()
            else:
                self.snake.pop()
            self.update_ui()
            self.clock.tick(SPEED)
            return reward, game_over, self.score

    def move(self, action):

            anti_clock_wise = [Direction.LEFT, Direction.UP, Direction.RIGHT, Direction.DOWN]
            idx = anti_clock_wise.index(self.direction)
            #straight
            if np.array_equal(action, [1, 0, 0]):
                new_dir = anti_clock_wise[idx]
            #right
            elif np.array_equal(action, [0, 1, 0]):
                next_idx = (idx + 1) % 4
                new_dir = anti_clock_wise[next_idx]  
            #left
            else: 
                next_idx = (idx - 1) % 4
                new_dir = anti_clock_wise[next_idx]  
            self.direction = new_dir

            x = self.head.x
            y = self.head.y
            if self.direction == Direction.RIGHT:
                x += BLOCK_SIZE
            elif self.direction == Direction.LEFT:
                x -= BLOCK_SIZE
            elif self.direction == Direction.DOWN:
                y += BLOCK_SIZE
            elif self.direction == Direction.UP:
                y -= BLOCK_SIZE

            self.head = Point(x, y)

