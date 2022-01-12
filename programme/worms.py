import pygame
import time
from math import *
from game_config import *
from game_state import *
from move import *
from map import *
from projectil import *


class Worms(pygame.sprite.Sprite):
    TERRE_COURANT=None
    def __init__(self,x,y,map):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x,y-GameConfig.PLAYER_H,GameConfig.PLAYER_W,GameConfig.PLAYER_H) #J'AI MODIFIER ICI
        Worms.TERRE_COURANT=self.rect.top+35
        self.image = GameConfig.STANDING_IMG
        self.vx = 0
        self.map=map
        self.vy = 0
        self.temp = 0
        self.y=y
        self.x=x
        self.jump=False
        self.projectile=None
        self.imageBalle =GameConfig.BALLE
        self.mask =GameConfig.BALLE_MASKS
        self.puissance=10
        self.click_gauche=False
        self.tire_proj=False
        self.tour_joueur=False
        
    def draw_proj(self,window):
        if self.tire_proj:
            self.projectile.draw(window)

    def lauch_proj(self):
        x,y=pygame.mouse.get_pos()
        hypothenus=sqrt(((self.rect.x-x)**2)+((self.rect.y-y)**2))
        x_adj=x
        y_adj=self.rect.y
        adjacent=sqrt(((self.rect.x-x_adj)**2)+((self.rect.y-y_adj)**2))
        angle=math.acos(adjacent/hypothenus)
        print(math.degrees(angle))
        self.projectile=Projectil(self,self.puissance,math.degrees(angle),self.map)


    
    def draw(self,window):
        window.blit(self.image,self)

    def drawe(self,window,rectangle):
        window.blit(self.image,rectangle) 

    def on_ground(self):
        if self.vy==0:
            return True
        else:
            return False            

    def majSol(self): #MODIFIER PAR RAPPORT AU COLLISION DE RECTANGLE
        for terre in self.map.get_Tab():
            if terre.collidepoint(self.rect.midbottom[0],self.rect.midbottom[1]+10): #rectangle de dessous du verre collision rectangle de dessous du bloc      
                Worms.TERRE_COURANT=terre.top
                self.jump=False
                return True
        Worms.TERRE_COURANT=GameConfig.WINDOW_H
        return False

    def colli_cote_droite(self):
        for terre in self.map.get_Tab():
            if terre.collidepoint(self.rect.midright):
                return True
        return False 
        
    def colli_cote_gauche(self):
        for terre in self.map.get_Tab():
            if terre.collidepoint(self.rect.midleft):
                return True
        return False
    
    def colli_cote_haut(self):
        for terre in self.map.get_Tab():
            if terre.collidepoint(self.rect.midtop[0],self.rect.midtop[1]+10):
                return True
        return False

    def advance_state(self,next_move) :
# Acceleration
        fx = 0
        fy = 0
        Worms.majSol(self)
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
            if(self.colli_cote_gauche()):
                fx=0
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
            if(self.colli_cote_droite()):
                fx=0
            GameConfig.REGARD_GAUCHE==False
            GameConfig.REGARD_DROIT==True
        else:
            self.temp=time.time()

        if next_move.jump:
            if(self.colli_cote_haut()):
                self.jump=False
                self.vy=0
            else:
                timed = time.time()
                fy = GameConfig.FORCE_JUMP
                self.image = GameConfig.JUMP_IMG
                self.jump=True
        
        if next_move.tire and self.tire_proj==False:
            self.click_gauche=True
            self.puissance+=5
            print("PUISSANCE",self.puissance)
        
        if not next_move.tire and self.click_gauche:
            self.tire_proj=True
            self.click_gauche=False

        if self.projectile!=None:
            if self.projectile.isdead():
                self.projectile=None
                self.tire_proj=False
                self.puissance=10
                self.tour_joueur=False


            



            
# Vitesse

        if self.majSol() and self.on_ground() :
            self.vy = fy*GameConfig.DT
           
        else :
            self.vy = self.vy+GameConfig.GRAVITY*GameConfig.DT
        self.vx = fx*GameConfig.DT
# Position
        x = self.rect.left
        vx_min = -x/GameConfig.DT
        vx_max = (GameConfig.WINDOW_W-GameConfig.PLAYER_W-x)/GameConfig.DT
        self.vx = min(self.vx,vx_max)
        self.vx = max(self.vx,vx_min)

        y = self.rect.top
        vy_max = (Worms.TERRE_COURANT-GameConfig.PLAYER_H-y)/GameConfig.DT
        self.vy = min(self.vy,vy_max)

        self.rect = self.rect.move(self.vx*GameConfig.DT,self.vy*GameConfig.DT)


