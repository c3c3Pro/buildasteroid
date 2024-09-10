from circleshape import *
from constants import *

class Asteroid:
    def __init__(self, x, y, radius):
        #overriding draw() method
        pygame.draw.circle(center=(x, y), radius=ASTEROID_MAX_RADIUS, width=2)
        