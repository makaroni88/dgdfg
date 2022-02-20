from pygame import *
from random import randint



class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
class Player(Gamesprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        
class Enemy(Gamesprite):
    deriction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.deriction = 'right'
        if self.rect.x  >= win_width - 85:
            self.deriction = 'left'

        if self.deriction == 'left':
            self.rect.x  -= self.speed
        else:
            self.rect.x += self.speed

class wall(sprite.Sprite):
    def __init__(self, color, wall_x, wall_width):
        super.__init__()
        self.color_1 = color_1
        self.image = Surface((self.width, self.height))
        self.imgae.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))





win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))


player = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 2)
final = Gamesprite("treasure.png", win_width - 120,win_height - 80,0)


game = True
clock = time.Clock()
FPS = 60

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background,(0,0))
    player.update()
    monster.update()
    display.update()
    clock.tick(FPS)