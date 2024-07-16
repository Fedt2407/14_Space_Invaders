import pygame

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font(None, 30)
        self.text_color = (255, 255, 255)
        self.position = (10, 570)
        self.lives = 3

    def increase_score(self, points):
        self.score += points

    def decrease_lives(self):
        self.lives -= 1

    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.score} - Lives: {self.lives}", True, self.text_color)
        screen.blit(score_text, self.position)