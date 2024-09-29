# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# import everything from a module
# into the current file
from asteroid import Asteroid
from constants import *
from player import *
from circleshape import *
from asteroidfield import AsteroidField
from shot import Shot

def main(): 

    #initialise pygame
    pygame.init()
    #new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #creating four groups:
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #grouping the objects together:
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    #spawn asteroids
    asteroid_field = AsteroidField()

    #instantiate a player object
    player1 = Player(x = SCREEN_WIDTH /2, y = SCREEN_HEIGHT /2, radius= PLAYER_RADIUS, color=(255, 255, 255))

    #initialise time
    clock = pygame.time.Clock()
    #initialise delta time
    dt = 0

    running = True
    
    while running:
        #closing the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #calculate delta time
        #fps is 60. the delta time is converted from milliseconds to seconds
        dt = clock.tick(60) / 1000
        #fill the screen with black color
        screen.fill((0, 0, 0))     
        #update and respawn asteroids
        asteroid_field.update(dt)
        #update all other objects:
        updatable.update(dt) 
        #shooting asteroids:
        for shot in shots:
            for asteroid in asteroids:
                if shot.collide(asteroid):
                    asteroid.split() 
                    shot.kill()
                    asteroid.kill()
        #quit the game if the player hits an asteroid:
        for asteroid in asteroids:
            if asteroid.collide(player1):
                print("Game Over!")
                running = False
        #draw the player on the screen
        for sprite in drawable:
            sprite.draw(screen)
        
        #update the full display surface to the screen 
        pygame.display.flip()
        
      

if __name__ == "__main__":
    main()