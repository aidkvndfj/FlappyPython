import pygame
import math
import random

GREEN = (40, 155, 25)

class TopPipe(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.width = WIDTH
        self.height = HEIGHT

        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.left = WIDTH
        self.rect.top = topPos
        self.speedx = -5

    def update(self):
        self.rect.centerx += self.speedx
