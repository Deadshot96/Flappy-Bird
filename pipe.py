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
        self.image = None
        self.imgHeight = None

        self.imgBtmRect = None
        self.imgUprRect = None

        self.load_images()

    def draw(self, win: pygame.Surface) -> None:
        # pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        # pygame.draw.rect(win, self.color, (self.x, PIPE_MIN, self.width, self.refUpper))

        # win.blit(self.imageBtm, (self.x, self.y))
        # win.blit(self.imageUpr, (self.x, PIPE_MIN))
        self.update_rects()

        win.blit(self.imageBtm, self.imgBtmRect)
        win.blit(self.imageUpr, self.imgUprRect)


    def isOnScreen(self) -> bool:
        return (self.x + self.width) > 0

    def move(self) -> None:
        self.x -= GAME_SPEED

    def getX(self) -> int:
        return self.x

    def load_images(self):
        image = pygame.image.load(os.path.join(ASSET_DIR, 'pipe.png'))
        width, height = image.get_size()
        self.imgHeight = max(self.height, height, self.refUpper)
        # width, height = image.get_size()
        # print(image.get_size())
        self.imageBtm = pygame.transform.scale(image, (self.width, self.imgHeight))
        self.imageUpr = pygame.transform.flip(image, False, True)
        self.imageUpr = pygame.transform.scale(self.imageUpr, (self.width, self.imgHeight))

    def update_rects(self):
        self.imgUprRect = self.imageUpr.get_rect()
        self.imgUprRect.topleft = (self.x, -(self.imgHeight - self.refUpper))

        self.imgBtmRect = self.imageBtm.get_rect()
        self.imgBtmRect.topleft = (self.x, self.y)

    def isColliding(self, x: int, y: int) -> bool:
        bird = pygame.rect.Rect(0, 0, BIRD_SIZE, BIRD_SIZE)
        bird.center = x, y
        self.update_rects()

        return self.imgUprRect.colliderect(bird) or self.imgBtmRect.colliderect(bird)
