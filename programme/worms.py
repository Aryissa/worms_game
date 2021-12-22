import pygame
import time
from game_config import *
from game_state import *
from move import *


class Worms(pygame.sprite.Sprite):
    
    def __init__(self,x):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x,GameConfig.Y_PLATEFORM-GameConfig.PLAYER_H,GameConfig.PLAYER_W,GameConfig.PLAYER_H)
        self.image = GameConfig.STANDING_IMG
        self.vx = 0
        self.vy = 0
        self.temp = 0
    def draw(self,window):
        window.blit(self.image,self)

    def drawe(self,window,rectangle):
        window.blit(self.image,rectangle) 

    def on_ground(self):
        if  self.rect.bottom > GameConfig.Y_PLATEFORM:
            
                            
            return True
        return False
        
    def advance_state(self,next_move) :
# Acceleration
        
        fx = 0
        fy = 0
        if self.rect.bottom==508    :

                if GameConfig.REGARD_DROIT==True:
                    self.image = GameConfig.STANDING_IMG
                else:
                    self.image = GameConfig.STANDING_IMG
                if GameConfig.REGARD_GAUCHE==True:
                    self.image = GameConfig.STANDING_IMG_REVERSE
                else:
                    self.image = GameConfig.STANDING_IMG
            
       
        if next_move.left :
            timed = time.time()
            
            if(timed-self.temp<0.2):
                fx = GameConfig.FORCE_LEFT
                self.image = GameConfig.STANDING_IMG_REVERSE
            elif(timed-self.temp<0.4):
                fx = GameConfig.FORCE_LEFT
                self.image = GameConfig.STANDING_IMG_REVERSE2
            elif(timed-self.temp<0.6 ):
                fx = GameConfig.FORCE_LEFT
                self.image = GameConfig.STANDING_IMG_REVERSE3
            elif(timed-self.temp<0.8 ):
                fx = GameConfig.FORCE_LEFT
                self.image = GameConfig.STANDING_IMG_REVERSE4
            elif(timed-self.temp<1 ):
                fx = GameConfig.FORCE_LEFT
                self.image = GameConfig.STANDING_IMG_REVERSE5
            else:
                self.temp=time.time()
                self.image = GameConfig.STANDING_IMG_REVERSE
            GameConfig.REGARD_GAUCHE==True
            GameConfig.REGARD_DROIT==False
        
        elif next_move.right :
            timed = time.time()
            if(timed-self.temp<0.2):
                fx = GameConfig.FORCE_RIGHT
                self.image = GameConfig.STANDING_IMG
            elif(timed-self.temp<0.4):
                fx = GameConfig.FORCE_RIGHT
                self.image = GameConfig.STANDING_IMG2
            elif(timed-self.temp<0.6 ):
                fx = GameConfig.FORCE_RIGHT
                self.image = GameConfig.STANDING_IMG3
            elif(timed-self.temp<0.8 ):
                fx = GameConfig.FORCE_RIGHT
                self.image = GameConfig.STANDING_IMG4
            elif(timed-self.temp<1 ):
                fx = GameConfig.FORCE_RIGHT
                self.image = GameConfig.STANDING_IMG5
            else:
                self.temp=time.time()
                self.image = GameConfig.STANDING_IMG
            GameConfig.REGARD_GAUCHE==False
            GameConfig.REGARD_DROIT==True
        else:
            self.temp=time.time()

        if next_move.jump:
            timed = time.time()
            fy = GameConfig.FORCE_JUMP
            self.image = GameConfig.JUMP_IMG
            
# Vitesse

        if self.on_ground() :
            self.vy = fy*GameConfig.DT
           
        else :
            self.vy = self.vy+GameConfig.GRAVITY*GameConfig.DT
        self.vx = fx*GameConfig.DT
# Position
        self.rect = self.rect.move(self.vx*GameConfig.DT,self.vy*GameConfig.DT)
        x = self.rect.left
        vx_min = -x/GameConfig.DT
        vx_max = (GameConfig.WINDOW_W-GameConfig.PLAYER_W-x)/GameConfig.DT
        self.vx = min(self.vx,vx_max)
        self.vx = max(self.vx,vx_min)

        y = self.rect.top
        vy_max = (GameConfig.Y_PLATEFORM-GameConfig.PLAYER_H-y)/GameConfig.DT
        self.vy = min(self.vy,vy_max)
