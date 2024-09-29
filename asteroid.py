from circleshape import *
from constants import *
import random

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

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle_two_circles = random.uniform(20, 50)

        velocity1 = self.velocity.rotate(angle_two_circles)
        velocity2 = self.velocity.rotate(-angle_two_circles)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x , self.position.y , new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)    

        asteroid1.velocity = velocity1 * 1.2
        asteroid2.velocity = velocity2 * 1.2

        
            

        