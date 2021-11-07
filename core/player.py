import pygame , os
from sprite import Spritesheet
class Player(pygame.sprite.Sprite):
    def __init__(self , pos ):
       super().__init__()
       self.load_animation()
       self.frame = 0
       self.image = self.animation["run"][self.frame]
       self.rect = self.image.get_rect(topleft = pos)
       self.direction = pygame.math.Vector2(0,0)
       self.speed = 1
       self.gravity = 0.8
       self.jump_speed = -10
       self.last_update = pygame.time.get_ticks()
       self.frame_rate = 0.15
    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x +=1
        elif keys[pygame.K_LEFT]:
            self.direction.x -=1    
        else :
            self.direction.x = 0 
        if keys[pygame.K_SPACE]:
            self.jump() 
    def add_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y    
    def jump(self):
        self.direction.y = self.jump_speed       
    def update(self):
        self.get_input()
        self.animate()
    def load_animation(self):
        self.animation = {'idle':[],'run':[],'jump':[],'fall':[]}
        right = Spritesheet('right.png')
        for i in range (4):
            self.animation["run"].append(right.parse_sprite(f'frame_{i}.png'))  
    def animate(self):
        # now  = pygame.time.get_ticks()
        # if now - self.last_update > self.frame_rate:
        #     self.last_update = now
        #     self.frame += 1
        #     if self.frame >= len(self.animation["run"]):
        #         self.frame = 0
        self.frame = (self.frame + 0.142)% len(self.animation['run'])
        self.image = self.animation['run'][int(self.frame)]

        # x,y = self.direction.x,self.direction.y
        # self.image = self.animation['run'][self.frame]
        # self.rect = self.image.get_rect()
        # self.direction.x,self.direction.y = x , y