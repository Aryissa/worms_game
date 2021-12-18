from projectil import *
from worms import *
from terrain import *
import random
class GameState :
    def __init__(self):
        self.projectil=[]
        self.time_till_new_projectil = GameConfig.TICKS_BETWEEN_PROJECTIL   
        self.player = Worms(20)
    def draw(self,window) :
        window.blit(GameConfig.BACKGROUND_IMG,(0,0))
        self.player.draw(window)
        for p in self.projectil:
            p.draw(window)
    def advance_state(self,next_move):
        keys = pygame.key.get_pressed()
        self.player.advance_state(next_move)

        for p in self.projectil:
            p.advance_state()
        if keys[pygame.K_F1]:
            self.time_till_new_projectil = GameConfig.TICKS_BETWEEN_PROJECTIL
            vx = GameConfig.BAT_MAX_SPEED
            y = self.player.vy+500 #GameConfig.Y_PLATEFORM-GameConfig.PLAYER_H+5
            print(self.player.vx)
            print(self.player.vy)
            self.projectil.append(projectil(20,y,vx))
            
        

        
