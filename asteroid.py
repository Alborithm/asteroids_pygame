from circleshape import *
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
        self.wrap_if_on_edge()
    
    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            velocity_first_child = self.velocity.rotate(angle)
            velocity_second_child = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_first_child = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_second_child = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_first_child.velocity = velocity_first_child * 1.2
            asteroid_second_child.velocity = velocity_second_child * 1.2