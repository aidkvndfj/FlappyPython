import pygame
import random

GREEN = (0, 255, 0)

class Pipe(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 100))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = ((WIDTH / 2, HEIGHT / 2))
        self.speedx = -5

    def update(self):
        self.rect.centerx += self.speedx
