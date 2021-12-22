import pygame
import time
class GameConfig:
    WINDOW_H=640
    WINDOW_W=960
    REGARD_DROIT=False
    REGARD_GAUCHE=False
    Y_PLATEFORM=516
    X_PLATEFORM=516
    PLAYER_W = 64
    PLAYER_H = 64
    DT = 0.5
    FORCE_LEFT = -20
    FORCE_RIGHT = -FORCE_LEFT
    GRAVITY = 9.81
    FORCE_JUMP = -100
    PROJECTIL_W = 32
    PROJECTIL_H = 32
    TICKS_BETWEEN_PROJECTIL = 1000
    PROJECTIL_SPEED = 50
    NB_FRAMES_PER_SPRITE_PROJECTIL = 300
    BAT_MAX_SPEED = 30

   


    def init():
        GameConfig.BACKGROUND_IMG=pygame.image.load('assets/background.png')
        GameConfig.STANDING_IMG=pygame.image.load('assets/Imageworms/w1.png')
        GameConfig.STANDING_IMG2=pygame.image.load('assets/Imageworms/w2.png')
        GameConfig.STANDING_IMG3=pygame.image.load('assets/Imageworms/w3.png')
        GameConfig.STANDING_IMG4=pygame.image.load('assets/Imageworms/w4.png')
        GameConfig.STANDING_IMG5=pygame.image.load('assets/Imageworms/w5.png')
        GameConfig.STANDING_IMG_REVERSE=pygame.transform.flip(GameConfig.STANDING_IMG,True,False)
        GameConfig.STANDING_IMG_REVERSE2=pygame.transform.flip(GameConfig.STANDING_IMG2,True,False)
        GameConfig.STANDING_IMG_REVERSE3=pygame.transform.flip(GameConfig.STANDING_IMG3,True,False)
        GameConfig.STANDING_IMG_REVERSE4=pygame.transform.flip(GameConfig.STANDING_IMG4,True,False)
        GameConfig.STANDING_IMG_REVERSE5=pygame.transform.flip(GameConfig.STANDING_IMG5,True,False)
        GameConfig.JUMP_IMG=pygame.image.load('assets/Imageworms/jumpH.png')
        GameConfig.BALLE=pygame.image.load('assets/Imageworms/balle.png')
        GameConfig.BALLE_MASKS = pygame.mask.from_surface(GameConfig.BALLE)
        GameConfig.TERRE=pygame.image.load('assets/Imageworms/terreH.png')
        GameConfig.TERRES=pygame.image.load('assets/Imageworms/terreS.png')
