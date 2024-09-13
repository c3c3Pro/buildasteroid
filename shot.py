from circleshape import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = (255, 255, 255)
        self.velocity = pygame.Vector2(0, -1) * PLAYER_SPEED

    def draw(self, screen):
        #drawing a shot beam
        pygame.draw.circle(screen, self.color, (self.position.x, self.position.y), SHOT_RADIUS, width=2)    

    def update(self, dt):    
        #calculates the position of each shot
        self.position += self.velocity * dt     
