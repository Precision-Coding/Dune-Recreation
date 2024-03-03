# DUNE RECREATION GUI

import pygame
import sys

def backGround(width, height):
    # Can be changed later on for customisation (Im not sure of the legality of that image but oh well)
    back_ground_img = pygame.image.load("assets/BackGrounds/DuneBG.png")
    back_ground_surf = pygame.transform.scale(back_ground_img, (width, height)).convert_alpha()
    return back_ground_surf

def ball(width, height):
    # Can be changed later on for customisation
    ball_img = pygame.image.load("assets/Balls/Ball1.png")
    ball_surf = pygame.transform.scale(ball_img, (width / 60, height / 30)).convert_alpha()
    return ball_surf



width, height = 1800, 900 # Size of game window


# Framerate
frame_rate = 60
clock = pygame.time.Clock()

# Screen Setup
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dune Recreation")

# Font
pygame.font.init()
baseFont = pygame.font.SysFont("helvetica", 20)

#Variables
x, y, x_velocity, y_velocity, gravity_offset, floor = width / 4, 0, 0, 0, 0, (height / 4 * 3)
ball_surf = ball(width, height)
back_ground = (backGround(width, height))
screen.blit(back_ground, (0,0))

# Event Loop
while True:
    # Ends the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    #Ball Movement
    x += x_velocity / 500
    y += y_velocity / 500

    # If the ball is touching the floor
    if y >= floor:
        gravity_offset = 0
        y = floor

        if pygame.mouse.get_pressed() == (True, False, False):
            x_velocity += width /  150


    # If the ball is in the air
    elif y < floor:
        if pygame.mouse.get_pressed() == (True, False, False):
            gravity_offset += height / 150
        #This is where the y and x velocity of the jump would have to be applied

    gravity = ((9.81 +  gravity_offset) * height) / 1000 # makes gravity proportional to window size
    y_velocity += gravity


    # Block Image Transfers
    screen.blit(back_ground, (0, 0))
    screen.blit(ball_surf, (x, y))

    # Updates and tickrate
    pygame.display.update()
    clock.tick(frame_rate)