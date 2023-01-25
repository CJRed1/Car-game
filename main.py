import pygame as pg
from pygame.locals import *
import random as rd
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

# BG
screen.fill((135, 255, 135))

pg.draw.ellipse(screen, (50, 200, 50), (winWidth/4-25, -winHeight, winWidth/2+50, winHeight*3))
pg.draw.rect(screen, (75, 75, 75), (winWidth/4, 0, winWidth/2, winHeight))

pg.draw.line(screen, (255, 255, 255), (winWidth/4+10, 0), (winWidth/4+10, winHeight), 10)
pg.draw.line(screen, (255, 255, 255), (winWidth*0.75-12, 0), (winWidth*0.75-12, winHeight), 10)
pg.draw.line(screen, (255, 213, 0), (winWidth/2-5, 0), (winWidth/2-5, winHeight), 10)

pg.display.update()

# Cars
playerSprite = pg.image.load('images/carmf.png')
playerSpriteCnt = playerSprite.get_rect()
playerSpriteCnt.center = winWidth/2 + winWidth/8, winHeight*0.75

carSprite0 = pg.image.load(f'images/carbad-0.png')
carSpriteCnt0 = carSprite0.get_rect()
carSpriteCnt0.center = winWidth/2 - winWidth/8 + rd.randint(-10, 20), winHeight*0.75 + rd.randint(-50, 50)

carSprite1 = pg.image.load(f'images/carbad-1.png')
carSpriteCnt1 = carSprite0.get_rect()
carSpriteCnt1.center = winWidth/2 - winWidth/8 + rd.randint(-20, 10), winHeight*0.25 + rd.randint(-40, 60)

carSprite2 = pg.image.load(f'images/carbad-2.png')
carSpriteCnt2 = carSprite0.get_rect()
carSpriteCnt2.center = winWidth/2 + winWidth/8 + rd.randint(-15, 15), winHeight*0.25 + rd.randint(-60, 40)

# Game Loop
running = True
while running:
    for event in pg.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    # Car Drawing
    screen.blit(playerSprite, playerSpriteCnt)
    
    screen.blit(carSprite0, carSpriteCnt0)
    screen.blit(carSprite1, carSpriteCnt1)
    screen.blit(carSprite2, carSpriteCnt2)

    pg.display.flip()