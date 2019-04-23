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

# Constants
WIDTH = 350
HEIGHT = 500
FPS = 30

# Define Colors
SKY = (0, 170, 255)
WHITE = (255, 255, 255)

# Variables
secondSpawn = False
score = 0

# Initalize PyGame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Snake")

# Define the game clock
clock = pygame.time.Clock()

# Font/Text Setup
scoreFont = pygame.font.SysFont("Halvetica", 20)
scoreText = scoreFont.render("Score: {0}".format(score), False, (WHITE))

#~~~~~~~ Sprites Init ~~~~~~~#
# Create sprite groups
pipes = pygame.sprite.Group() # Pipe Group
allSprites = pygame.sprite.Group() # Group for all sprites

# Create bird and first pipe set
pipe = Pipe(WIDTH, HEIGHT, "MASTER", 0) # Create Master Pipe
pipe2 = Pipe(WIDTH, HEIGHT, "FOLLOWER", pipe.rect.bottom + 100) # Create Follower Pipe
bird = Bird(HEIGHT)

# Add pipes/bird to respective groups
pipes.add(pipe, pipe2) #add pipes to pipe group
allSprites.add(pipe, pipe2, bird) # Add pipes and bird to all sprites

#~~~~~~~~~ Functions ~~~~~~~~#
def ReSpawn(group): # will respawn a pipe group
    if (group == 1):
        pipe.respawn(0)
        pipe2.respawn(pipe.rect.bottom + 100)
    if (group == 2):
        pipe3.respawn(0)
        pipe4.respawn(pipe3.rect.bottom + 100)

#~~~~~~ Main Game Loop ~~~~~~#
running = True
while (running):
    # Set FPS
    clock.tick(FPS)

    # Check for bird collision
    if (bird.rect.bottom < -50 or bird.rect.top > HEIGHT or pygame.sprite.spritecollide(bird, pipes, False)):
        running = False

    # Checks to see it is clear to spawn 2nd pipe group
    if (pipe.rect.centerx < WIDTH / 2 and secondSpawn == False):
        pipe3 = Pipe(WIDTH, HEIGHT, "MASTER", 0)
        pipe4 = Pipe(WIDTH, HEIGHT, "FOLLOWER", pipe3.rect.bottom + 100)
        pipes.add(pipe3, pipe4)
        allSprites.add(pipe3, pipe4)
        secondSpawn = True

    # Checks for key pressed
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
        if (event.type == pygame.KEYDOWN):
            key = pygame.key.get_pressed()
            if (key[pygame.K_SPACE]):
                bird.jump()

    # Check For respawn
    if (pipe.rect.right <= 0):
        ReSpawn(1)
    if (secondSpawn == True):
        if (pipe3.rect.right <= 0):
            ReSpawn(2)

    # Check To score
    if (pipe.rect.right < bird.rect.left and pipe.rect.right > bird.rect.left - 10):
        score += 1
        scoreText = scoreFont.render("Score: {0}".format(score), False, (WHITE))
    if(secondSpawn):
        if(pipe3.rect.right < bird.rect.left and pipe3.rect.right > bird.rect.left - 10):
            score += 1
            scoreText = scoreFont.render("Score: {0}".format(score), False, (WHITE))

    allSprites.update()

    # Draw/Render
    # Remove Everything On Screen
    screen.fill(SKY)

    # Draw sprites and score
    allSprites.draw(screen)
    screen.blit(scoreText, (10, 10))

    # Display frame
    pygame.display.flip()

# End Pygame
pygame.quit()
pygame.font.quit()
