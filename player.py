# player.py

import pygame
import circleshape

from constants import PLAYER_RADIUS

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        # Call the parent class's constructor with x, y, and PLAYER_RADIUS
        super().__init__(x, y, PLAYER_RADIUS)

        # Create the rotation field and initialize it to 0
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # draw the player's ship as a triangle
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
