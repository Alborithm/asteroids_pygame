from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS, IS_DEBUG, SCREEN_WIDTH, SCREEN_HEIGHT
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0
    
    # For drawing the player sprite
    def triangle(self):
        # It is an isosceles triangle so you can differentiate where it it looking at
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
        # debuging
        # Draw player collision shape which is the cirlce right now
        if IS_DEBUG:
            pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if not self.shoot_cooldown > 0:
                self.shot()
                self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
        
        self.shoot_cooldown -= dt


    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

        # check for wrap
        # X Wrap
        # if position x is < 0 - ship radius wraps it
        if self.position.x < 0 - self.radius:
            self.position.x = SCREEN_WIDTH + self.radius - 1
        elif self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = 0 - self.radius + 1
            
        # Y Wrap
        if self.position.y < 0 - self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius - 1
        elif self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = 0 - self.radius + 1

    def shot(self):
        new_shot = Shot(self.position.x, self.position.y)
        velocity = pygame.Vector2(0,1)
        velocity = velocity.rotate(self.rotation)
        velocity = velocity * PLAYER_SHOOT_SPEED
        new_shot.velocity = velocity
