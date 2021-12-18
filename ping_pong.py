from pygame import
mixer.init()
font.init()
from random import randint
win_wid = 500
win_hei = 800
clock = time.clock()
FPS = 60
window = display.set_mode((win_wid, win_hei))
display.set_caption("Ping Pong")
#sprites
ball = image.load('pingpong ball.jpg')
racket_1 = image.load('racket1.png')
racket_2 = image.load('racket2.jpg')

mixer.music.load()
mixer.music.play()
background = transform.scale(image.load("ping pong tab.png"))

class GameSprite(sprite.Sprite):
    def __init__(self, racket_image, racket_x, racket_y, size_x, size_y, racket_speed):
        sprite.Sprite.__init__(self):
        self.iamge = transform.scale(image.load(racket_image), (size_x, size_y))
        self.speed = racket_speed
        self.rect = self.image.get_rect
        self.rect_x = racket_x
        self.rect_y = racket_y
    def reset(self):
        window.blit(self.image, (self.rect_x. self.rect_y))

class Player(GameSprite):
    def update(self):
        keys = key.get_preesed()
        if keys.[K_LEFT] and self.rect_x > 5:
            self.rect_x -= self.speed
        if keys.[K_RIGHT] and self.rect_x < win_wid - 80:
            self.rect_x += self.speed
    
racket1 = Player()
racket2 = Player()

