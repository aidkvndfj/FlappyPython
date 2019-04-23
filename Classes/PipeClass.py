import pygame
from PipeClassTop import *

class Pipe():
    def __init__(self, WIDTH, HEIGHT, screen):
        def __init__(self):
            self.screen = screen
            self.pipes = pygame.sprite.Group()
            topPipe = TopPipe(WIDTH, HEIGHT)
            self.pipes.add(topPipe)

        def update(self):
            self.pipes.update()
            self.pipes.draw(self.screen)
