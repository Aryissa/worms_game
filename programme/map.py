import pygame
import numpy as np
import random
from game_config import *
from game_state import *
from worms import *

#ligne à gauche / colonne à droite
class Map:
    APPARITIONX=0
    APPARITIONY=0
    def init():
        matrice=np.zeros((22,30))
        for ligne in range(21):
            for colone in range(29):
                value=random.randint(0,1)
                matrice[ligne][colone]=value

        col=random.randint(0,29)
        lin=random.randint(0,21)
        while (matrice[lin][col]==1 and matrice[lin+1][col]!=1):
            col=random.randint(0,29)
            lin=random.randint(0,21)


        matrice[lin][col]=2
        Map.APPARITIONX=col*35
        Map.APPARITIONY=lin*35
        print(matrice)
        return matrice

    def creationMap(matrice,window):
        for ligne in range(21):
            for colone in range(29):
                if(matrice[ligne][colone]==1):
                    rectangle=pygame.Rect(colone*35,ligne*35,30,30)
                    if(matrice[ligne-1][colone]==1):
                        window.blit(GameConfig.TERRES,rectangle)
                    else:    
                        window.blit(GameConfig.TERRE,rectangle)
        
    def creerPerso(matrice,window,player):
        for ligne in range(21):
            for colone in range(29):
                if(matrice[ligne][colone]==2):
                    rectangleplay=pygame.Rect(colone*35,ligne*35,30,30)
                    player.drawe(window,rectangleplay)
    
    
    

