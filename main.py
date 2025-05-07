# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
pygame.init()
# this allows us to use code from
# the open-source pygame library
# throughout this file
clock = pygame.time.Clock()
dt = 0
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    game_over = False
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable, shots)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    asteroid_field = AsteroidField()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000.0 
        screen.fill((0,0,0))
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        if player.collision(asteroids):
            print("Game Over", "You have been hit by an asteroid!")
            game_over = True
        for shot in shots:
            if shot.collision(asteroids):
                # Remove the asteroid that was hit
                for asteroid in asteroids:
                    if shot.collision([asteroid]):
                        asteroid.split()
                        break
                # Remove the shot after it hits an asteroid
                shot.kill()
        # Check for collisions between asteroids and player
        
        pygame.display.flip()
        

if __name__ == "__main__":
    main()