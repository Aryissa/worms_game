import pygame
import time



class GameConfig:
    WINDOW_H=700
    WINDOW_W=1020
    REGARD_DROIT=False
    REGARD_GAUCHE=False
    #Y_PLATEFORM=512
    X_PLATEFORM=516
    PLAYER_W = 21
    PLAYER_H = 31
    WORMS_DT = 0.4
    BULLET_DT=0.4
    GRENADE_DT=0.1
    FORCE_LEFT = -20
    FORCE_RIGHT = -FORCE_LEFT
    GRAVITY = 9.81
    FORCE_JUMP = -100
    PROJECTIL_W = 24
    PROJECTIL_H = 31
    TICKS_BETWEEN_PROJECTIL = 1000
    PROJECTIL_SPEED = 50
    NB_FRAMES_PER_SPRITE_PROJECTIL = 300
    BULLET_MAX_SPEED = 30
    GREY = (51,51,0)
   


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
        GameConfig.GRENADE=pygame.image.load('assets/Imageworms/grenade.png')
        GameConfig.BALLE_MASKS = pygame.mask.from_surface(GameConfig.BALLE)
        GameConfig.TERRE=pygame.image.load('assets/Imageworms/terreH.png')
        GameConfig.TERRES=pygame.image.load('assets/Imageworms/terreS.png')
        GameConfig.FONT20 = pygame.font.Font('assets/BradBunR.ttf',20)
        GameConfig.FONT150 = pygame.font.Font('assets/BradBunR.ttf',150)
