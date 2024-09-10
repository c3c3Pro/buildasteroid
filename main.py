# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# import everything from a module
# into the current file
from constants import *
from player import *
from circleshape import *

def main(): 

    #initialise pygame
    pygame.init()
    #new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #creating two player groups:
    #the first is updatable:
    updatable = pygame.sprite.Group()
    #the second is drawable:
    drawable = pygame.sprite.Group()
    #adding an instance of a player into two of these groups:
    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    asteroid_field = AsteroidField()

    #instantiate a player object
    player1 = Player(x = SCREEN_WIDTH /2, y = SCREEN_HEIGHT /2, radius= PLAYER_RADIUS, color=(255, 255, 255))
    clock = pygame.time.Clock()
    #delta time initially set to zero
    dt = 0

    while True:
        #closing the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #calculate delta time
        #fps is 60. the delta time is converted from milliseconds to seconds
        dt = clock.tick(60) / 1000
        #fill the screen with black color
        screen.fill((0, 0, 0))     
        #update the player state           
        for sprite in updatable:
            sprite.update(dt) 
        #draw the player on the screen
        for sprite in drawable:
            sprite.draw(screen)
        #update the full display surface to the screen 
        pygame.display.flip()
        
      

if __name__ == "__main__":
    main()