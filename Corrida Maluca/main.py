import pygame
from random import randint

pygame.init()
screen=(1505,555)
clock=pygame.time.Clock()
display=pygame.display.set_mode(screen)
background=pygame.image.load("Recursos/raceway.png")
pygame.display.set_caption("Corrida Maluca")
white=(255,255,255)

red=pygame.image.load("Recursos/snail.png")
blue=pygame.image.load("Recursos/turtle.png")
yellow=pygame.image.load("Recursos/mouse.png")
redX=0
blueX=0
yellowX=0
redY=10
blueY=100
yellowY=190

victory=pygame.mixer.Sound("Recursos/victory.mp3")
victory.set_volume(1)
pygame.mixer.music.load("Recursos/soundtrack.mp3")
pygame.mixer.music.play(-1)
midway=False

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit()

    display.fill(white)
    display.blit(background,(0,0))
    display.blit(red,(redX,redY))
    display.blit(blue,(blueX,blueY))
    display.blit(yellow,(yellowX,yellowY))

    if redX>1505:
        redX=1505
        redY=290
        midway=True
    if blueX>1505:
        blueX=1505
        blueY=380
        midway=True
    if yellowX>1505:
        yellowX=1505
        yellowY=470
        midway=True

    if midway==False:
        redX=redX+randint(1,10)
    elif midway==True:
        redX=redX-randint(1,10)
    if midway==False:
        blueX=blueX+randint(1,10)
    elif midway==True:
        blueX=blueX-randint(1,10)
    if midway==False:
        yellowX=yellowX+randint(1,10)
    elif midway==True:
        yellowX=yellowX-randint(1,10)
    pygame.display.update()
    clock.tick(24)
pygame.quit()