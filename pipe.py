import pygame
from settings import *
from random import randrange

class Pipe:

    def __init__(self, prevX):
        self.x = prevX + randrange(PIPE_WIDTH, 2 * PIPE_WIDTH) + PIPE_WIDTH
        self.width = PIPE_WIDTH
        self.height = randrange(PIPE_HEIGHT_MIN, PIPE_HEIGHT_MAX)
        self.y = PIPE_MAX - self.height
        self.gap = randrange(PIPE_GAP_MIN, PIPE_GAP_MAX)
        self.refUpper = PIPE_MAX - (self.height + self.gap)
        self.color = YELLOW

    def draw(self, win: pygame.Surface) -> None:
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, self.color, (self.x, PIPE_MIN, self.width, self.refUpper))


    def isOnScreen(self) -> bool:
        return (self.x + self.width) > 0

    def move(self) -> None:
        self.x -= GAME_SPEED

    def getX(self) -> int:
        return self.x

    def load_images(self):
        pass