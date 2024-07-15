import pygame
import random

# Pygame initialization
pygame.init()

# Game window dimensions
window_width = 800
window_height = 600

# Creating the game window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Space Invaders")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

# Variables for the spaceship
spaceship_width = 64
spaceship_height = 64
spaceship_x = window_width // 2 - spaceship_width // 2
spaceship_y = window_height - spaceship_height - 10
spaceship_speed = 5

# Variables for the aliens
alien_width = 50
alien_height = 50
alien_speed = 2
aliens = []

# Create aliens
for i in range(5):
    x = random.randint(0, window_width - alien_width)
    y = random.randint(50, 150)
    aliens.append(pygame.Rect(x, y, alien_width, alien_height))

def draw_spaceship(x, y):
    pygame.draw.rect(window, white, (x, y, spaceship_width, spaceship_height))

def draw_alien(alien):
    pygame.draw.rect(window, green, alien)

# Game cycle
running = True
while running:
    window.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement of the spaceship
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and spaceship_x > 0:
        spaceship_x -= spaceship_speed
    if keys[pygame.K_RIGHT] and spaceship_x < window_width - spaceship_width:
        spaceship_x += spaceship_speed

    # Movement of the aliens
    for alien in aliens:
        alien.x += alien_speed
        if alien.x <= 0 or alien.x >= window_width - alien_width:
            alien_speed *= -1
            for a in aliens:
                a.y += alien_height // 2

    # Draw the spaceship
    draw_spaceship(spaceship_x, spaceship_y)

    # Disegna gli alieni
    for alien in aliens:
        draw_alien(alien)

    pygame.display.update()

# Close the game
pygame.quit()

