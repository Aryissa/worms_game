import pygame
from game_config import *
from game_state import *
from worms import *
from move import *
import time
from projectil import * 
from map import *

def display_message(window,text,font_size,x,y) :
    img = GameConfig.FONT20.render(text,True,GameConfig.GREY)
    if font_size == 150:
        img = GameConfig.FONT150.render(text,True,GameConfig.GREY)
    display_rect = img.get_rect()
    display_rect.center=(x,y)
    window.blit(img,display_rect)

def get_next_move():
        next_move = Move()
        keys = pygame.key.get_pressed()
        mouse=pygame.mouse.get_pressed()
        if keys[pygame.K_RIGHT]:
            next_move.right = True
        if keys[pygame.K_LEFT]:
            next_move.left = True
        if keys[pygame.K_UP]:
            next_move.jump = True
        if mouse[0]:
            next_move.tire=True

        return next_move


def game_loop(window):
    cpt=0
    quitting=False
    game_state = GameState()
    game_over=False
    while not game_over and not quitting:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quitting=True  
        pygame.time.delay(20) 
        game_state.draw(window)
        fin_Partie=game_state.get_player_alive()
        if(fin_Partie):
            cpt+=1
            display_message(window,"Fin Partie",150,GameConfig.WINDOW_W/2, GameConfig.WINDOW_H/2-50)
            if(cpt>100):
                game_over=True
        pygame.display.update()     
        next_move = get_next_move()
        game_state.advance_state(next_move)            
        
        

def main():
    pygame.init()
    GameConfig.init()
    
    window=pygame.display.set_mode((GameConfig.WINDOW_W,GameConfig.WINDOW_H))
    pygame.display.set_caption("Worms")
    
    game_loop(window)
    
    pygame.quit()
    quit()

main()
