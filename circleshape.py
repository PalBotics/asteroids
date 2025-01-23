# circleshape.py

import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def collision_check(self, target):
        #dist = pygame.math.Vector2.distance_to(target.position,self.position)
        dist = self.position.distance_to(target.position)
        min_dist = self.radius + target.radius
        #print(f"Checking collision: dist={dist}, min_dist={min_dist}")
        return dist <= min_dist

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass