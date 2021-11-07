import pygame
from player import Player
from tiles import Tile
from settings import *
class Level:
    def __init__(self, level_map ,surface ):
        self.surface = surface
        self.setup_level(level_map)
        self.world_shift = [0,0]
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for index_row , row in enumerate(layout):
            for index_col ,col in enumerate(row): 
                y = index_row * tile_size
                x = index_col * tile_size
                if col == 'X':
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                if col == 'P':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
    def scroll_x(self):
        player_sprite = self.player.sprite 
        player_rect = player_sprite.rect.centerx     
        direction  = player_sprite.direction.x  
        if player_rect < WIDTH / 4  and direction < 0 :
            self.world_shift[0]  =  8
            player_sprite.speed = 0      
        elif player_rect > WIDTH - (WIDTH / 4) and direction >0 :
            self.world_shift[0]  =  -8
            player_sprite.speed = 0        
        else :
            self.world_shift[0] = 0
            player_sprite.speed = 0.3  
    def scroll_y(self):                           
        player_sprite = self.player.sprite 
        player_rect = player_sprite.rect.centery     
        direction  = player_sprite.direction.y  
        if player_rect < HEIGHT / 4  and direction < 0 :
            self.world_shift[1]  =  4
            player_sprite.speed = 0      
        elif player_rect > HEIGHT - (HEIGHT / 4) and direction >0 :
            self.world_shift[1]  =  -4
            player_sprite.speed = 0        
        else :
            self.world_shift[1] = 0
            player_sprite.speed = 0.3          
    def collision_x (self):
        player_sprite = self.player.sprite 
        player_sprite.rect.x += player_sprite.direction.x * player_sprite.speed    
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player_sprite.rect):
                if player_sprite.direction.x < 0 :
                    player_sprite.rect.left = sprite.rect.right 
                elif player_sprite.direction.x > 0 :
                    player_sprite.rect.right = sprite.rect.left    
    def collision_y (self):
        player_sprite = self.player.sprite 
        player_sprite.add_gravity()
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player_sprite.rect):
                if player_sprite.direction.y < 0 :
                    player_sprite.rect.top = sprite.rect.bottom 
                    player_sprite.direction.y = 0
                elif player_sprite.direction.y > 0 :
                    player_sprite.rect.bottom = sprite.rect.top    
                    player_sprite.direction.y = 0
                    

    def run(self):
        # adding camera by offsetting the world(i.e sprite Group) 
        # ---- tiles ----
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.surface)
        self.scroll_x()
        self.scroll_y()

        # ---- player ---
        self.player.update()
        self.collision_y()
        self.collision_x()
        self.player.draw(self.surface)