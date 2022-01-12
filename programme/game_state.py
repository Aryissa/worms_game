from projectil import *
from worms import *
from terrain import *
import random
from map import *
class GameState :
    def __init__(self):
        self.time_till_new_projectil = GameConfig.TICKS_BETWEEN_PROJECTIL
        self.map=Map()   #MODIFIER PARTOUT OU IL Y A MAP
        self.player = Worms(Map.APPARITIONX,Map.APPARITIONY,self.map)
        self.player2 = Worms(random.randint(0,GameConfig.WINDOW_W),random.randint(0,GameConfig.WINDOW_H),self.map)  
        self.joueursuivant = False
        self.tourjoueur=1
        self.player.setactive()

        
        
    def draw(self,window) :
        window.blit(GameConfig.BACKGROUND_IMG,(0,0))
        self.map.creationMap(self.map,window)
        #Map.creerPerso(self.map,window,self.player)
        self.player.draw(window)
        self.player2.draw(window)
        self.player.draw_proj(window)
    def advance_state(self,next_move):
        clock=pygame.time.Clock()
        keys = pygame.key.get_pressed()
        self.player.advance_state(next_move)
        self.player2.advance_state(next_move)
        if (self.player.projectile==None and self.player.tire_proj):
            self.player.lauch_proj()
        if not(self.player.projectile==None):
            self.player.projectile.advance_state(next_move)
        self.puissance=0

    def tour(self) :
         if self.player.ajouer == True:
            self.player.setdesactive()
            self.player.ajouer=False
            print(self.tourjoueur)
            if self.tourjoueur<len(self.listplayer):
                self.player = self.listplayer[self.tourjoueur]
                self.player.setactive()
                print("Changement joueur",self.tourjoueur)
            else :
                self.tourjoueur =0


            
        

        
