import os,pygame
import json
file_dir = 'sprites/'
class Spritesheet:
    def __init__(self,filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(os.path.join('sprites',filename)).convert()
        self.meta_data = self.filename.replace('png','json')
        with open(file_dir + self.meta_data) as f :
            self.data = json.load(f)
        f.close()
    def get_sprite(self , x , y , w , h):
        sprite = pygame.Surface((w,h)) #empty sprite image
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprite_sheet,(0,0),(x , y , w , h))
        return sprite
    def parse_sprite(self,Fname):
        sprite = self.data["frames"][Fname]["frame"]
        x,y,w,h = sprite['x'],sprite['y'],sprite['w'],sprite['h']
        img = self.get_sprite(x,y,w,h)
        return img
         



'''Position: Where you are

Velocity: How fast you are changing your position.
Added to your velocity every time step.

Acceleration: How fast you are changing your velocity.
It should be added to your velocity every time
'''
