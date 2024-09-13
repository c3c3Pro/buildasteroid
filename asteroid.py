from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        #overriding draw() method
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0,0)
        self.color = (128, 128, 128)


    def draw(self, screen):
        #drawing an asteroid as a gray circle:
        pygame.draw.circle(screen, self.color, (self.position.x, self.position.y), self.radius, width=2)    

    def update(self, dt):    
        self.position += self.velocity * dt
        