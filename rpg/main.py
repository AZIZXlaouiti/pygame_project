import sys
import pygame
from Level import Level
from Player import Player
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
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)   

if __name__ == '__main__':
    game = Game()
    game.run()
