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

    clock = pygame.time.Clock()
    dt = 0

    player1 = Player(x = SCREEN_WIDTH /2, y = SCREEN_HEIGHT /2, radius= PLAYER_RADIUS, color=(255, 255, 255))

    while True:
        #fill the screen with black color
        pygame.Surface.fill(screen,(0, 0, 0), rect=None)
        #draw the player on the screen
        player1.draw(screen)
        dt = clock.tick(60) / 1000 
        #update the full display surface to the screen 
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #fps is 60. the delta time is converted from milliseconds to seconds
        
        
    

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")    

if __name__ == "__main__":
    main()