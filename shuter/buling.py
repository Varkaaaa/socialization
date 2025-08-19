from random import randint
from gamesprite import GameSprite
from const import *
from pygame import *


class Buling(GameSprite):
    def __init__(self, img, x, y, w, h, speed = SPEED*2,):
        super().__init__(img, x, y, w, h)
        self.speed = speed
    def update(self):
        if self.rect.y <= 0:
            self.kill()
        self.rect.y -= self.speed 
