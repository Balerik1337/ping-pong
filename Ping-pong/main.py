from pygame import *
from random import (
    randint,uniform
)
from time import time as timer


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
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed


window = display.set_mode((700,500))
window.fill((0,20,60))


clock = time.Clock()
FPS = 50
game = True
finish = False


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)