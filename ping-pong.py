from pygame import * #бібліотека

class GameSprite(sprite.Sprite): #батько
   def __init__(self, player_image, player_x, player_y, player_speed, widht, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
 


class Player(GameSprite): #класс гравець наслідує від класса gamesprite
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
#ігрове вікно
back = (200, 255, 255)
win_width, win_height = 600, 500
window = display.set_mode((win_width, win_height))
window.fill(back)
#функія clock і прапорці для стану гри
finish = False
game = True
clock = time.Clock()
FPS = 144
#параметри ракеток
racket1 = Player("racket right.png", 30, 200, 4, 50, 150)
racket2 = Player("racket left.png", 520, 200, 4, 50, 150)
#параметри м'яча
ball = GameSprite("ball.png", 200,200, 4, 50, 50)
#текст та шрифти
font.init()
font = font.Font(None,35)
lose1 = font.render("Перший гравець програв!!", True, (180,0,0))
lose2 = font.render("Другий гравець програв!", True, (180,0,0))
#скорость
speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            #оновлення ракеток та м'яча
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
      #collide
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= -1
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game = False
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200,200))
            game = False
        racket1.reset()
        racket2.reset()
        ball.reset()
#оновлення для стану гри
    display.update()
    clock.tick(FPS)
