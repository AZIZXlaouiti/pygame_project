import os
import pygame 
from settings import * 

class Tile(pygame.sprite.Sprite):
    def __init__(self , pos, groups , key= None):
        super().__init__(groups)
        if not key:
            self.image = pygame.Surface((tile_size , tile_size))
            self.image.fill('black')
        elif key == 'M':
            self.image = pygame.image.load(os.path.join('../sprites/win_0.png'))
            self.image = pygame.transform.scale(self.image , (self.image.get_width()*2 , self.image.get_height()*2))
        self.rect = self.image.get_rect(topleft = pos)
