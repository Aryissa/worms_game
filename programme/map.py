from numpy.lib.function_base import select
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
    def __init__(self):
        self.matrice=np.zeros((22,30))
        self.matriceRectangle=[]
        for ligne in range(10,21):
            for colone in range(29):
                value=random.randint(0,1)
                self.matrice[ligne][colone]=value
                if(self.matrice[ligne][colone]==1):
                    self.matriceRectangle.append(pygame.Rect(colone*35,ligne*35,35,35))
        
        for ligne in range(10,21):
            for colone in range(29):
                if (self.matrice[ligne][colone]==1 and (self.matrice[ligne-1][colone]==0 and self.matrice[ligne+1][colone]==0 and self.matrice[ligne][colone-1]==0 and self.matrice[ligne][colone+1]==0 )):
                    self.matrice[ligne][colone]=0
                    for element in self.matriceRectangle:
                        if(element==pygame.Rect(colone*35,ligne*35,35,35)):
                            self.matriceRectangle.remove(pygame.Rect(colone*35,ligne*35,35,35))
        
        col=random.randint(0,29)
        lin=random.randint(10,21)
        while (self.matrice[lin][col]==1 and self.matrice[lin+1][col]!=1):
            col=random.randint(0,29)
            lin=random.randint(10,21)


        self.matrice[lin][col]=2
        Map.APPARITIONX=col*21
        Map.APPARITIONY=lin*29
        print(self.matrice)

    def creationMap(self,matrice,window):
        """for ligne in range(21):
            for colone in range(29):
                if(matrice[ligne][colone]==1):
                    if(matrice[ligne-1][colone]==1):
                        window.blit(GameConfig.TERRES,self.matriceRectangle[ligne-1][colone])
                    else:    
                        print(self.matriceRectangle[ligne][colone])
                        window.blit(GameConfig.TERRE,self.matriceRectangle[ligne][colone])
                        print("Tous les carrés", self.TAB_RECT_TERRE) """
        for element in self.matriceRectangle:
            terreDessus=False
            for element2 in self.matriceRectangle:
                x,y=element2.midbottom
                if element.collidepoint(x,y):
                    terreDessus=True
            if(terreDessus==True):
                window.blit(GameConfig.TERRES,element)
            else:
                window.blit(GameConfig.TERRE,element)
        
    def creerPerso(matrice,window,player):
        for ligne in range(10,21):
            for colone in range(29):
                if(matrice[ligne][colone]==2):
                    rectangleplay=pygame.Rect(colone*35,ligne*35,30,30)
                    player.drawe(window,rectangleplay)
    
    def get_Tab(self):
        return self.matriceRectangle
    
    def get_matrice(self):
        return self.matrice
    
    
    

