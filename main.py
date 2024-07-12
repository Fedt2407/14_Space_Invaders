import pygame
import random

# Initialization of Pygame
pygame.init()

# Window dimensions
window_width = 800
window_height = 600

# Create the game window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Space Invaders")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Variables for the spaceship
spaceship_image = pygame.image.load("spaceship.png")
spaceship_width = 64
spaceship_height = 64
spaceship_x = window_width // 2 - spaceship_width // 2
spaceship_y = window_height - spaceship_height - 10
spaceship_speed = 5

# Variables for the aliens
alien_image = pygame.image.load("alien.png")
alien_width = 64
alien_height = 64
alien_x = random.randint(0, window_width - alien_width)
alien_y = random.randint(50, 150)
alien_speed = 2

def draw_spaceship(x, y):
    window.blit(spaceship_image, (x, y))

def draw_alien(x, y):
    window.blit(alien_image, (x, y))

# Game loop
running = True
while running:
    window.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Spaceship movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and spaceship_x > 0:
        spaceship_x -= spaceship_speed
    if keys[pygame.K_RIGHT] and spaceship_x < window_width - spaceship_width:
        spaceship_x += spaceship_speed

    # Alien movement
    alien_x += alien_speed
    if alien_x <= 0 or alien_x >= window_width - alien_width:
        alien_speed *= -1
        alien_y += 50

    draw_spaceship(spaceship_x, spaceship_y)
    draw_alien(alien_x, alien_y)

    pygame.display.update()

# Close the game
pygame.quit()
