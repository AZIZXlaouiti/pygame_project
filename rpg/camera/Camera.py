import pygame
from settings import *

class Camera(pygame.sprite.Group): 
    def __init__(self) -> None:
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0]//2
        self.half_height = self.display_surface.get_size()[1]//2
        self.offset = pygame.math.Vector2(100 , 50)

    def custom_draw(self , player):
        # get the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height-190
        # blit sprite according to a key and not time of creation
        for sprite in sorted(self.sprites() , key= lambda sprite: sprite.rect.center):
            offset_rect = sprite.rect.topleft  - self.offset
            self.display_surface.blit(sprite.image , offset_rect)    
      