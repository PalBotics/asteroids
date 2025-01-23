# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# import everything from constants.py
from constants import *

# import the Player class
from player import Player

# import the CircleShape class
from circleshape import CircleShape

# import the Asteroid class
from asteroid import Asteroid

# import the Asteroidfield class
from asteroidfield import AsteroidField

# import the Bullet class
from bullet import Bullet 

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # initialize pygame
    pygame.init()

    # initialize a new game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create a Clock object to control the frame rate
    clock = pygame.time.Clock()
    
    # Calculate the time delta (dt) in seconds
    dt = clock.tick(60) / 1000  # 60 FPS

    # create groups to manage game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    # add all instances of player to the appropriate groups
    Player.containers = (updatable, drawable)

    # add all asteroids to the appropriate groups
    Asteroid.containers = (updatable, drawable, asteroids)

    # add the Asteroidfield class to the updatable group
    AsteroidField.containers = (updatable)

    # add the Bullet class to updatable and drawable
    Bullet.containers = (updatable, drawable)

    # instantiate a Player object
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, bullets, updatable, drawable)

    # instantiate the Asteroidfield
    asteroidfield = AsteroidField()

    # set a flag to end the game loop
    running = True

    # start the game loop
    while running:

        # Calculate the time delta (dt) in seconds
        #dt = clock.tick(60) / 1000  # 60 FPS

        # make an escape from the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return        

        # paint the screen black
        screen.fill((0,0,0))

        # draw the player
        for obj in drawable:
            obj.draw(screen)

        #update the player state
        for obj in updatable:
            obj.update(dt)

        #update the display
        pygame.display.flip()  

        # check for collisions
        for asteroid in asteroids:

            # check for ship / asteroid collisions
            if CircleShape.collision_check(player, asteroid):
                print("Game over!") 
                #  running = False  

            # check for bullet / asteroid collisions
            for bullet in bullets:
                #print(f"Checking bullet {bullet} with asteroid {asteroid}")
                if bullet.collision_check(asteroid):
                    #print("asteroid has been shot")
                    bullet.kill()  # Remove the bullet from its group
                    asteroid.kill()  # Remove the asteroid from its group

        # Control the frame rate (e.g., 60 FPS)
        clock.tick(60)

    


if __name__ == "__main__":
    main()