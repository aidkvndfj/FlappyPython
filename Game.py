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
allSprites = pygame.sprite.Group() # Group for all sprites

# Create bird and first pipe set
pipe = Pipe(WIDTH, HEIGHT) # Create Master Pipe
bird = Bird(HEIGHT)

# Add pipes/bird to respective groups
allSprites.add(bird) # Add pipes and bird to all sprites

#~~~~~~~~~ Functions ~~~~~~~~#

#~~~~~~ Main Game Loop ~~~~~~#
running = True
while (running):
    # Set FPS
    clock.tick(FPS)

    # Check for bird collision
    # if (bird.rect.bottom < -50 or bird.rect.top > HEIGHT or pygame.sprite.spritecollide(bird, pipe.pipes, False)):
        # running = False

    # Checks for key pressed
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
        if (event.type == pygame.KEYDOWN):
            key = pygame.key.get_pressed()
            if (key[pygame.K_SPACE]):
                bird.jump()

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
