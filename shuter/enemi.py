from random import randint
from gamesprite import GameSprite
from const import *
from pygame import *


class Enemy(GameSprite):
    def __init__(self, img, x, y, w, h, speed = SPEED, xp = 1):
        super().__init__(img, x, y, w, h)
        self.speed = speed
        self.rect.x = randint(0, WIN_W - UFO_W)
        self.rect.y = randint(0, 50)
        self.xp = xp
    def update(self, player, skipable = False):
        if self.rect.y >= WIN_H:
            if not skipable:
                player.skip += 1
            self.rect.x = randint(0, WIN_W - UFO_W)
            self.rect.y = randint(0, 50)
        self.rect.y += self.speed 
        

