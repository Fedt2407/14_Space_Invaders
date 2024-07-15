import pygame
from aliens import Octopus, Crab
from spaceship import Spaceship
from scoreboard import Scoreboard

# Initialization of Pygame
pygame.init()

# Window dimensions
window_width = 1000
window_height = 600

# Create the game window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Space Invaders")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Initialize spaceship
spaceship = Spaceship(window_width // 2 - 30, window_height - 80)
scoreboard = Scoreboard()

# Create initial aliens
aliens = []
for i in range(10):
    x = 65 * i
    y = 5
    aliens.append(Crab(x, y))

for i in range(10):
    x = 65 * i
    y = 65
    aliens.append(Octopus(x, y))

# Game loop
running = True
clock = pygame.time.Clock()
explosions = []  # Lista per memorizzare le esplosioni

while running:
    window.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimenti della navicella spaziale
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and spaceship.x > 0:
        spaceship.x -= spaceship.speed
    if keys[pygame.K_RIGHT] and spaceship.x < window_width - spaceship.width:
        spaceship.x += spaceship.speed
    if keys[pygame.K_SPACE]:
        spaceship.shoot()

    # Aggiorna e disegna gli alieni
    for alien in aliens:
        alien.update(window_width)
        alien.draw(window)

    # Aggiorna e disegna i missili
    for missile in spaceship.missiles:
        missile.update()
        missile.draw(window)

        # Controlla collisioni con gli alieni
        for alien in aliens:
            if missile.rect.colliderect(alien.rect):
                explosion = alien.hit()  # Chiama il metodo hit e ottieni l'esplosione
                scoreboard.increase_score(10)  # Aumenta il punteggio
                if explosion:
                    explosions.append(explosion)  # Aggiungi l'esplosione alla lista
                missile.active = False  # Disattiva il missile

    # Aggiorna e disegna le esplosioni
    for explosion in explosions:
        explosion.update()  # Aggiorna l'esplosione
        explosion.draw(window)  # Disegna l'esplosione
        if not explosion.active:
            explosions.remove(explosion)  # Rimuovi l'esplosione inattiva

    # Rimuovi alieni inattivi
    aliens = [alien for alien in aliens if alien.active]

    # Rimuovi missili inattivi
    spaceship.missiles = [missile for missile in spaceship.missiles if missile.active]

    # Disegna la navicella spaziale
    spaceship.draw(window)
    scoreboard.draw(window)

    pygame.display.update()
    clock.tick(60)

# Chiudi il gioco
pygame.quit()