import pygame
from settings import *
class Player(pygame.sprite.Sprite):
    def __init__(self , pos , groups ):
       super().__init__(groups)
       self.image = pygame.Surface((tile_size//2 , tile_size))
       self.image.fill('white')
       self.rect = self.image.get_rect(topleft = pos)