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
    dt = 0

    # instantiate a Player object
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    # start the game loop
    while True:
        # make an escaoe from the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return        

        # paint the screen black
        screen.fill((0,0,0))

        # draw the player
        player.draw(screen)

        #update the display
        pygame.display.flip()        

        # Control the frame rate (e.g., 60 FPS)
        clock.tick(60)

    


if __name__ == "__main__":
    main()