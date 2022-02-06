import os
import pygame 
from settings import *

class UI: 
    def __init__(self) -> None:
        
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(None , 30)

        # bar setup
        self.health_bar_image = pygame.image.load(os.path.join('../sprites/health_0.png'))
        self.health_bar_image = pygame.transform.scale(self.health_bar_image , (self.health_bar_image.get_width()*2 , self.health_bar_image.get_height()*2))
        self.health_bar_rect = self.health_bar_image.get_rect(topleft = (15,HEIGHT-80))
    def display(self, player):
        self.display_surface.blit(self.health_bar_image , self.health_bar_rect)