import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def collides_with(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius

    def wrap_if_on_edge(self):
        if self.position.x < 0 - self.radius:
            self.position.x = SCREEN_WIDTH + self.radius - 1
        elif self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = 0 - self.radius + 1
            
        # Y Wrap
        if self.position.y < 0 - self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius - 1
        elif self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = 0 - self.radius + 1