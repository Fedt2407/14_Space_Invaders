import pygame

import pygame
import time

class Missile:
    def __init__(self, x, y, speed=5, cell_size=3):
        self.x = x
        self.y = y
        self.speed = speed
        self.cell_size = cell_size
        self.color = (255, 165, 0)
        self.active = True

        # Grid-based shape of the missile
        self.shape = [
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 1, 1, 0],
            [1, 1, 0, 1, 1],
            [1, 0, 0, 0, 1]
        ]

        self.width = len(self.shape[0]) * self.cell_size
        self.height = len(self.shape) * self.cell_size
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def draw(self, window):
        if self.active:
            for i, row in enumerate(self.shape):
                for j, cell in enumerate(row):
                    if cell:
                        pygame.draw.rect(window, self.color, (self.x + j * self.cell_size, self.y + i * self.cell_size, self.cell_size, self.cell_size))
    
    def update(self):
        if self.active:
            self.y -= self.speed
            if self.y < 0:
                self.active = False
            self.rect.topleft = (self.x, self.y)

class Spaceship:
    def __init__(self, x, y, cell_size=5):
        self.x = x
        self.y = y
        self.cell_size = cell_size
        self.color = (0, 0, 255)
        self.missiles = []
        self.speed = 5
        self.last_shot_time = 0  # Timestamp of the last shot
        self.shoot_delay = 1  # Delay in seconds

        # Grid-based shape of the spaceship
        self.shape = [
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
            [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
        ]

        self.width = len(self.shape[0]) * self.cell_size
        self.height = len(self.shape) * self.cell_size
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def draw(self, window):
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(window, self.color, (self.x + j * self.cell_size, self.y + i * self.cell_size, self.cell_size, self.cell_size))

        for missile in self.missiles:
            missile.draw(window)

    def update(self, window_width):
        self.rect.topleft = (self.x, self.y)

        for missile in self.missiles:
            missile.update()

        # Remove inactive missiles
        self.missiles = [missile for missile in self.missiles if missile.active]

    def shoot(self):
        current_time = time.time()
        if current_time - self.last_shot_time >= self.shoot_delay:
            missile_x = self.x + self.width // 2  # Center the missile
            missile_y = self.y  # Start from the top of the spaceship
            missile = Missile(missile_x, missile_y)
            self.missiles.append(missile)
            self.last_shot_time = current_time  # Update the last shot time
    
