import pygame

class Explosion:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.duration = 10
        self.frame = 0
        self.active = True

        self.frames = [
            [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
            [0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0],
            [1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
            [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0],
            [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1]
        ]

    def draw(self, window):
        if self.active:
            for i, row in enumerate(self.frames):
                for j, cell in enumerate(row):
                    if cell:
                        pygame.draw.rect(window, (255, 165, 0), (self.x + j * 5, self.y + i * 5, 5, 5))

    def update(self):
        if self.frame < self.duration:
            self.frame += 1
        else:
            self.active = False  # Termina l'esplosione dopo il numero di frame


class Missile:
    def __init__(self, x, y, speed=5, cell_size=3):
        self.x = x
        self.y = y
        self.speed = speed
        self.cell_size = cell_size
        self.color = (0, 255, 0)
        self.active = True

        # Grid-based shape of the missile
        self.shape = [
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0],
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
            self.y += self.speed  # Change the direction to go downwards
            if self.y > 600:
                self.active = False
            self.rect.topleft = (self.x, self.y)


class Octopus:
    def __init__(self, x, y, cell_size=5):
        self.x = x
        self.y = y
        self.cell_size = cell_size
        self.color = (167, 7, 255)
        self.active = True
        self.missiles = []
        
        # Grid-based shape of the alien
        self.shape = [
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
            [0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
            [0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
            [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
            [1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1],
            [1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1]
        ]

        self.width = len(self.shape[0]) * self.cell_size
        self.height = len(self.shape) * self.cell_size
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.speed = 1

    def draw(self, window):
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(window, self.color, (self.x + j * self.cell_size, self.y + i * self.cell_size, self.cell_size, self.cell_size))

    def update(self, window_width):
        self.x += self.speed
        if self.x <= 0 or self.x >= window_width - self.width:
            self.speed *= -1
            self.y += self.cell_size * 24
        self.rect.topleft = (self.x, self.y)

    def hit(self):
        self.explosion = Explosion(self.x, self.y)
        self.active = False
        return self.explosion


    def shoot(self):
        if self.active:
            self.missiles.append(Missile(self.x + self.width // 2, self.y, speed=5))
            return self.missiles[-1]


class Crab:
    def __init__(self, x, y, cell_size=5):
        self.x = x
        self.y = y
        self.cell_size = cell_size
        self.color = (255, 0, 0)
        self.active = True
        self.missiles = []
        
        # Grid-based shape of the alien
        self.shape = [
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
            [1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1]
        ]

        self.width = len(self.shape[0]) * self.cell_size
        self.height = len(self.shape) * self.cell_size
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.speed = 1

    def draw(self, window):
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(window, self.color, (self.x + j * self.cell_size, self.y + i * self.cell_size, self.cell_size, self.cell_size))

    def update(self, window_width):
        self.x += self.speed
        if self.x <= 0 or self.x >= window_width - self.width:
            self.speed *= -1
            self.y += self.cell_size * 24
        self.rect.topleft = (self.x, self.y)


    def hit(self):
        self.explosion = Explosion(self.x, self.y)
        self.active = False
        return self.explosion
    

    def shoot(self):
        if self.active:
            self.missiles.append(Missile(self.x + self.width // 2, self.y, speed=5))
            return self.missiles[-1]
