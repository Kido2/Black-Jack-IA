import pygame, sys
from pygame.locals import *
from random import randint
def board():
    pygame.init()
    ventana=pygame.display.set_mode((1290,650))
    pygame.display.set_caption("Real Game")
    board=pygame.image.load("board.png")
    stand= pygame.image.load("stand.jpg")
    hit=pygame.image.load("hit.jpg")
    posx, posy=0,0
    posx2,posy2=970,50
    posx3,posy3=970,450
    ventana.blit(board,(posx,posy))
    ventana.blit(stand,(posx2,posy2))
    ventana.blit(hit,(posx3,posy3))
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

board()
