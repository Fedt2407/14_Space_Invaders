import pygame

class Alien:
    def __init__(self, x, y, cell_size=5):
        self.x = x
        self.y = y
        self.cell_size = cell_size
        self.color = (167, 7, 255)
        
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
        self.speed = 2

    def draw(self, window):
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(window, self.color, (self.x + j * self.cell_size, self.y + i * self.cell_size, self.cell_size, self.cell_size))

    def update(self, window_width):
        self.x += self.speed
        if self.x <= 0 or self.x >= window_width - self.width:
            self.speed *= -1
            self.y += self.cell_size * 11
        self.rect.topleft = (self.x, self.y)
