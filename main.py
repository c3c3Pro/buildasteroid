# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# import everything from a module
# into the current file
from constants import *


def main(): 

    #initialise pygame
    pygame.init()
    #new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        #fill the screen with black color
        pygame.Surface.fill(screen,(0, 0, 0), rect=None)
        #update the full display surface to the screen 
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")    

if __name__ == "__main__":
    main()