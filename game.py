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
        self.background = None

    def draw(self, win: pygame.Surface) -> None:
        win.fill(MID_BLACK)
        
        win.blit(self.background, (0, 0))
        pygame.display.update()

    def load_images(self):
        self.background = pygame.image.load(os.path.join(ASSET_DIR, 'background-day.png')).convert()
        self.background = pygame.transform.scale(self.background, (self.width, self.height))

    def game_init(self):

        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Flappy Bird Developer")

        self.clock = pygame.time.Clock()

        self.load_images()

    def quit(self):
        pygame.font.quit()
        pygame.quit()



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
                    col = self.win.get_at(pos)
                    print(x, y, col, sep='\t')
                    
            self.draw(self.win)

        self.quit()


if __name__ == "__main__":
    X = Game()
    X.run()
