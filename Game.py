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

WIDTH = 300
HEIGHT = 500
FPS = 30

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Vars
secondSpawn = False

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Snake")

clock = pygame.time.Clock()

#~~~~~~~ Sprites Init ~~~~~~~#
pipes = pygame.sprite.Group() # Pipe Group
allSprites = pygame.sprite.Group() # Group for all sprites

pipe = Pipe(WIDTH, HEIGHT, "MASTER", 0) # Create Master Pipe
pipe2 = Pipe(WIDTH, HEIGHT, "FOLLOWER", pipe.rect.bottom + 100) # Create Follower Pipe
bird = Bird(HEIGHT)

pipes.add(pipe, pipe2) #add pipes to pipe group
allSprites.add(pipe, pipe2, bird) # Add pipes and bird to all sprites

#~~~~~~~~~ Functions ~~~~~~~~#
def ReSpawn():
    pipe.respawn(0)
    pipe2.respawn(pipe.rect.bottom + 100)

#~~~~~~ Main Game Loop ~~~~~~#
running = True
while (running):
    clock.tick(FPS)

    if (bird.rect.bottom < -50 or bird.rect.top > HEIGHT):
        running = False

    if (pipe.rect.right < WIDTH / 2 and secondSpawn == False):
        pipe3 = Pipe(WIDTH, HEIGHT, "MASTER", 0)
        pipe4 = Pipe(WIDTH, HEIGHT, "FOLLOWER", pipe3.rect.bottom + 100)
        secondSpawn = True

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
        if (event.type == pygame.KEYDOWN):
            key = pygame.key.get_pressed()
            if (key[pygame.K_SPACE]):
                bird.jump()

    if (pipe.rect.right <= 0):
        ReSpawn()

    allSprites.update()
    # print("run")

    screen.fill(BLACK)
    allSprites.draw(screen)

    pygame.display.flip()

pygame.quit()
