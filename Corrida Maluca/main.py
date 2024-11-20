import pygame
from random import randint

pygame.init()
screen=(1505,555)
clock=pygame.time.Clock()
display=pygame.display.set_mode(screen)
icon=pygame.image.load("Recursos/icon.ico")
background=pygame.image.load("Recursos/raceway.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Corrida Maluca")
white=(255,255,255)
black=(0,0,0)

red=pygame.image.load("Recursos/snail.png")
blue=pygame.image.load("Recursos/turtle.png")
yellow=pygame.image.load("Recursos/mouse.png")
redX=0
blueX=0
yellowX=0
redY=10
blueY=100
yellowY=190
winner=0

victory=pygame.mixer.Sound("Recursos/victory.mp3")
victory.set_volume(1)
pygame.mixer.music.load("Recursos/soundtrack.mp3")
pygame.mixer.music.play(-1)
midway=False
midwayRed=False
midwayBlue=False
midwayYellow=False
end=False
victorySound=False
running=True

while running==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            running=False
    if running==False:
        break

    display.blit(background,(0,0))
    display.blit(red,(redX,redY))
    display.blit(blue,(blueX,blueY))
    display.blit(yellow,(yellowX,yellowY))

    if end==False:
        if midwayRed==False:
            redX=redX+randint(1,10)
        else:
            redX=redX-randint(1,10)
        if midwayBlue==False:
            blueX=blueX+randint(1,10)
        else:
            blueX=blueX-randint(1,10)
        if midwayYellow==False:
            yellowX=yellowX+randint(1,10)
        else:
            yellowX=yellowX-randint(1,10)

    if redX>1505:
        redX=1505
        redY=290
        midwayRed=True
    if blueX>1505:
        blueX=1505
        blueY=380
        midwayBlue=True
    if yellowX>1505:
        yellowX=1505
        yellowY=470
        midwayYellow=True

    if midwayRed==True or midwayBlue==True or midwayYellow==True:
        midway=True
    if midwayRed==True:
        red=pygame.image.load("Recursos/snailFlip.png")
    if midwayBlue==True:
        blue=pygame.image.load("Recursos/turtleFlip.png")
    if midwayYellow==True:
        yellow=pygame.image.load("Recursos/mouseFlip.png")

    font=pygame.font.Font("freesansbold.ttf",20)
    fontEnd=pygame.font.Font("freesansbold.ttf",60)
    text=font.render("Aguarde...", True, black)
    textEnd=fontEnd.render("Ganhador!", True, white)
    redText1=font.render("Vermelho em Primeiro!", True, black)
    redText2=font.render("Vermelho em Segundo!", True, black)
    blueText1=font.render("Azul em Primeiro!", True, black)
    blueText2=font.render("Azul em Segundo!", True, black)
    yellowText1=font.render("Amarelo em Primeiro!", True, black)
    yellowText2=font.render("Amarelo em Segundo!", True, black)

    if midway==True and midwayRed==False or midway==True and midwayBlue==False or midway==True and midwayYellow==False:
        display.blit(text,(410,269))
    else:
        if midway==False:
            if redX>=blueX and redX>=yellowX:
                display.blit(redText1,(410,269))
            elif blueX>=redX and blueX>=yellowX:
                display.blit(blueText1,(410,269))
            else:
                display.blit(yellowText1,(410,269))
        else:
            if redX<=blueX and redX<=yellowX:
                display.blit(redText1,(410,269))
            elif blueX<=redX and blueX<=yellowX:
                display.blit(blueText1,(410,269))
            else:
                display.blit(yellowText1,(410,269))
    
    if midway==True and midwayRed==False or midway==True and midwayBlue==False or midway==True and midwayYellow==False:
        display.blit(text,(910,269))
    else:
        if midway==False:
            if redX>=blueX and redX<=yellowX or redX<=blueX and redX>=yellowX:
                display.blit(redText2,(910,269))
            elif blueX>=redX and blueX<=yellowX or blueX<=redX and blueX>=yellowX:
                display.blit(blueText2,(910,269))
            else:
                display.blit(yellowText2,(910,269))
        else:
            if redX>=blueX and redX<=yellowX or redX<=blueX and redX>=yellowX:
                display.blit(redText2,(910,269))
            elif blueX>=redX and blueX<=yellowX or blueX<=redX and blueX>=yellowX:
                display.blit(blueText2,(910,269))
            else:
                display.blit(yellowText2,(910,269))

    if redX<=0:
        end=True
    if blueX<=0:
        end=True
        winner=1
    if yellowX<=0:
        end=True
        winner=2

    if end==True:
        pygame.mixer.music.stop()
        background=pygame.image.load("Recursos/blackground.png")
        display.blit(textEnd,(400,250))
        if winner==0:
            display.blit(red,(800,250))
        elif winner==1:
            display.blit(blue,(800,250))
        else:
            display.blit(yellow,(800,250))
        if victorySound==False:
            pygame.mixer.Sound.play(victory)
            victorySound=True
    pygame.display.update()
    clock.tick(24)