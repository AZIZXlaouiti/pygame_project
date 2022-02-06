import sys
import pygame
from Level import Level
from Player import Player
from __test__.debug import debug
from settings import * 

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((HEIGHT , WIDTH))
        self.clock = pygame.time.Clock()
        self.level = Level(level_map)
        
        # self.player = Player()
    def run(self):
        while True:
            self.screen.fill((226, 226, 221))
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_UP:
                        self.level.player.direction.y = -1
                    elif e.key == pygame.K_t:
                        self.level.player.apply_switch()
                    elif e.key == pygame.K_DOWN:
                        self.level.player.direction.y = 1
                    else:
                       self.level.player.direction.y  = 0    
            self.level.run()
            debug('s' , x =10 ,y=40) 
            pygame.display.update()
            self.clock.tick(FPS)   

if __name__ == '__main__':
    game = Game()
    game.run()
