import pygame
from player import Player
from tiles import Tile
from settings import *
class Level:
    def __init__(self, level_map ,surface ):
        self.surface = surface
        self.setup_level(level_map)
        self.world_shift = 0
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for index_row , row in enumerate(layout):
            for index_col ,col in enumerate(row): 
               if col == 'X':
                   y = index_row * tile_size
                   x = index_col * tile_size
                   tile = Tile((x,y),tile_size)
                   self.tiles.add(tile)
               if col == 'P':
                   y = index_row * tile_size
                   x = index_col * tile_size
                   player_sprite = Player((x,y))
                   self.tiles.add(player_sprite)
    def run(self):
        #adding camera by offsetting the world(i.e sprite Group) 
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.surface)
