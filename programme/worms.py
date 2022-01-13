import pygame
import time
from math import *
from game_config import *
from game_state import *
from move import *
from map import *
from grenade import *
from projectil import *


class Worms(pygame.sprite.Sprite):
    TERRE_COURANT=None
    def __init__(self,x,y,map):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x,y-GameConfig.PLAYER_H,GameConfig.PLAYER_W,GameConfig.PLAYER_H) 
        Worms.TERRE_COURANT=self.rect.top+35
        self.image = GameConfig.STANDING_IMG
        self.vx = 0     #force du worms en x
        self.map=map    #map  
        self.vy = 0     #force du worms en x
        self.temp = 0
        self.y=y    #position en y
        self.x=x    #position en x
        self.jump=False #savoir s'il saute
        self.projectile=None    #si le projectile est créer ou pas
        self.imageBalle =GameConfig.BALLE   
        self.mask =GameConfig.BALLE_MASKS
        self.puissance=10   #puissance de la munition ou de la grenade
        self.click_gauche=False 
        self.tire_proj=False    #si on tire ou pas
        self.tour_joueur=False  #si c'est son tour ou pas
        self.choixArme=0 #0 si rocket, si 1 alors grenade
        self.cpt=0  #compteur de temps
        self.window=pygame.display.set_mode((GameConfig.WINDOW_W,GameConfig.WINDOW_H))
        self.vivant=True #savoir si le worms est vivant 
        

    


    def draw_proj(self,window): #dessiner le projectile
        if self.tire_proj:
            self.projectile.draw(window)

    def lauch_proj(self): #création du projet
        #Angle du tire par rapport au curseur
        x,y=pygame.mouse.get_pos() 
        hypothenus=sqrt(((self.rect.x-x)**2)+((self.rect.y-y)**2))
        x_adj=x
        y_adj=self.rect.y
        adjacent=sqrt(((self.rect.x-x_adj)**2)+((self.rect.y-y_adj)**2))
        angle=math.acos(adjacent/hypothenus) #formule de trigonométrie sur les triangle
        #Savoir si on tire un projectile ou une grenade
        if(self.choixArme==0):
            #création du projectile
            self.projectile=Projectil(self,self.puissance,math.degrees(angle),self.map)
        if(self.choixArme==1):
            #création de la grenade
            self.projectile=Grenade(self,self.puissance,math.degrees(angle),self.map)


    
    def draw(self,window):#dessine le worms
        if(self.vivant):#s'il est vivant
            window.blit(self.image,self)

    def drawe(self,window,rectangle):
        window.blit(self.image,rectangle) 

    def on_ground(self):#savoir s'il a réatérit sur la terre
        if self.vy==0:
            return True
        else:
            return False            

    def majSol(self): #savoir s'il est sur la terre
        for terre in self.map.get_Tab(): #pour tous les bloques dans ma map
            if terre.collidepoint(self.rect.midbottom[0],self.rect.midbottom[1]+10):#verifie si le bas du worms et sur la terre   
                Worms.TERRE_COURANT=terre.top#la terre où le worms se trouve
                self.jump=False
                return True
        Worms.TERRE_COURANT=GameConfig.WINDOW_H
        return False

    #Les différente collision entre la terre et le worms

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


    #Les différents mouvement que peux faire le Worms
    def advance_state(self,next_move) :
# Acceleration
        fx = 0
        fy = 0
        self.cpt+=1 #compteur de temps prend +1
        Worms.majSol(self)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.cpt>10:   #Changement d'arme
            if(self.choixArme==1):
                self.choixArme=0
                self.cpt=0
            else:
                self.choixArme=1
                self.cpt=0

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
        
        if not next_move.tire and self.click_gauche:
            self.tire_proj=True
            self.click_gauche=False

        if self.projectile!=None:
            if self.projectile.isdead():
                self.projectile.explosion()
                self.projectile=None
                self.tire_proj=False
                self.puissance=10
                self.tour_joueur=False

# Vitesse

        if self.majSol() and self.on_ground() :
            self.vy = fy*GameConfig.WORMS_DT
           
        else :
            self.vy = self.vy+GameConfig.GRAVITY*GameConfig.WORMS_DT
        self.vx = fx*GameConfig.WORMS_DT
# Position
        x = self.rect.left
        vx_min = -x/GameConfig.WORMS_DT
        vx_max = (GameConfig.WINDOW_W-GameConfig.PLAYER_W-x)/GameConfig.WORMS_DT
        self.vx = min(self.vx,vx_max)
        self.vx = max(self.vx,vx_min)

        y = self.rect.top
        vy_max = (Worms.TERRE_COURANT-GameConfig.PLAYER_H-y)/GameConfig.WORMS_DT
        self.vy = min(self.vy,vy_max)

        self.rect = self.rect.move(self.vx*GameConfig.WORMS_DT,self.vy*GameConfig.WORMS_DT)

    
        if(self.rect.y==669): #si le worms tombe dans le vide alors il meurt
            self.vivant=False

    def get_rect_worms(self):
        return self.rect

