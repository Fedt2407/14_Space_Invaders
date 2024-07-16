import pygame
import time
from aliens import Octopus, Crab, Skull
from spaceship import Spaceship
from scoreboard import Scoreboard
import random

# Initialization of Pygame
pygame.init()

# Window dimensions
window_width = 1000
window_height = 600

# Create the game window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Space Invaders Reforged by Fxx1")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Initialize spaceship
spaceship = Spaceship(window_width // 2 - 30, window_height - 80)
scoreboard = Scoreboard()

# Create initial aliens
aliens = []
for i in range(15):
    x = 65 * i
    y = 5
    aliens.append(Skull(x, y))

for i in range(15):
    x = 65 * i
    y = 52
    aliens.append(Octopus(x, y))

for i in range(15):
    x = 65 * i
    y = 100
    aliens.append(Crab(x, y))

# Initialize other variables
alien_missiles = []
explosions = []
ship_explosions = []
alien_shoot_interval = 1  # Intervalo di sparo in secondi
last_alien_shoot_time = time.time()

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    window.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement of the spaceship
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and spaceship.x > 0:
        spaceship.x -= spaceship.speed
    if keys[pygame.K_RIGHT] and spaceship.x < window_width - spaceship.width:
        spaceship.x += spaceship.speed
    if keys[pygame.K_SPACE] and spaceship.active:
        spaceship.shoot()

    # Shoot alien missiles
    current_time = time.time()
    if current_time - last_alien_shoot_time > alien_shoot_interval:
        active_aliens = [alien for alien in aliens if alien.active]
        if active_aliens:
            random_alien = random.choice(active_aliens)
            missile = random_alien.shoot()
            alien_missiles.append(missile)
        last_alien_shoot_time = current_time

    # Update and draw aliens
    for alien in aliens:
        alien.update(window_width)
        alien.draw(window)

    # Update and draw alien missiles
    for missile in alien_missiles[:]:
        missile.update()
        missile.draw(window)
        if not missile.active:
            alien_missiles.remove(missile)
        if missile.rect.colliderect(spaceship.rect) and spaceship.active:
            ship_explosions.append(spaceship.hit())
            scoreboard.decrease_lives()
            spaceship.active = False  # Make the spaceship disappear
            missile.active = False  # Deactivate the missile that hit the spaceship
            # Check if the game is over
            if scoreboard.lives == 0:
                scoreboard.game_over(window)
                spaceship.active = False

    # Update and draw spaceship missiles
    for missile in spaceship.missiles[:]:
        missile.update()
        missile.draw(window)

        # Check for collisions with aliens
        for alien in aliens[:]:
            if missile.rect.colliderect(alien.rect):
                explosion = alien.hit()  # Called when a missile hits an alien
                scoreboard.increase_score(10)  # Increase the score by 10
                if explosion:
                    explosions.append(explosion)  # Add the explosion to the list of explosions
                missile.active = False  # Deactivate the missile

    # Update and draw explosions
    for explosion in explosions[:]:
        explosion.update()  # Update the explosion
        explosion.draw(window)  # Draw the explosion
        if not explosion.active:
            explosions.remove(explosion)  # Remove the explosion if it's not active

    # Update and draw spaceship explosions
    for ship_explosion in ship_explosions[:]:
        ship_explosion.update()  # Update the explosion
        ship_explosion.draw(window)  # Draw the explosion
        if not ship_explosion.active:
            ship_explosions.remove(ship_explosion)  # Remove the explosion if it's not active

    # Check if spaceship should reappear
    if not spaceship.active and scoreboard.lives > 0:
        time.sleep(1)  # Wait for 1 second before respawning
        spaceship = Spaceship(window_width // 2 - 30, window_height - 80)

    # Remove inactive aliens
    aliens = [alien for alien in aliens if alien.active]

    # Remove inactive spaceship missiles
    spaceship.missiles = [missile for missile in spaceship.missiles if missile.active]

    # Draw the spaceship and the scoreboard
    if spaceship.active:
        spaceship.draw(window)
    scoreboard.draw(window)

    pygame.display.update()
    clock.tick(60)

# Chiudi il gioco
pygame.quit()
