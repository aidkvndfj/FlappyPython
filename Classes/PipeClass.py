import pygame
import math
import random

GREEN = (40, 155, 25)

class Pipe(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT, type, topPos):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.width = WIDTH
        self.height = HEIGHT
        if (self.type == "MASTER"):
            self.image = pygame.Surface((60, random.randint(50, 450)))
        if (self.type == "FOLLOWER"):
            self.image = pygame.Surface((60, math.ceil(HEIGHT - topPos)))

        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.left = WIDTH
        self.rect.top = topPos
        self.speedx = -5

    def update(self):
        self.rect.centerx += self.speedx

    def respawn(self, topPos):
        if (self.type == "MASTER"):
            self.image = pygame.Surface((60, random.randint(100, 300)))
        if (self.type == "FOLLOWER"):
            self.image = pygame.Surface((60, self.height - topPos))

        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.left = self.width
        self.rect.top = topPos
        self.speedx = -5
