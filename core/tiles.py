import pygame 
class Tile(pygame.sprite.Sprite):
    def __init__(self , pos , size ):
         super().__init__()
         # image/pygame.Surface don't have pos 
         # --> you have to store the blit pos in a rect 
         self.image = pygame.Surface((size , size))
         self.image.fill("red")
         # get_rect --> create a new rect with size of self.image and pos  
         self.rect = self.image.get_rect(topleft = pos) 
    def update(self , shift):
        # camera shift
        self.rect.x += shift[0]
        self.rect.y += shift[1]
        