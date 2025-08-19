from pygame import *
from const import *
class Area():
    def __init__(self, x,y, w,h, color = GREEN):
        self.rect = Rect(x,y, w,h)
        self.fill_color = color
    
    def color(self, new_color):
        self.fill_color = new_color
    
    def fill(self, window):
        draw.rect(window, self.fill_color, self.rect)

    def collidepoint(self, x,y):
        return self.rect.collidepoint(x,y)

class Label(Area):
    def __init__(self, x,y, w,h, color = GREEN):
        super().__init__(x,y, w,h, color)

    def set_text(self, text, fon_size = 30, text_color = BLACK):
        #render - превращение в картинку
        self.image = font.SysFont('arial', fon_size).render(text, True, text_color)

    def draw(self, window, x_shift = 10, y_shift = 10):
        self.fill(window)
        window.blit(self.image, (self.rect.x + x_shift, self.rect.y + y_shift))