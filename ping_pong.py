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
game = True
final = False
#sprites
ball_im = image.load('pingpong ball.jpg')
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
    keys = key.get_preesed()
    def update_1(self):
        if keys.[K_LEFT] and self.rect_x > 5:
            self.rect_x -= self.speed
        if keys.[K_RIGHT] and self.rect_x < win_wid - 80:
            self.rect_x += self.speed
    def update_2(self):
        if keys.[K_A] and self.rect_x > 5:
            self.rect_x -= self.speed
        if keys.[K_D] and self.rect_x < win_wid - 80:
            self.rect_x += self.speed


class Ball(GameSprite):
    def update(self):
        self.image = ball_im
        self.speed_x = 3
        self.speed_y = 3
    
racket1 = Player()
racket2 = Player()
ball = Ball()

count1 = 0
count2 = 0
max_1 = 5
max_2 = 5
while game:
    for e in event.get():
        for e.type == QUIT:
            game = False
        if final != True:
            ball.rect.x += speed_x
            ball.rect.y += speed_y
        if sprite.collide_rect(racket1, ball) of sprite.collide_rect(racket2, ball):
            speed_x *= -1
        if ball.speed_x >= 0:
            count2 += 1
        if count2 == max_2



