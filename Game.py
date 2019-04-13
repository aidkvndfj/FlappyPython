##############################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~Created By: Eric~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
##############################

#~~~~~~~~~~~ Setup ~~~~~~~~~~#
# Needed Imports
import pygame
import random
import sys
sys.path.insert(0, 'Classes')
from BirdClass import *
from PipeClass import *

WIDTH = 600
HEIGHT = 600
FPS = 30

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Snake")

clock = pygame.time.Clock()

pipes = pygame.sprite.Group()
allSprites = pygame.sprite.Group()

pipe = Pipe(WIDTH, HEIGHT)

pipes.add(pipe)
allSprites.add(pipe)


running = True
while (running):
    clock.tick(FPS)

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False


    allSprites.update()
    # print("run")

    screen.fill(BLACK)
    allSprites.draw(screen)

    pygame.display.flip()

pygame.quit()
