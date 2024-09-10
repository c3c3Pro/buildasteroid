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
        #update the player state
        player1.update(dt)     
        #fill the screen with black color
        screen.fill((0, 0, 0))
        #pygame.Surface.fill(screen,(0, 0, 0), rect=None)  
        #draw the player on the screen
        player1.draw(screen)
        #update the full display surface to the screen 
        pygame.display.flip()
        
      

if __name__ == "__main__":
    main()