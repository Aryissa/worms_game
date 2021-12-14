import pygame
from game_config import *
from game_state import *
from worms import *


def get_next_move():
        next_move = Move()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            next_move.right = True
        if keys[pygame.K_LEFT]:
            next_move.left = True
        if keys[pygame.K_UP]:
            next_move.jump = True
        return next_move

def game_loop(window):
    
    quitting=False
    game_state = GameState()
    while not quitting:
        
        

        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                quitting=True  
        pygame.time.delay(20)  
        game_state.draw(window)
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