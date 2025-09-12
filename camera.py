import pygame
class Camera:
    def __init__(self, screen_width, screen_height):
        self.offset = pygame.Vector2(0, 0)
        self.screen_center = pygame.Vector2(screen_width / 2, screen_height /2)
        self.target = None

    def follow_camera(self, target):
        #set which object the camera follows 
        #in this case, use player
        self.target = target

    def update(self):
        if self.target is not None:
            self.offset.x = self.target.position.x - self.screen_center.x
            self.offset.y = self.target.position.y - self.screen_center.y

    def apply(self, position):
        # convert world position to the relative position of an object
        # screen position = world position - camera offset
        return position - self.offset
    