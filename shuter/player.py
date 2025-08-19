from gamesprite import GameSprite
from const import *
from pygame import *
from buling import *


class Player(GameSprite):
    def __init__(self, img, x, y, w, h, speed = SPEED, xp = XP):
        super().__init__(img, x, y, w, h)
        self.speed = speed
        self.xp = xp
        self.killed = 0
        self.skip = 0
        self.bulingi = sprite.Group()

    def update(self, left, right):
        keys = key.get_pressed()
        if self.rect.x > 0 and keys[left]:
            self.rect.x -= self.speed
        if self.rect.right < WIN_W and keys[right]:
            self.rect.x += self.speed

    def doza(self):
        buling = Buling('src/bullet.png', self.rect.centerx, self.rect.y, DOZA_W, DOZA_H)
        self.bulingi.add(buling)