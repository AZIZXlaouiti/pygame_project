import pygame
from settings import *
class Player(pygame.sprite.Sprite):
    def __init__(self , pos , groups  , collision):
       super().__init__(groups)
       self.image = pygame.Surface((tile_size//2 , tile_size))
       self.image.fill('white')
       self.rect = self.image.get_rect(topleft = pos)

       self.direction = pygame.math.Vector2(0,0)
       self.speed = 5

       self.collision_sprites = collision

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x =1
        elif keys[pygame.K_LEFT]:
            self.direction.x =-1    
        else :
            self.direction.x = 0 
        if keys[pygame.K_UP]:
            self.direction.y =-1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1    
        else :
            self.direction.y = 0     
    def collision(self , direction):
        if direction == 'H':
            for sprite in self.collision_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0 : # moving right
                       self.rect.right = sprite.rect.left
                    if self.direction.x < 0 : 
                        self.rect.left = sprite.rect.right   
        if direction == 'V': 
            for sprite in self.collision_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0 : # moving down
                       self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0 : 
                        self.rect.top = sprite.rect.bottom     
    def move(self , speed):
        if self.direction.magnitude() != 0 :
            self.direction = self.direction.normalize() # set the length to constant so it will have the smae speed across input 
        
        self.rect.x += self.direction.x * speed
        self.collision('H')

        self.rect.y += self.direction.y * speed
        self.collision('V')

        
    def update(self):
        self.get_input()    
        self.move(self.speed)