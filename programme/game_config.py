import pygame

class GameConfig:
    WINDOW_H=640
    WINDOW_W=960
    REGARD_DROIT=False
    REGARD_GAUCHE=False
    Y_PLATEFORM=516
    PLAYER_W = 64
    PLAYER_H = 64
    DT = 0.5
    FORCE_LEFT = -20
    FORCE_RIGHT = -FORCE_LEFT
    GRAVITY = 9.81
    FORCE_JUMP = -100

    def init():
        GameConfig.BACKGROUND_IMG=pygame.image.load('../assets/background.png')
        GameConfig.STANDING_IMG=pygame.image.load('../assets/Imageworms/w1.png')
        GameConfig.STANDING_IMG_REVERSE=pygame.transform.flip(GameConfig.STANDING_IMG,True,False)
        GameConfig.JUMP_IMG=pygame.image.load('../assets/Imageworms/jumpH.png')