import pygame
import time
import math
from game_config import *
from move import *



class Projectil(pygame.sprite.Sprite):
    RIGHT = 1
    LISTE_PROJ=[]
    def __init__(self,player,velocity,angle,map):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        
        self.angle = (math.pi/2)+(math.radians( angle ))
        self.start_time = pygame.time.get_ticks()
        self.rect = pygame.Rect(player.rect.x,player.rect.y,GameConfig.PROJECTIL_W,GameConfig.PROJECTIL_H)
        self.sprite_count=0

        
        self.direction=(pygame.mouse.get_pos()[0]-self.rect.x)/abs(pygame.mouse.get_pos()[0]-self.rect.x)
        self.image =GameConfig.BALLE
        self.mask =GameConfig.BALLE_MASKS
        self.puissance=0
        self.rect.x=player.rect.x
        self.rect.y=player.rect.y
        self.vx = velocity * math.sin( self.angle )
        self.vy = velocity * math.cos( self.angle )
        self.map=map
   
   
    def advance_state(self,next_move):

        if(self.direction>0):  
            self.rect.x+=self.vx
            self.vy += GameConfig.GRAVITY*GameConfig.DT
            self.rect.y +=self.vy
        else:
            self.rect.x-=self.vx
            self.vy += GameConfig.GRAVITY*GameConfig.DT
            self.rect.y +=self.vy
          
            

    def draw(self, window):
        self.temp= time.time()
        self.mask = GameConfig.BALLE_MASKS
        window.blit(self.image, self.rect)

    def isdead(self):
        for terre in self.map.get_Tab():
            if terre.collidepoint(self.rect.bottomleft) or self.rect.bottomleft[0]>GameConfig.WINDOW_W or self.rect.bottomleft[1]>GameConfig.WINDOW_H:
                return True
        return False
        
