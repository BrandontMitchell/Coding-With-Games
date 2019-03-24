import pygame
import random
import time
import math
import sys

"""

1. Display
    a. window size
    b. keydown events (space for jump, q for quit)
    c. object placement on load

2. Object movement
    a. Pipes moving left to right at constant speed
        i. once user reaches certain level, move pipes vertically as well as horizontal
    b. bird stays in place, just moves up and down (if past pipes)
    c. Background objects (ground, structures, clouds, etc.)

3. Game physics
    a. bird negative velocity with gravity
    b. bird positive y velocity with help from space bar 


"""
# game settings 
pygame.init()
FPS = 120
gameOver = False
clock = pygame.time.Clock()

# Object colors 
black = (0,0,0)
white = (255,255,255)

# Size and positioning
WIDTH = 480
HEIGHT = 263
ground = 150
textLoc = [200, 80]
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load("background.png").convert()
pygame.display.set_caption("Flappy Bird")

# flappy characteristics
x = 150
y = 50
bgX = 0
x_vel = 0
y_vel = 0
        
def createPipe(xStart, yStart):
    pipe = pygame.image.load("pipe.bmp").convert_alpha()
    pipe = pygame.transform.scale(pipe, (50, 35))
    pipe.set_colorkey((255, 255, 255))
    screen.blit(pipe, (xStart, yStart))


def flappyCreate(xStart,yStart):
    flappy = pygame.image.load("flappy.bmp").convert_alpha()
    flappy = pygame.transform.scale(flappy, (50, 35))
    flappy.set_colorkey((255, 255, 255))
    screen.blit(flappy, (xStart, yStart))
    
def gameover():
    font = pygame.font.SysFont(None, 25)
    text = font.render("Game Over", True, black)
    screen.blit(text, textLoc)
    gameOver = True

#test


while not gameOver:
    

    #in game controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_vel = -8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y_vel = 3
    

    #background image scrolling effect
    rel_x = bgX % bg.get_rect().width
    screen.blit(bg, (rel_x - bg.get_rect().width, 0))
    # events()
    if rel_x < WIDTH:
        screen.blit(bg, (rel_x, 0))
    bgX -= 1
    
    #bird creation and velocity updates
    flappyCreate(x, y)
    y += y_vel
    if y > ground: 
        gameover()
        y_vel=0

    #pipe creation
    createPipe(150, 0)

    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)
    
    

pygame.quit()
