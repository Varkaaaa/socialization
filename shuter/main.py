from pygame import *
from gamesprite import GameSprite
from player import Player
from const import *
from enemi import Enemy
from knopki import Label
# вынесем размер окна в константы для удобства
# W - width, ширина
# H - height, высота

# создание окна размером 700 на 500
window = display.set_mode((WIN_W, WIN_H))
# создание таймера
clock = time.Clock()

# название окна
display.set_caption("Догонялки")

mixer.init()
mixer.music.load('src/space.ogg')
mixer.music.set_volume(0.5)
mixer.music.play(-1)

font.init()
title = font.SysFont('verdana', 70)
win = title.render(
    'YOU WIN', True, GREEN 
)

lost = title.render(
    'YOU LOSE', True, RED
)

standrt = font.SysFont('verdana', 24)


oh_god_damn = mixer.Sound('src/fire.ogg')

# задать картинку фона такого же размера, как размер окна
background = GameSprite("src/galaxy.jpg", 0, 0, WIN_W, WIN_H)
#смэрть = GameSprite("src/смэрть.png", 0, 0, WIN_W, WIN_H)
sprite1 = Player('src/rocket.png', (WIN_W - HERO_W)/2, WIN_H - HERO_H, HERO_W, HERO_H)
ufos = sprite.Group()
for i in range(UFOS):
    kaneki = Enemy('src/ufo.png', x3, y3, UFO_W, UFO_H)
    ufos.add(kaneki)
#соединение размера и загрузка картинки
close = Label(200, 350, 120, 50, RED)
again = Label(200, 250, 120, 50)
close.set_text('закрыть')
again.set_text('гоуууу')
co = Enemy('src/социализация.jpg', 0, 0, 500, 500, 1)

# игровой цикл
finish = True
game = True
rounds = 0
while game:
    if not finish:
        # отобразить картинку фона
        background.draw(window)
        score = standrt.render(f'счёт {sprite1.killed}', True, WHITE)
        window.blit(score, (10, 10))        
        skip = standrt.render(f'пропущенно {sprite1.skip}', True, WHITE)
        window.blit(skip, (10, 40))        
        xp = standrt.render(f'xp {sprite1.xp}', True, WHITE)
        window.blit(xp, (10, 70))
        sprite1.draw(window)
        ufos.draw(window)
        sprite1.bulingi.draw(window)
        #kaneki.update(x3, y3, x3 + 100, x3 + 175, y3 + 50)


        sprite1.update(K_a, K_d)
        ufos.update(sprite1)
        sprite1.bulingi.update()
        sprite_vs_ufo = sprite.spritecollide(
            sprite1, ufos, True
        )

        if sprite_vs_ufo:
            oh_god_damn.play()
            #смэрть.draw(window)
            display.update() 
            time.delay(100)   
            sprite1.xp -= 1 
            kaneki = Enemy('src/ufo.png', x3, y3, UFO_W, UFO_H)
            ufos.add(kaneki)        
            
        doza_vs_ufo = sprite.groupcollide(
            sprite1.bulingi, ufos, True, True
        )


        for c in doza_vs_ufo:
            kaneki = Enemy('src/ufo.png', x3, y3, UFO_W, UFO_H)
            ufos.add(kaneki)  
            sprite1.killed += 1  

        if sprite1.xp <= 0 or sprite1.skip >= MAX_SKIP:
            window.blit(lost, (50, 200))
            finish = True        
            
        if sprite1.killed >= VICTORY:
            window.blit(win, (100, 200))
            rounds += 1
            if rounds >= 3:
                co.draw(window)
            else:
                finish = True
        
    else:
        close.draw(window)
        again.draw(window)


        for ufo in ufos:
            ufo.kill()
        for buling in sprite1.bulingi:
            buling.kill()
        sprite1.kill()
        sprite1 = Player('src/rocket.png', (WIN_W - HERO_W)/2, WIN_H - HERO_H, HERO_W, HERO_H)
        ufos = sprite.Group()
        for i in range(UFOS):
            kaneki = Enemy('src/ufo.png', x3, y3, UFO_W, UFO_H)
            ufos.add(kaneki)



            




    # слушать события и обрабатывать
    for e in event.get():
        if e.type == MOUSEBUTTONDOWN:
            if finish:
                x, y = e.pos
                if close.collidepoint(x, y):
                    game = False
                if again.collidepoint(x, y):
                    finish = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                oh_god_damn.play()
                sprite1.doza()
        # выйти, если нажат "крестик"
        if e.type == QUIT:
            game = False
    # обновить экран, чтобы отобрзить все изменения
    display.update()
    clock.tick(FPS)
