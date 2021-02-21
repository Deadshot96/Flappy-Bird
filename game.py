import pygame
import os
import time
import math
from settings import *


class Game:
    
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.win = None
        self.clock = None
        self.fps = FPS

    def draw(self, win: pygame.Surface) -> None:
        win.fill(MID_BLACK)

    def game_init(self):

        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Flappy Bird Developer")

        self.clock = pygame.time.Clock()



    def run(self):
        
        self.game_init()

        run = True
        while run:
            self.clock.tick(self.fps)
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    x, y = pos
                    print(x, y, sep='\t')
                    
            self.draw(self.win)

        pygame.font.quit()
        pygame.quit()


if __name__ == "__main__":
    X = Game()
    X.run()
