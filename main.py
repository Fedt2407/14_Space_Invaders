import pygame
import random
from aliens import Alien

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
spaceship_width = 64
spaceship_height = 64
spaceship_x = window_width // 2 - spaceship_width // 2
spaceship_y = window_height - spaceship_height - 10
spaceship_speed = 5

# Create initial aliens
aliens = []
for i in range(1):
    x = random.randint(0, window_width - 50)
    y = random.randint(50, 150)
    aliens.append(Alien(x, y))

def draw_spaceship(x, y):
    pygame.draw.rect(window, white, (x, y, spaceship_width, spaceship_height))

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

    # Update and draw aliens
    for alien in aliens:
        alien.update(window_width)
        alien.draw(window)

    # Draw the spaceship
    draw_spaceship(spaceship_x, spaceship_y)

    pygame.display.update()

# Close the game
pygame.quit()
