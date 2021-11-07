import pygame 
from tiles import Tile

class Level:
    def __init__(self, level_map ,surface ):
        self.surface = surface
        self.setup_level(level_map)
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        for row in layout:
            print(row)

    def run(self):
        self.tiles.draw(self.surface)

