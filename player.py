# player.py

import pygame
import circleshape
from bullet import Bullet

from constants import *

class Player(circleshape.CircleShape):
    
    def __init__(self, x, y, bullets_group, updatable_group, drawable_group):
        # Call the parent class's constructor with x, y, and PLAYER_RADIUS
        super().__init__(x, y, PLAYER_RADIUS)

        # Create the rotation field and initialize it to 0
        self.rotation = 0

        self.pos_x = x
        self.pos_y = y
        self.radius = PLAYER_RADIUS
        self.shot_timer = PLAYER_SHOOT_COOLDOWN

        # Store the groups
        self.bullets_group = bullets_group
        self.updatable_group = updatable_group
        self.drawable_group = drawable_group

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

    # method to rotate the player ship
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    # method to move the player ship
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    # method to shoot
    def shoot(self):
        # check to see if shot timer is 0
        if self.shot_timer <= 0:

            # Create a bullet instance at the player's position
            bullet = Bullet(self.position.x, self.position.y, SHOT_RADIUS, PLAYER_SHOOT_SPEED)

            direction = pygame.Vector2(0, 1).rotate(self.rotation)
            bullet.velocity = direction * PLAYER_SHOOT_SPEED

            # Add the bullet to the bullets group
            self.bullets_group.add(bullet)
            self.updatable_group.add(bullet)
            self.drawable_group.add(bullet)

            # reset shot timer
            self.shot_timer = PLAYER_SHOOT_COOLDOWN
    
    def update(self, dt):
        #print("update")
        keys = pygame.key.get_pressed()

        # decrease shot timer
        self.shot_timer -= dt

        if keys[pygame.K_a]:
            dt_neg = dt*-1
            self.rotate(dt_neg)
            #print("rotate left")
        if keys[pygame.K_d]:
            self.rotate(dt)
            #print("rotate right")
        if keys[pygame.K_s]:
            dt_neg = dt*-1
            self.move(dt_neg)
            #print("move backwards")
        if keys[pygame.K_w]:
            self.move(dt)
            #print("move forwards")
        if keys[pygame.K_SPACE]:
            self.shoot()
