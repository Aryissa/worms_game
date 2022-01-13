from numpy.lib.function_base import select
import pygame
import numpy as np
import random
from game_config import *
from game_state import *
from worms import *

class Map:
    APPARITIONX=0   #apparition du worms X
    APPARITIONY=0   #apparition du worms Y
    def __init__(self):
        self.vent=random.randint(-5,5) #initialisation du vent sur la map
        self.matrice=np.zeros((22,30))  #création d'une matrice remplit de zéros qui représente notre map
        self.matriceRectangle=[]    #matrice contenant tous les rectangles des bloques dans la map
        #Création de la map en mettant des 1 dans ma matrice représentant les bloques
        for ligne in range(10,21):
            for colone in range(29):
                value=random.randint(0,1)
                self.matrice[ligne][colone]=value
                if(self.matrice[ligne][colone]==1):
                    self.matriceRectangle.append(pygame.Rect(colone*35,ligne*35,35,35)) #création des rectangles
        
        #On enlève les rectangle qui n'ont aucun voisin direct (hors diagonal)
        for ligne in range(10,21):
            for colone in range(29):
                if (self.matrice[ligne][colone]==1 and (self.matrice[ligne-1][colone]==0 and self.matrice[ligne+1][colone]==0 and self.matrice[ligne][colone-1]==0 and self.matrice[ligne][colone+1]==0 )):
                    self.matrice[ligne][colone]=0
                    for element in self.matriceRectangle:
                        if(element==pygame.Rect(colone*35,ligne*35,35,35)):
                            self.matriceRectangle.remove(pygame.Rect(colone*35,ligne*35,35,35))
        
        #Spawn du Worms aléatoire sur l'axe des X
        col=random.randint(0,29)
        lin=11

        self.matrice[lin][col]=2
        Map.APPARITIONX=col*21
        Map.APPARITIONY=lin*29

    #Affichage de map on vérifie sur la matrice si le bloque a un bloque au dessus ou non 
    def creationMap(self,matrice,window):
        for element in self.matriceRectangle:
            terreDessus=False
            for element2 in self.matriceRectangle:
                x,y=element2.midbottom
                if element.collidepoint(x,y):
                    terreDessus=True
            if(terreDessus==True): #s'il a une terre dessus alors on fait apparaitre une terre sans herbe 
                window.blit(GameConfig.TERRES,element)
            else:   #s'il n'a pas de terre dessus alors on fait apparaitre une terre sans herbe 
                window.blit(GameConfig.TERRE,element)


    #appartion du worms à l'endroit aléatoire
    def creerPerso(matrice,window,player):
        for ligne in range(10,21):
            for colone in range(29):
                if(matrice[ligne][colone]==2):
                    rectangleplay=pygame.Rect(colone*35,ligne*35,30,30)
                    player.drawe(window,rectangleplay)
    
    #récupère la matrice de rectangle
    def get_Tab(self):
        return self.matriceRectangle
    
    #récupère la matrice de 1 et de 0 
    def get_matrice(self):
        return self.matrice
    
    
    

