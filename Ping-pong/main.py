from pygame import *
from random import (
    randint,uniform
)
from time import time as timer
font.init()


class GameSprite(sprite.Sprite):
    def __init__ (self,player_image,player_x,player_y,x_size,y_size,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(x_size,y_size))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 350:
            self.rect.y += self.speed


window = display.set_mode((700,500))
window.fill((255,255,255))


racket2 = Player("racket.png",5,150,50,150,7.5)
racket = Player("racket.png",645,150,50,150,7.5)
ball = GameSprite("tenis_ball.png",300,200,50,50,7.5)
lose = font.SysFont('Arial',50)
lose1 = lose.render('PLAYER 2 WIN!',True,(2,75,0))
lose2 = lose.render('PLAYER 1 WIN!',True,(2,75,0))

clock = time.Clock()
FPS = 50
game = True
finish = False
speed_x = 3
speed_y = 3


while game:
    if finish == False:
        window.fill((255,255,255))
        racket.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        racket.reset()
        racket2.reset()
        ball.reset()

    
    for e in event.get():
        if e.type == QUIT:
            game = False


    if ball.rect.y < 0 or ball.rect.y > 450:
        speed_y *= -1

    if ball.rect.x < 0:
        finish = True
        window.blit(lose1,(200,200))
    if ball.rect.x > 650:
        finish = True
        window.blit(lose2,(200,200))

    if sprite.collide_rect(racket, ball) or sprite.collide_rect(racket2,ball):
        speed_x *= -1


    display.update()
    clock.tick(FPS)