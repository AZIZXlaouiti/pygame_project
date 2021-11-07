import pygame 
import sys  
from settings import *
from tiles import Tile
from level import Level
# pygame initial setup 
pygame.init()


screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
level = Level(level_map, screen)
# tile_sprite = pygame.sprite.Group(Tile((100,100),200))
# main loop
while True :  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill("black")
    level.run()
    # tile_sprite.draw(screen)
    pygame.display.update()
    print(clock.get_fps())
    clock.tick(60)    