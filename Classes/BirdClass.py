import pygame
import os

WHITE = (255, 255, 255)

gameFolder = os.path.dirname("..")
# playerImg = pygame.image.load(os.path.join(gameFolder, 'bird.png')).convert()
birdImage = pygame.image.load(os.path.join(gameFolder, 'bird.png'))

class Bird(pygame.sprite.Sprite):
    def __init__(self, HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.image = birdImage
        # self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (40, HEIGHT / 2)
        self.gravity = 1
        self.vely = 0

    def update(self):
        self.vely += self.gravity
        self.rect.centery += self.vely

    def jump(self):
        self.vely = -10
