import pygame 
import sys  
from settings import *
from tiles import Tile
# pygame initial setup 
pygame.init()


screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
tile_sprite = pygame.sprite.Group(Tile((100,100),200))
# main loop
while True :  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill("black")
    tile_sprite.draw(screen)
    pygame.display.update()
    clock.tick(60)    