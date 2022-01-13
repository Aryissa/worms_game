import pygame
import time
import math
from game_config import *
from move import *



class Projectil(pygame.sprite.Sprite):
    def __init__(self,player,velocity,angle,map):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.map=map
        self.angle = (math.pi/2)+(math.radians( angle ))
        self.rect = pygame.Rect(player.rect.x,player.rect.y,GameConfig.PROJECTIL_W,GameConfig.PROJECTIL_H)
        self.sprite_count=0
        self.player=player

        
        self.direction=(pygame.mouse.get_pos()[0]-self.rect.x)/abs(pygame.mouse.get_pos()[0]-self.rect.x)
        self.image =GameConfig.BALLE
        self.mask =GameConfig.BALLE_MASKS
        self.puissance=0
        self.rect.x=player.rect.x
        self.rect.y=player.rect.y
        self.vx = velocity * math.sin( self.angle )
        self.vy = velocity * math.cos( self.angle )
        self.acceleration_x=map.vent
   
   
    def advance_state(self):

        if(self.direction>0):  
            self.vx+=self.acceleration_x*GameConfig.BULLET_DT
            self.rect.x+=self.vx
            self.vy += GameConfig.GRAVITY*GameConfig.BULLET_DT
            self.rect.y +=self.vy
        else:
            self.vx+=self.acceleration_x*GameConfig.BULLET_DT
            self.rect.x-=self.vx
            self.vy += GameConfig.GRAVITY*GameConfig.BULLET_DT
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

    def explosion(self):
        if(self.isdead()):
            rectangle_explosion=pygame.Rect(self.rect.x,self.rect.y,50+self.puissance*0.3,50+self.puissance*0.3)
            if(self.player.rect.colliderect(rectangle_explosion)):
                self.player.vivant=False
            for terre in self.map.get_Tab():
                if (terre.colliderect(rectangle_explosion)):
                    self.map.matriceRectangle.remove(terre)
                
        
