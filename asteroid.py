from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        #overriding draw() method
        super().__init__(x, y, radius)
        #self.velocity = pygame.Vector2(velocity)
        self.position = pygame.Vector2(x, y)
        self.color = (128, 128, 128)


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.position.x, self.position.y), self.radius, width=2)    

    def update(self, dt):    
        self.position += self.velocity * dt
        