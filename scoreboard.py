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

    def game_over(self, screen):
        if self.lives == 0:
            game_over_text = self.font.render("GAME OVER", True, self.text_color)
            text_width = game_over_text.get_width()
            text_height = game_over_text.get_height()
            screen_width = screen.get_width()
            screen_height = screen.get_height()
            x = (screen_width - text_width) // 2
            y = (screen_height - text_height) // 2
            screen.blit(game_over_text, (x, y))