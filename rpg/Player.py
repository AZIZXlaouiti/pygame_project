import pygame
from utils.spriteSheet import Spritesheet
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision):
        super().__init__(groups)
        self.load_animation()
        # self.image = pygame.Surface((tile_size//2, tile_size))
        self.frame = 0
        self.image = self.animation["run"][self.frame]
        # self.image.fill('blue')
        self.rect = self.image.get_rect(topleft=pos)
        
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.gravity = 0.8
        self.jump_speed = -16
        self.collision_sprites = collision
        self.on_floor = True
        self.switch = False
        self.status = 's'
    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0
        
    def apply_switch(self):
        if self.switch :
           self.image.fill('blue')
        else :
            self.image.fill('black')
               
        self.switch = not self.switch   
    def add_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        
    def load_animation(self):
        self.animation = {'idle':[],'run':[],'jump':[],'fall':[]}
        right = Spritesheet('idle.png')
        # self.animation['run'].append(pygame.draw.rect(self.sprite_sheet, 'green', (20, 20, 10, 20), 1))
        for i in range (4):
            self.animation["run"].append(right.parse_sprite(f'frame_{i}.png'))  
    def jump(self):
        self.direction.y = self.jump_speed
    def animate(self):
    # -------------------------------------------------------------------
        self.frame = (self.frame + 0.25)% len(self.animation['run'])
        self.image = self.animation['run'][int(self.frame)]  
    # -------------------------------------------------------------------
    def collision(self, direction):
        if direction == 'H':
            for sprite in self.collision_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
        if direction == 'V':
            for sprite in self.collision_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                        self.direction.y = 0
                        self.on_floor = True
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
                        self.direction.y = 0
            if self.on_floor and self.direction.y != 0 :
                self.on_floor = False            
    def move(self, speed):
        if self.direction.magnitude() != 0:
            # set the length to constant so it will have the smae speed across input
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * speed
        self.collision('H')

        self.rect.y += self.direction.y * speed
        self.collision('V')
        self.add_gravity()
    def update(self):
        self.get_input()
        self.move(self.speed)
        self.animate()
