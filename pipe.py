import pygame
from settings import *
from random import randrange

class Pipe:

    def __init__(self):
        self.x = 80
        self.width = PIPE_WIDTH
        self.height = randrange(PIPE_HEIGHT_MIN, PIPE_HEIGHT_MAX)
        self.y = PIPE_MAX - self.height
        self.gap = PIPE_GAP_MAX # randrange(PIPE_GAP_MIN, PIPE_GAP_MAX)
        self.refUpper = PIPE_MAX - (self.height + self.gap)
        self.color = YELLOW

    def draw(self, win: pygame.Surface) -> None:
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, self.color, (self.x, PIPE_MIN, self.width, self.refUpper))


    def isOnScreen(self) -> bool:
        return (self.x + self.width) > 0