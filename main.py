import pygame
import sys
from asteroid import *
from asteroidfield import *
from constants import *
from player import Player


def main():
    pygame.init()

    # Creates window / play area
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)    # Player starts in center of screen

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Allows window to close properly

        dt = clock.tick(60) / 1000  # Set frame rate

        updatable.update(dt)   # Player sprite can spin
        screen.fill((0, 0, 0))  # Black window

        for asteroid in asteroids:
            if player.collision_check(asteroid):
                sys.exit("Game over!")

        for sprite in drawable:
            sprite.draw(screen) # Instantiates player
        pygame.display.flip()   # Loops window back to top
        

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()