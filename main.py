import pygame
import random
from aliens import Alien
from spaceship import Spaceship

# Initialization of Pygame
pygame.init()

# Window dimensions
window_width = 1800
window_height = 1000

# Create the game window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Space Invaders")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Variables for the spaceship
spaceship = Spaceship(window_width // 2 - 30, window_height - 100)

# Create initial aliens
aliens = []
for i in range(1):
    x = random.randint(0, window_width - 50)
    y = random.randint(50, 150)
    aliens.append(Alien(x, y))

def draw_spaceship(x, y):
    pygame.draw.rect(window, white, (x, y, spaceship.width, spaceship.height))

# Game loop
running = True
while running:
    window.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Spaceship movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and spaceship.x > 0:
        spaceship.x -= spaceship.speed
    if keys[pygame.K_RIGHT] and spaceship.x < window_width - spaceship.width:
        spaceship.x += spaceship.speed

    # Update and draw aliens
    for alien in aliens:
        alien.update(window_width)
        alien.draw(window)

    # Draw the spaceship
    spaceship.draw(window)

    pygame.display.update()

# Close the game
pygame.quit()
