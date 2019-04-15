import pygame
import random

GREEN = (0, 255, 0)

class Pipe(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT, location):
        pygame.sprite.Sprite.__init__(self)
        self.screenWidth = WIDTH
        self.screenHeight = HEIGHT
        self.speedx = -5
        self.location = location
        self.spawn(self.location)

    def update(self):
        self.rect.centerx += self.speedx
        if (self.rect.right <= 0):
            self.spawn(self.location)

    def spawn(self, location):
        height = random.randint(150, 200)
        self.image = pygame.Surface((60, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.left = self.screenWidth
        if (location == "TOP"):
            self.rect.top = 0
        if (location == "BOTTOM"):
            self.rect.bottom = self.screenHeight
