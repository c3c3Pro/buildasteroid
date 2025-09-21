from circleshape import *
import pygame
from camera import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = (255, 255, 255)
        self.velocity = pygame.Vector2(0, -1) * PLAYER_SPEED

    def draw(self, screen, camera):
        #drawing a shot beam
        screen_position = camera.apply(self.position)
        pygame.draw.circle(screen, self.color, (screen_position.x, screen_position.y), SHOT_RADIUS, width=2)    

    def update(self, dt):    
        #calculates the position of each shot
        self.position += self.velocity * dt     
