from pygame import*
font.init()
from random import randint
win_wid = 600
win_hei = 500
clock = time.Clock()
FPS = 60
window = display.set_mode((win_wid, win_hei))
display.set_caption("Ping Pong")
game = True
final = False
#sprites
#ball_im = 'ballwhite.png'
#racket_1 = 'racket01.png'
#racket_2 = 'racket01.png'
count1 = 0
count2 = 0
background = (39, 33, 36)
window.fill(background)

class GameSprite(sprite.Sprite):
    def __init__(self, racket_image, racket_x, racket_y, size_x, size_y, racket_speed):
        super().__init__()
        self.image = transform.scale(image.load(racket_image), (size_x, size_y))
        self.speed = racket_speed
        self.rect = self.image.get_rect()
        self.rect_x = racket_x
        self.rect_y = racket_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect_y > 5:
            self.rect_x -= self.speed
        if keys[K_DOWN] and self.rect_y < win_hei - 80:
            self.rect_x += self.speed
    def update_2(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect_y > 5:
            self.rect_x -= self.speed
        if keys[K_d] and self.rect_y < win_hei - 80:
            self.rect_x += self.speed
    
racket1 = Player('racket01.png', 50, -250, 40, 50, 8)
racket2 = Player('racket01.png', 550, -250, 40, 50, 8)
ball = GameSprite('ballwhite.png', 300, -250, 30, 30, 10)

font1 = font.Font(None, 35)
win1 = font1.render("1 PLAYER WINS", True, (163, 21, 28))
win2 = font1.render("2 PLAYER WINS", True, (163, 21, 28))
font2 = font.Font(None, 10)
text1 = font2.render(str(count1), True, (243,246,244))
window.blit(text1, (10,50))
text2 = font2.render(str(count2), True,  (243,246,244))
window.blit(text2, (10, 20))

speed_x = 3
speed_y = 3

max_1 = 5
max_2 = 5
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if final != True:
        window.fill(background)
        racket1.update_1()
        racket2.update_2()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > win_wid-50 or ball.rect.y > 0:
            speed_x *= -1
        if ball.rect.x >= 0:
            count2 += 1
            ball.kill()
            racket1.update_1()
            racket2.update_2()
            ball.update()
        if ball.rect.x >= -600:
            count1 += 1
            ball.kill()
            racket1.update_1()
            racket2.update_2()
            ball.update()
        if count2 == max_2:
            final = True
        if count1 == max_1:
            final = True
        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
