import pygame
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
    def draw(self,window):
        window.blit(self.image,self)

    def on_ground(self):
        print(self.rect.bottom)
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
            
        if next_move.jump:
            
            fy = GameConfig.FORCE_JUMP
            self.image = GameConfig.JUMP_IMG
        if next_move.left :
            fx = GameConfig.FORCE_LEFT
            self.image = GameConfig.STANDING_IMG_REVERSE
            GameConfig.REGARD_GAUCHE==True
            GameConfig.REGARD_DROIT==False
        elif next_move.right :
            fx = GameConfig.FORCE_RIGHT
            self.image = GameConfig.STANDING_IMG
            GameConfig.REGARD_GAUCHE==False
            GameConfig.REGARD_DROIT==True
            
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
        
    