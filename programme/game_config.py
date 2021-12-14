import pygame

class GameConfig:
    WINDOW_H=640
    WINDOW_W=960
    Y_PLATEFORM=516

def init():
    GameConfig.BACKGROUND_IMG=pygame.image.load('../assets/background.png')