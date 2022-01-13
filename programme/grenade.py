import pygame
import time
import math
from game_config import *
from move import *



class Grenade(pygame.sprite.Sprite):

    def __init__(self,player,velocity,angle,map):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.map=map #la map
        self.angle = (math.pi/2)+(math.radians( angle )) #calcul de l'angle en radiant
        self.rect = pygame.Rect(player.rect.x,player.rect.y,18,21)#rectangle de ma grenade
        self.sprite_count=0
        self.player=player#le worms qui tire
        
        self.direction=(pygame.mouse.get_pos()[0]-self.rect.x)/abs(pygame.mouse.get_pos()[0]-self.rect.x) #si la munition par a droite ou a gauche
        self.image =GameConfig.GRENADE
        self.mask =GameConfig.BALLE_MASKS
        self.puissance=velocity #la puissance de la grenade
        self.rect.x=player.rect.x
        self.rect.y=player.rect.y
        self.vx = velocity * math.sin( self.angle ) #calcul de la vitesse en x par rapport a la puissance et à l'angle de tire
        self.vy = velocity * math.cos( self.angle ) #calcul de la vitesse en y par rapport a la puissance et à l'angle de tire
        self.acceleration_x=map.vent    #définissions du vent dans l'acceleration
        self.cpt=0  #compteur de temp
   
   #Avancement de la grenade
    def advance_state(self):
        self.cpt+=1 #incrémentation du temps pour savoir quand est ce que la grenade explose
        #vitesse du projectile
        if(self.direction>0):  
            self.vx+=self.acceleration_x*GameConfig.GRENADE_DT
            self.rect.x+=self.vx
            self.vy += GameConfig.GRAVITY*GameConfig.GRENADE_DT
            self.rect.y +=self.vy
        else:
            self.vx+=self.acceleration_x*GameConfig.GRENADE_DT
            self.rect.x-=self.vx
            self.vy += GameConfig.GRAVITY*GameConfig.GRENADE_DT
            self.rect.y +=self.vy
        #redéfinissions de la vitesse s'il y a une collision entre la terre et la grenade
        for terre in (self.map.get_Tab()):
            if terre.collidepoint(self.rect.x+18,self.rect.y):
                self.vy = self.vy *0.2
                self.vx = -self.vx #par à l'opposé sur l'axe x
            elif terre.collidepoint(self.rect.x-18,self.rect.y):
                self.vy = self.vy *0.2
                self.vx = -self.vx  #par à l'opposé sur l'axe x
            if terre.collidepoint(self.rect.x,self.rect.y+21):
                self.vy = self.vy *0.2
                self.vy = -self.vy  #par à l'opposé sur l'axe y
            elif terre.collidepoint(self.rect.x,self.rect.y-21):
                self.vy = self.vy *0.2
                self.vy = -self.vy  #par à l'opposé sur l'axe y
          
            

    def draw(self, window):#permet de dessiner la grenade
        self.temp= time.time()
        self.mask = GameConfig.BALLE_MASKS
        window.blit(self.image, self.rect)

    def isdead(self): #savoir quand est ce que la grenade explose
        if self.cpt==50:
            return True
        return False
    
    def explosion(self): #que fait la grenade quand elle explose et si elle tue le worms
        if(self.isdead()):
            rectangle_explosion=pygame.Rect(self.rect.x,self.rect.y,50+self.puissance*0.3,50+self.puissance*0.3)
            if(self.player.rect.colliderect(rectangle_explosion)):
                self.player.vivant=False
            for terre in self.map.get_Tab():
                if (terre.colliderect(rectangle_explosion)):
                    self.map.matriceRectangle.remove(terre)
        
