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
        pass

# Game Loop
running = True
while running:
    for event in pg.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

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