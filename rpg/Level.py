import pygame
from __test__.debug import debug
from camera.Camera import Camera 
from settings import *
from Tiles import Tile
from Player import Player
class Level:
    def __init__(self , level_map ):

        self.display_surface = pygame.display.get_surface()
        # get the display surface from anywhere 
        # sprites setup
        self.visible_sprites = Camera()
        self.collision_sprites = pygame.sprite.Group()
        self.active_sprites = pygame.sprite.Group()
        # level setup
        self.setup_level(level_map)

    def setup_level(self , level_map):

        for index_row , row in enumerate(level_map):
            for index_col ,col in enumerate(row): 
                y = index_row * tile_size
                x = index_col * tile_size
                if col == 'X':
                   Tile((x,y), [self.visible_sprites , self.collision_sprites])
                if col == 'P':
                   self.player = Player((x,y) , [self.visible_sprites] , self.collision_sprites)
    def run(self):
        self.visible_sprites.draw(self.display_surface)    
        self.visible_sprites.update()
        debug(self.player.direction)