from worms import *
from terrain import *
class GameState :
    def __init__(self):
        self.player = Worms(20)
    def draw(self,window) :
        window.blit(GameConfig.BACKGROUND_IMG,(0,0))
        self.player.draw(window)
    def advance_state(self,next_move):
        self.player.advance_state(next_move)