import pygame
import os
import time
import math
from settings import *
from bird import Bird
from pipe import Pipe


class Game:
    
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.win = None
        self.clock = None
        self.fps = FPS
        self.backgrounds = []
        self.tickEvent = pygame.event.Event(EVENT_TICK_TYPE)
        self.gameOver = pygame.event.Event(EVENT_GAMEOVER_TYPE)
        self.background_index = 0
        self.base = None
        self.baseX = BASE_WIDTH
        self.bird = None
        self.pipes = list()

    def draw(self, win: pygame.Surface) -> None:
        win.fill(MID_BLACK)

        index = self.background_index // 10
        win.blit(self.backgrounds[index], (0, 0))
        
        # win.blit(self.base, (0, 0))
        self.bird.move()
        self.bird.draw(self.win)

        for i in range(len(self.pipes) - 1, -1, -1):
            pipe = self.pipes[i]
            pipe.move()
            if pipe.isOnScreen():
                pipe.draw(win)
            else:
                self.pipes.remove(pipe)
                del pipe

        self.draw_base(self.win)

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
        pygame.time.set_timer(self.tickEvent.type, EVENT_TICK_DELTA)
        
        self.bird = Bird()

        self.load_images()

    def quit(self) -> None:
        pygame.font.quit()
        pygame.quit()

    def draw_base(self, win: pygame.Surface) -> None:
        if self.baseX <= 0:
            self.baseX = BASE_WIDTH

        self.baseX -= GAME_SPEED

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

                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()

                    if keys[pygame.K_SPACE]:
                        self.bird.jump()

                if event.type == self.tickEvent.type:
                    # print("Tick: ", self.tickEvent, sep='\t')
                    self.background_index += 1
                    # self.pipes.append(Pipe())
                    if self.background_index == 20:
                        self.background_index = 0
                
                    # print("Pipe: ", self.pipeGenEvent, sep='\t')
                    if len(self.pipes) >= 10:
                        # Failsafe to avoid too many pipes in the pipeline - :?)
                        continue


                    if len(self.pipes) == 0:
                        self.pipes.append(Pipe(self.width))
                    else:
                        prevX = self.pipes[-1].getX()
                        self.pipes.append(Pipe(prevX))
                    # print(len(self.pipes))

                if event.type == self.gameOver.type:
                    print("Game Over")
                    
                    
            self.draw(self.win)

            x, y = self.bird.get_pos()
            
            for pipe in self.pipes:
                if pipe.isColliding(x, y):
                    pygame.event.clear()
                    pygame.event.post(self.gameOver)


        self.quit()


if __name__ == "__main__":
    X = Game()
    X.run()
