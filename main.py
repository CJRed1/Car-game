import pygame as pg
from pygame.locals import *
import random as rd
pg.init()
pg.mixer.init()

dt = 0
clock = pg.time.Clock()

# garfield music
garmusic = pg.mixer.music.load('sounds/garmusic.ogg')
pg.mixer.music.set_volume(1)

# Window Size
winWidth = 800
winHeight = 800
winSize = (winWidth, winHeight)
screen = pg.display.set_mode(winSize)

# Title & Icon
pg.display.set_caption("wow")
pg.display.set_icon(pg.image.load('images/macrin.png'))

# a tree
treeList = []
treeXYList = []
for i in range(0, 10):
    tree = pg.image.load(f'images/tree.png')
    treeXY = tree.get_rect()
    treeXY.center = winWidth/8, 200 * i
    if i > 4:
        treeXY.center = winWidth*0.875, 200 * (i-6)
    treeList.insert(i, tree)
    treeXYList.insert(i, treeXY)

# Cars
player = pg.image.load('images/carmf.png')
playerXY = player.get_rect()
playerXY.center = winWidth/2 + winWidth/8, winHeight*0.75

car0 = pg.image.load(f'images/carbad-0.png')
carXY0 = car0.get_rect()
carXY0.center = winWidth/2 - winWidth/8, -250

car1 = pg.image.load(f'images/carbad-1.png')
carXY1 = car0.get_rect()
carXY1.center = winWidth/2 + winWidth/8, -750

garcar = pg.image.load(f'images/garcar.png')
garcarXY = garcar.get_rect()
garcarXY.center = winWidth/2 - winWidth/8, -1750

santiago = pg.image.load(f'images/santiago.png')
santiagoXY = santiago.get_rect()
santiagoXY.center = winWidth/2 + winWidth/8, -2750

# Game Loop
running = True
while running:
    
    # tree movement
    for i in range(0, 10):
        treeXYList[i].y += 1 * dt/2

        if treeXYList[i].y > winHeight:
            treeXYList[i].y = -200      

    # Enemy Car Movement
    carXY0.y += 1 * dt/2
    carXY1.y += 1 * dt/2
    garcarXY.y += 1 * dt/2
    santiagoXY.y += 1 * dt/2

    if carXY0.y > winHeight + 150:
        carXY0.y = -rd.randint(250, 1050)

    if carXY1.y > winHeight + 150:
        carXY1.y = -rd.randint(250, 1050)

    if garcarXY.y > -150 and garcarXY.y < -130 :
        pg.mixer.music.play(-1, 4)
    
    if garcarXY.y > winHeight + 150:
        garcarXY.y = -rd.randint(750, 1750)
        pg.mixer.music.stop()

    if santiagoXY.y > winHeight + 150:
        santiagoXY.y = -rd.randint(1750, 2750)

    carList = [carXY0, carXY1, garcarXY, santiagoXY]
    for i in range(3):
        if playerXY.x == carList[i].x and carList[i].y > playerXY.y - 64:
            print('you ded mf')
            running = False

    for event in pg.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

            if event.key in [K_LEFT, K_a] and playerXY.x > winWidth/4:
                playerXY = playerXY.move(-winWidth/4, 0)

            if event.key in [K_RIGHT, K_d] and playerXY.x < winWidth*0.75:
                playerXY = playerXY.move(winWidth/4, 0)

            if event.key == K_SPACE and (playerXY.x < winWidth/4 or playerXY.x > winWidth*0.75):
                playerXY.y -= 2 * dt/2

    # my man deaccelerating
    if playerXY.x < winWidth/4 or playerXY.x > winWidth*0.75:
        playerXY.y += 1 * dt/2
    if playerXY.y >= winHeight*0.65:
        playerXY.y -= 1 * dt/4
    
    # BG
    screen.fill((135, 255, 135))

    pg.draw.ellipse(screen, (50, 200, 50), (winWidth/4-25, -winHeight, winWidth/2+50, winHeight*3))
    pg.draw.rect(screen, (75, 75, 75), (winWidth/4, 0, winWidth/2, winHeight))

    pg.draw.line(screen, (255, 255, 255), (winWidth/4+10, 0), (winWidth/4+10, winHeight), 10)
    pg.draw.line(screen, (255, 255, 255), (winWidth*0.75-12, 0), (winWidth*0.75-12, winHeight), 10)
    pg.draw.line(screen, (255, 213, 0), (winWidth/2-5, 0), (winWidth/2-5, winHeight), 10)

    # Car Drawing
    screen.blit(player, playerXY)
    screen.blit(car0, carXY0)
    screen.blit(car1, carXY1)
    screen.blit(garcar, garcarXY)
    screen.blit(santiago, santiagoXY)
    for i in range(0, 10):
        screen.blit(treeList[i], treeXYList[i])

    pg.display.flip()
    dt = clock.tick(60)