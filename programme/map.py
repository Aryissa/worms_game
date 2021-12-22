import pygame
import numpy as np
import random
from game_config import *
from game_state import *
from worms import *

class Map:

    def init():
        matrice=np.zeros((30,30))
        for ligne in range(29):
            for colone in range(29):
                value=random.randint(0,1)
                matrice[ligne][colone]=value
        col=colone
        lin=ligne
        while (matrice[col][lin]!=1):
            col=random.randint(0,29)
            lin=random.randint(0,29)
        
        print("ligne",lin)
        print("colone",col)

        matrice[lin][col]=2
        return matrice

    def creationMap(matrice,window):
        for ligne in range(29):
            for colone in range(29):
                if(matrice[ligne][colone]==1):
                    rectangle=pygame.Rect(ligne*29,colone*29,27,27)
                    if(matrice[ligne][colone-1]==1):
                        window.blit(GameConfig.TERRES,rectangle)
                    else:    
                        window.blit(GameConfig.TERRE,rectangle)
        
    def creerPerso(matrice,window,player):
        for ligne in range(29):
            for colone in range(29):
                if(matrice[ligne][colone]==2):
                    rectangleplay=pygame.Rect(ligne*29,colone*29,30,30)
                    player.drawe(window,rectangleplay)
