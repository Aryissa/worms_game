import pygame
from game_config import *
from move import *



class projectil(pygame.sprite.Sprite):
    RIGHT = 1
    def __init__(self,x,y,vx):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x,
            y,
            GameConfig.PROJECTIL_W,
            GameConfig.PROJECTIL_H)
        self.sprite_count=0
        self.direction=projectil.RIGHT
        self.image =GameConfig.BALLE
        self.mask =GameConfig.BALLE_MASKS
        self.vx = vx
    def advance_state(self):
        self.rect = self.rect.move(self.vx*GameConfig.DT, 0)
    def draw(self, window):
        self.mask = GameConfig.BALLE_MASKS
        window.blit(self.image, self.rect)
        