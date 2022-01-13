import pygame
import time
import math
from game_config import *
from move import *



class Grenade(pygame.sprite.Sprite):

    def __init__(self,player,velocity,angle,map):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.map=map
        self.angle = (math.pi/2)+(math.radians( angle ))
        self.rect = pygame.Rect(player.rect.x,player.rect.y,GameConfig.PROJECTIL_W,GameConfig.PROJECTIL_H)
        self.sprite_count=0
        self.player=player
        
        self.direction=(pygame.mouse.get_pos()[0]-self.rect.x)/abs(pygame.mouse.get_pos()[0]-self.rect.x)
        self.image =GameConfig.GRENADE
        self.mask =GameConfig.BALLE_MASKS
        self.puissance=0
        self.rect.x=player.rect.x
        self.rect.y=player.rect.y
        self.vx = velocity * math.sin( self.angle )
        self.vy = velocity * math.cos( self.angle )
        self.acceleration_x=map.vent
        self.cpt=0
   
   
    def advance_state(self):
        self.cpt+=1
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
        for terre in (self.map.get_Tab()):
            if terre.collidepoint(self.rect.x+GameConfig.PROJECTIL_W,self.rect.y):
                self.vy = self.vy *0.9
                self.vx = -self.vx
            elif terre.collidepoint(self.rect.x-GameConfig.PROJECTIL_W,self.rect.y):
                self.vy = self.vy *0.9
                self.vx = -self.vx
            if terre.collidepoint(self.rect.x,self.rect.y+GameConfig.PROJECTIL_H):
                self.vy = self.vy *0.9
                self.vy = -self.vy
            elif terre.collidepoint(self.rect.x,self.rect.y-GameConfig.PROJECTIL_H):
                self.vy = self.vy *0.9
                self.vy = -self.vy
          
            

    def draw(self, window):
        self.temp= time.time()
        self.mask = GameConfig.BALLE_MASKS
        window.blit(self.image, self.rect)

    def isdead(self):
        if self.cpt==30:
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
        
