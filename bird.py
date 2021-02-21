import pygame
import os
from settings import *

class Bird:

    def __init__(self):
        self.x = BIRD_X
        self.y = BIRD_Y
        self.size = BIRD_SIZE
        self.color = YELLOW


    def draw(self, win: pygame.Surface) -> None:
        pygame.draw.circle(win, self.color, (self.x, self.y), self.size)


