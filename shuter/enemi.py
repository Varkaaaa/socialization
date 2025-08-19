from random import randint
from gamesprite import GameSprite
from const import *
from pygame import *


class Enemy(GameSprite):
    def __init__(self, img, x, y, w, h, speed = SPEED,):
        super().__init__(img, x, y, w, h)
        self.speed = speed
        self.rect.x = randint(0, WIN_W - UFO_W)
        self.rect.y = randint(0, 50)
    def update(self, player):
        if self.rect.y >= WIN_H:
            player.skip += 1
            self.rect.x = randint(0, WIN_W - UFO_W)
            self.rect.y = randint(0, 50)
        self.rect.y += self.speed 

