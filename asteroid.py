# asteroid.py

import circleshape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius, velocity, updatable, drawable):
        # Call the parent class's constructor with x, y, and radius
        super().__init__(x, y, radius)
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.pos_x = x
        self.pos_y = y
        self.radius = radius
        self.velocity = velocity
        self.updatable = updatable
        self.drawable = drawable

    # draw the asteroid as a circle
    def draw(self, screen):
        pygame.draw.circle(screen, 
                           (255, 255, 255), # white color
                           (int(self.position.x), int(self.position.y)), # use position from parent
                           self.radius, 
                           2)   # border width
        
    # split the asteroid into smaller asteroids or, if small, then kill it
    def split(self):
        #print("Splitting or killing asteroid")
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            #print("Splitting asteroid")
            random_angle = random.uniform(20, 50) # random angle between 20 and 50
            new_vector1 = self.velocity.rotate(random_angle) * 1.2  # 1.2 times the speed
            new_vector2 = self.velocity.rotate(-random_angle) * 1.2 # 1.2 times the speed
            new_radius = self.radius - ASTEROID_MIN_RADIUS  # new radius is smaller for the new asteroids
            # spawn two new asteroids
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius, new_vector1, self.updatable, self.drawable)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius, new_vector2, self.updatable, self.drawable)

            # add the asteroids to the appropriate groups
            #self.groups()[0].add(asteroid1)
            #self.groups()[0].add(asteroid2)
            self.updatable.add(asteroid1)
            self.updatable.add(asteroid2)
            self.drawable.add(asteroid1)
            self.drawable.add(asteroid2)


    # Override the update() method so that it moves in a straight line at constant speed.  
    # On each frame, it should add (self.velocity * dt) to its position (get self.velocity from its parent class, CircleShape).
    def update(self, dt):
        self.position += self.velocity * dt