from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score
import pygame
import sys

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Initialize the font
    pygame.font.init()
    # Initialize Score
    score = Score()

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    # Game Loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        # player.update(dt)
        # player.draw(screen)
        for updatable_item in updatable:
            updatable_item.update(dt)
        for asteroid_item in asteroids:
            if player.collides_with(asteroid_item):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot_item in shots:
                if shot_item.collides_with(asteroid_item):
                    log_event("asteroid_shot")
                    shot_item.kill()
                    asteroid_item.split()
                    score.up_score(1)
        for drawable_item in drawable:
            drawable_item.draw(screen)

        score.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
