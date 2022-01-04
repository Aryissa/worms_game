from projectil import *
from worms import *
from terrain import *
import random
from map import *
class GameState :
    def __init__(self):
        self.listprojectil=[]
        self.time_till_new_projectil = GameConfig.TICKS_BETWEEN_PROJECTIL
        self.map=Map.init()   #MODIFIER PARTOUT OU IL Y A MAP
        self.player = Worms(Map.APPARITIONX,Map.APPARITIONY) 
        
    def draw(self,window) :
        window.blit(GameConfig.BACKGROUND_IMG,(0,0))
        Map.creationMap(self.map,window)
        Map.creerPerso(self.map,window,self.player)
        self.player.draw(window)
        for p in self.listprojectil:
            p.draw(window)
    def advance_state(self,next_move):
        keys = pygame.key.get_pressed()
        self.player.advance_state(next_move)
        

        for p in self.listprojectil:    
            p.advance_state()
        for event in pygame.event.get():    
            if event.type == pygame.MOUSEBUTTONUP:
                print(event.type)
                self.time_till_new_projectil = GameConfig.TICKS_BETWEEN_PROJECTIL
                vx = GameConfig.BAT_MAX_SPEED
               
                print(self.player.vx)
                print(self.player.vy) #Force , angle 100 = horizon 
                self.listprojectil.append(projectil(self.player.rect.x,self.player.rect.y,25,150))
                print(self.listprojectil)
        for p in self.listprojectil:
                    if p.isdead():
                        self.listprojectil.remove(p)

                        

            
        

        
