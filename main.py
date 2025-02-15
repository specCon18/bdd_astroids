import pygame
import sys
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot 

def main():

    # Print basic starting info
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
   
    # Initialize game, screen, game-clock and delta time counter
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # Groups
    drawables = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set the containers of the astroids
    Asteroid.containers = (asteroids,drawables,updatables)

    # Set the containers of the astroid_field
    AsteroidField.containers = (updatables)
    af = AsteroidField()

    # Set the containers of player
    Player.containers = (drawables, updatables)
    # Set the position of the player
    p1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    
    Shot.containers = (shots,drawables,updatables)
    while True:
        # if event is quit then kill the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # fill the screen with the void of space
        screen.fill((0, 0, 0))
        
        for drawable in drawables:
            drawable.draw(screen)
        for updatable in updatables:
            updatable.update(dt)
        for asteroid in asteroids:
            if p1.is_colided(asteroid):
                print("Game Over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if shot.is_colided(asteroid):
                    asteroid.split()
                    shot.kill()
        pygame.display.flip()
        tick = clock.tick(60)
        dt = tick/1000
if __name__ == "__main__":
    main()
