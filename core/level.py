import pygame 
from tiles import Tile
from settings import *
class Level:
    def __init__(self, level_map ,surface ):
        self.surface = surface
        self.setup_level(level_map)
        self.world_shift = 0
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        for index_row , row in enumerate(layout):
            for index_col ,col in enumerate(row): 
               print(index_row, index_col,col)
               if col == 'X':
                   y = index_row * tile_size
                   x = index_col * tile_size
                   tile = Tile((x,y),tile_size)
                   self.tiles.add(tile)

    def run(self):
        #adding camera by offsetting the world(i.e sprite Group) 
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.surface)
