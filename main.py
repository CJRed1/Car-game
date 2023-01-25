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

# Road

# BG
screen.fill((135, 255, 135))

pg.draw.ellipse(screen, (50, 200, 50), (winWidth/4-25, -winHeight, winWidth/2+50, winHeight*3))
pg.draw.rect(screen, (75, 75, 75), (winWidth/4, 0, winWidth/2, winHeight))

pg.draw.line(screen, (255, 255, 255), (winWidth/4+10, 0), (winWidth/4+10, winHeight), 10)
pg.draw.line(screen, (255, 255, 255), (winWidth/2+winWidth/4-12, 0), (winWidth/2+winWidth/4-12, winHeight), 10)
pg.draw.line(screen, (255, 213, 0), (winWidth/2-5, 0), (winWidth/2-5, winHeight), 10)

pg.display.update()

# Game Loop
running = True
while running:
    for event in pg.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False