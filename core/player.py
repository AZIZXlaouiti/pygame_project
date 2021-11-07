import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self , pos ):
       super().__init__()
       self.image = pygame.Surface((32,64))
       self.image.fill("green")
       self.rect =  self.image.get_rect(topleft = pos)
       self.directions = pygame.math.Vector2(0,0)
    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.directions.x +=1
        elif keys[pygame.K_LEFT]:
            self.directions.x -=1    
        else :
            self.directions.x = 0 
    def update(self):
        self.get_input()
        self.rect.x += self.directions.x    