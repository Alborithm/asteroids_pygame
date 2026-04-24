from constants import FONT_SIZE
import pygame

class Score():
    def __init__(self):
        self.score = 0
        self.x = 50
        self.y = 50
        self.font = pygame.font.Font(None, 32)
        self.text_surface = self.font.render("Test", False, "white", None)
    
    def draw(self, screen):
        self.text_surface = self.font.render(str(self.score), False, "White", None)
        screen.blit(self.text_surface, (self.x, self.y))

    def up_score(self, amount):
        self.score += amount