import pygame
import time
import math
from game_config import *
from move import *



class projectil(pygame.sprite.Sprite):
    RIGHT = 1
    def __init__(self,x,y,velocity,angle):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        
        self.angle = math.radians( angle )
        self.start_time = pygame.time.get_ticks()
        self.rect = pygame.Rect(x,y,GameConfig.PROJECTIL_W,GameConfig.PROJECTIL_H)
        self.sprite_count=0
        self.direction=projectil.RIGHT
        self.image =GameConfig.BALLE
        self.mask =GameConfig.BALLE_MASKS

        self.vx = velocity * math.sin( self.angle )
        self.vy = velocity * math.cos( self.angle )
    

    def advance_state(self):
        print(self.rect.y)
        
        self.rect.x+=self.vx
        self.vy += GameConfig.GRAVITY*GameConfig.DT
        self.rect.y +=self.vy
        self.isdead()
          
            

    def draw(self, window):
        self.temp= time.time()
        self.mask = GameConfig.BALLE_MASKS
        window.blit(self.image, self.rect)

    def isdead(self):
        if self.rect.y > 1000:
            print("is dead fonctionne")
            return True
        else : return False
        
        