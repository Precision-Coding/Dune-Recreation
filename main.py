# DUNE RECREATION GUI

import pygame
import sys

def backGround(width, height):
    # Can be changed later on for customisation (Im not sure of the legality of that image but oh well)
    back_ground_img = pygame.image.load("assets\BackGrounds\DuneBG.png").convert_alpha()
    back_ground_surf = pygame.transform.scale(back_ground_img, (width, height))
    return back_ground_surf

def ball(width, height):
    # Can be changed later on for customisation
    ball_img = pygame.image.load("assets\Balls\Ball1.png").convert_alpha()
    ball_surf = pygame.transform.scale(ball_img, (width / 60, height / 30))
    return ball_surf

width, height = 1200, 600 # Size of game window
resolution = 1

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

# Event Loop
while True:
    # Ends the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Loads Surfaces from functions
    back_ground_surf = backGround(width, height)
    court_surf = ball(width, height)

    # Block Image Transfers
    screen.blit(back_ground_surf, (0,0))
    screen.blit(court_surf, (width / 2,  height / 2))

    # Updates and tickrate
    pygame.display.update()
    clock.tick(frame_rate)
