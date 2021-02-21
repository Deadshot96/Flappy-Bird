import pygame
import os
import time
import math
from settings import *
from bird import Bird


class Game:
    
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.win = None
        self.clock = None
        self.fps = FPS
        self.backgrounds = []
        self.tickEvent = pygame.USEREVENT
        self.background_index = 0
        self.base = None
        self.baseX = BASE_WIDTH
        self.bird = None

    def draw(self, win: pygame.Surface) -> None:
        win.fill(MID_BLACK)

        index = self.background_index // 10
        win.blit(self.backgrounds[index], (0, 0))
        
        # win.blit(self.base, (0, 0))
        self.draw_base(self.win)
        self.bird.draw(self.win)
        
        pygame.display.update()

    def load_images(self):
        background_day = pygame.image.load(os.path.join(ASSET_DIR, 'background-day.png')).convert()
        background_day = pygame.transform.scale(background_day, (self.width, self.height))
        
        background_night = pygame.image.load(os.path.join(ASSET_DIR, 'background-night.png')).convert()
        background_night = pygame.transform.scale(background_night, (self.width, self.height))

        self.backgrounds = [background_day, background_night]

        self.base = pygame.image.load(os.path.join(ASSET_DIR, 'base.png')).convert()
        self.base = pygame.transform.scale(self.base, (BASE_WIDTH, BASE_HEIGHT))

    def game_init(self):

        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Flappy Bird Developer")

        self.clock = pygame.time.Clock()
        pygame.time.set_timer(self.tickEvent, 1200)

        self.bird = Bird()

        self.load_images()

    def quit(self) -> None:
        pygame.font.quit()
        pygame.quit()

    def draw_base(self, win: pygame.Surface) -> None:
        if self.baseX <= 0:
            self.baseX = BASE_WIDTH

        self.baseX -= 2

        win.blit(self.base, (self.baseX - BASE_WIDTH, self.height - BASE_HEIGHT))
        win.blit(self.base, (self.baseX, self.height - BASE_HEIGHT))


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

                if event.type == self.tickEvent:
                    self.background_index += 1
                    if self.background_index == 20:
                        self.background_index = 0
                    # print(self.background_index)

                    
            self.draw(self.win)

        self.quit()


if __name__ == "__main__":
    X = Game()
    X.run()
