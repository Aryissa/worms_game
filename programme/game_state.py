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
        self.player.advance_state(next_move)
        for p in self.projectil:
            p.advance_state()
        if self.time_till_new_projectil == 0 :
            self.time_till_new_projectil = GameConfig.TICKS_BETWEEN_PROJECTIL
            vx = GameConfig.BAT_MAX_SPEED
            vx = vx*random.choice([-1,1])
            y =random.randint(
            GameConfig.Y_PLATEFORM-2*GameConfig.PLAYER_H,
            GameConfig.Y_PLATEFORM-GameConfig.PROJECTIL_H)
            if vx < 0 :
                self.projectil.append(projectil(GameConfig.WINDOW_W,y,vx))
            else :
                self.projectil.append(projectil(-GameConfig.PROJECTIL_W,y,vx))
        self.time_till_new_projectil-=1

        
