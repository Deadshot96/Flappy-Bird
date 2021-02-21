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
        self.image = None

        self.load_images()


    def draw(self, win: pygame.Surface) -> None:

        if self.vy < 0:
            self.image = self.downflap
        elif self.vy > 0:
            self.image = self.upflap
        else:
            self.image = self.midflap

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        win.blit(self.image, self.rect)

        # pygame.draw.circle(win, self.color, (self.x, self.y), self.size // 2)

    def move(self):
        self.vy += self.gravity
        self.y += self.vy
        self.y = int(self.y)

    def jump(self):
        self.vy = -8

    def load_images(self):
        self.upflap = pygame.image.load(os.path.join(ASSET_DIR, 'upflap.png'))
        self.midflap = pygame.image.load(os.path.join(ASSET_DIR, 'midflap.png'))
        self.downflap = pygame.image.load(os.path.join(ASSET_DIR, 'downflap.png'))

        self.upflap = pygame.transform.scale(self.upflap, (self.size, self.size))
        self.midflap = pygame.transform.scale(self.midflap, (self.size, self.size))
        self.downflap = pygame.transform.scale(self.downflap, (self.size, self.size))

