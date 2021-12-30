import pygame

from game_config import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self,vx,image,worms):
        super().__init__()
        self.velocity = vx
        self.worms = worms
        self.image = image
        self.angle = 0
        self.image = pygame.transform.scale(self.image,(15,15))
        self.origine_image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = worms.rect.x + 26
        self.rect.y = worms.rect.y +10

    def rotate(self):
        #tourner la bullet
        self.angle += 20
        self.image = pygame.transform.rotozoom(self.origine_image,self.angle,1)

    def remove(self):
        self.worms.all_bullets.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rect.y += self.velocity
        self.rotate()

        #vérifier si la bullet est hors écran
        if self.rect.x > 1000:
            #supprimer la bullet
            self.remove()