# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# import everything from constants.py
from constants import *

# import the Player class
from player import Player



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

    # add all instances of player to both groups
    Player.containers = (updatable, drawable)

    # instantiate a Player object
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    # start the game loop
    while True:

        # Calculate the time delta (dt) in seconds
        #dt = clock.tick(60) / 1000  # 60 FPS

        # make an escaoe from the game loop
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

        # Control the frame rate (e.g., 60 FPS)
        clock.tick(60)

    


if __name__ == "__main__":
    main()