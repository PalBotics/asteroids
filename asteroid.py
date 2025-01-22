# asteroid.py

import circleshape
import pygame

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        # Call the parent class's constructor with x, y, and radius
        super().__init__(x, y, radius)

        self.pos_x = x
        self.pos_y = y
        self.radius = radius

    # draw the asteroid as a circle
    def draw(self, screen):
        pygame.draw.circle(screen, 
                           (255, 255, 255), # white color
                           (int(self.position.x), int(self.position.y)), # use position from parent
                           self.radius, 
                           2)   # border width

    # Override the update() method so that it moves in a straight line at constant speed.  
    # On each frame, it should add (self.velocity * dt) to its position (get self.velocity from its parent class, CircleShape).
    def update(self, dt):
        self.position += self.velocity * dt