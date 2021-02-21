import pygame
import os
from settings import *

class Bird:

    def __init__(self):
        self.x = BIRD_X
        self.y = BIRD_Y
        self.size = BIRD_SIZE
        self.color = YELLOW
        self.gravity = 0.25
        self.vy = 0


    def draw(self, win: pygame.Surface) -> None:
        self.move()
        pygame.draw.circle(win, self.color, (self.x, self.y), self.size)

    def move(self):
        self.vy += self.gravity
        self.y += self.vy
        self.y = int(self.y)

    def jump(self):
        self.vy = -8

