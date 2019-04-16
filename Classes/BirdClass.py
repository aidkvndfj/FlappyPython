import pygame

WHITE = (255, 255, 255)

class Bird(pygame.sprite.Sprite):
    def __init__(self, HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (40, HEIGHT / 2)
        self.gravity = 1
        self.vely = 0

    def update(self):
        self.vely += self.gravity
        self.rect.centery += self.vely

    def jump(self):
        self.vely = -10
