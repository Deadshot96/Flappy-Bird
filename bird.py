import pygame
import os
from settings import *
from typing import Tuple

def LinearMap(x, maxX, minX, maxY, minY):
    return (x - minX) / (maxX - minX) * (maxY - minY) + minY

class Bird:

    def __init__(self):
        self.x = BIRD_X
        self.y = BIRD_Y
        self.size = BIRD_SIZE
        self.color = YELLOW
        self.gravity = 0.25
        self.vy = 0
        self.image = None
        self.angle = 0
        self.bird_index = 0
        self.maxVel = MAXVEL

        self.load_images()


    def draw(self, win: pygame.Surface) -> None:

        # if self.vy < 0:
        #     self.angle = 20
        # elif self.vy > 0:
        #     self.angle = -20
        # else:
        #     self.angle = 0

        self.angle = LinearMap(self.vy, 8, -8, -20, 20)

        self.image = [self.upflap, self.midflap, self.downflap][self.bird_index // 10]
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        win.blit(self.image, self.rect)

        # pygame.draw.circle(win, self.color, (self.x, self.y), self.size // 2)

    def move(self):
        self.vy = min(self.maxVel, self.vy + self.gravity)
        self.y += self.vy
        self.y = int(self.y)

        self.bird_index += 1
        if self.bird_index == 30:
            self.bird_index = 0

    def jump(self):
        self.vy = -self.maxVel

    def load_images(self):
        self.upflap = pygame.image.load(os.path.join(ASSET_DIR, 'upflap.png'))
        self.midflap = pygame.image.load(os.path.join(ASSET_DIR, 'midflap.png'))
        self.downflap = pygame.image.load(os.path.join(ASSET_DIR, 'downflap.png'))

        self.upflap = pygame.transform.scale(self.upflap, (self.size, self.size))
        self.midflap = pygame.transform.scale(self.midflap, (self.size, self.size))
        self.downflap = pygame.transform.scale(self.downflap, (self.size, self.size))

    def get_pos(self) -> Tuple:
        return self.x, self.y

