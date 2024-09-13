import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, radius)
        self.color = color
        self.rotation = 0
        self.shoot_timer = 0

    def triangle(self):
        #drawing a triangle
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        #ensures the rotation is within 360 degrees
        self.rotation %= 360

    def update(self, dt):
        #handling key events
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
           self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)      
       # if keys[pygame.K_SPACE]:
        #    self.shoot()    

        self.shoot_timer += dt
        if keys[pygame.K_SPACE] and self.shoot_timer >= PLAYER_SHOOT_COOLDOWN:
            self.shoot()
            self.shoot_timer = 0


    def move(self, dt):
        #calculating the player's position when it moves forward
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        #where the player shoots
        shot_velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)

        shot.velocity = shot_velocity



