import pygame
import random
import time
import math

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
pygame.init()

# Object colors 
black = (0,0,0)
white = (255,255,255)

# Size and positioning
size = width, height = 700, 700
ground = 480
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy Bird")

# Ball characteristics
x = 350
y = 250
x_vel = 0
y_vel = 0

gameOver = False
clock = pygame.time.Clock()

def ball(x,y):
    pygame.draw.circle(screen, black, (x,y), 20)

def gameover():
    font = pygame.font.SysFont(None, 25)
    text = font.render("Game Over", True, black)
    screen.blit(text, [150, 250])


while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_vel = -10
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y_vel = 5
    screen.fill(white) 
    ball(x,y)
    y += y_vel

    if y > ground: 
        gameover()
        y_vel=0

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
