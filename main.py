import pygame as pg
from pygame.locals import *
pg.init()

funnycolor = 0
curBG = 0

# Window Size
winWidth = 800
winHeight = 800
winSize = (winWidth, winHeight)
screen = pg.display.set_mode(winSize)

# Title & Icon
pg.display.set_caption("wow")
pg.display.set_icon(pg.image.load('images/macrin.png'))

# BG Color
screen.fill((135, 255, 135))
pg.display.update()

class Car():
    def __init__(self, winParent):
        self.winParent = winParent
        self.image = pg.image.load('images/carmf.png')
        self.x = 400
        self.y = 650
        self.hspeed = 0

    def draw(self):
        self.winParent.fill((135, 255, 135))
        self.winParent.blit(self.image, (self.x, self.y))
        pg.display.flip()

car = Car(screen)
# Game Loop
running = True
while running:
    car.draw()
    car.x += car.hspeed
    for event in pg.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

            if event.key == K_LEFT:
                car.hspeed = -2
            elif event.key == K_RIGHT:
                car.hspeed = 2

            if funnycolor == 0 and event.key == K_h:
                funnycolor = 1
            elif funnycolor == 1 and event.key == K_e:
                funnycolor = 2
            elif funnycolor == 2 and event.key == K_y:
                if curBG == 0:
                    screen.fill((255, 135, 255))
                    curBG = 1
                else:
                    screen.fill((135, 255, 135))
                    curBG = 0
                pg.display.update()
                funnycolor = 0
            else:
                funnycolor = 0

        if event.type == pg.KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                car.hspeed = 0
    pg.display.update()