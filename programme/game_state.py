from projectil import *
from worms import *
from terrain import *
import random
from map import *
from game_config import *
class GameState :


    def __init__(self):
        self.time_till_new_projectil = GameConfig.TICKS_BETWEEN_PROJECTIL
        self.map=Map()
        self.player = Worms(Map.APPARITIONX,Map.APPARITIONY,self.map)
        self.player2 = Worms(random.randint(0,GameConfig.WINDOW_W),350,self.map)
        self.player.tour_joueur=True  
        self.joueursuivant = False
        self.tourjoueur=1
        self.tour1=False

    
    def draw(self,window) :
        window.blit(GameConfig.BACKGROUND_IMG,(0,0))
        

        if(self.player.tour_joueur):
            str_puissance_j1="Puissance_J1: "+str(self.player.puissance)
            if(self.player.choixArme==0):
                str_arm="Arme selectionner: Rocket"
            if(self.player.choixArme==1):
                str_arm="Arme selectionner: Grenade"
            img = GameConfig.FONT20.render(str_arm+"      "+str_puissance_j1,True,GameConfig.GREY)
            display_rect = img.get_rect()
            display_rect.center=(500, 10)
            window.blit(img,display_rect)

        if(self.player2.tour_joueur):
            str_puissance_j2="Puissance_J2: "+str(self.player2.puissance)
            if(self.player2.choixArme==0):
                str_arm="Arme selectionner: Rocket"
            if(self.player2.choixArme==1):
                str_arm="Arme selectionner: Grenade"
            img = GameConfig.FONT20.render(str_arm+"      "+str_puissance_j2,True,GameConfig.GREY)
            display_rect = img.get_rect()
            display_rect.center=(500, 10)
            window.blit(img,display_rect)





        self.map.creationMap(self.map,window)
        self.player.draw(window)
        self.player.draw_proj(window)
        self.player2.draw(window)
        self.player2.draw_proj(window)
    def advance_state(self,next_move):
        
        
        if(self.player.tour_joueur):
            self.player.advance_state(next_move)
            if (self.player.projectile==None and self.player.tire_proj):
                self.player.lauch_proj()
            if not(self.player.projectile==None):
                self.player.projectile.advance_state()
                if(self.player.projectile.isdead()):
                    self.player2.tour_joueur=True
        
        if(self.player2.tour_joueur):
            self.player2.advance_state(next_move)
            if (self.player2.projectile==None and self.player2.tire_proj):
                self.player2.lauch_proj()
            if not(self.player2.projectile==None):
                self.player2.projectile.advance_state()
                if(self.player2.projectile.isdead()):
                    self.player.tour_joueur=True

        
    def get_player_alive(self):
        if self.player.vivant==False or self.player2.vivant==False:
            return True
        else:
            return False

    


            
        

        
