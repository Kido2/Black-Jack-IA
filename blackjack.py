import pygame ,sys, random
from pygame.locals import*


Negro=(0,0,0)
Azul=(0,0,128)
Cream=(255,255,204)
Verde=(0,128,0)


def crearMazo(baraja):
    Miarchivo=(baraja,"r")
    cartas=[In.strip() for In in Miarchivo]
    random.shuffle(cartas)
    return cartas
def RepartirCartas(cartas):
    jugador=[]
    repartidor=[]
    while len(repartidor)<2:
        jugador.append(cartas[0])
        cartas.pop(0)
        repartidor.append(cartas[0])
        cartas.pop(0)
    return jugador, repartidor
def Suma(Mano):
    Suma1=0
    Suma2=0
    for carta in Mano:
        if carta[-1].isdigit() and int(carta[-1])!=10:
            Suma1+=int(carta[-1])
            Suma2+=int(carta[-1])
        if carta[-1] in "JQK" or card[-2:].isdigit():
            Suma1+=11
            Suma2+=1
    if Suma2==2:
        Suma1=12
    return Suma1, Suma2
def RepartirCarta(mano,cartas):
    mano.append(cartas[0])
    cartas.pop(0)
def gameOver():
    pygame.init()
    displaysuper=pygame.display.set_mode((1000,600))
    displaysuper.fill(Negro)
    drawText("¡Game Over!",pygame.font.SysFont(None,70), displaysuper,350,200)
    drawText("!Please try again¡", pygame.font.SysFont(None,100), displaysuper,125,280)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if evemt.type==QUIT:
                pygame.quit()
                sys.exit()
def obtApuestas(dinero,cartas):
    pygame.init()
    displaysuper=pygame.display.set_mode((1000,600))
    pygame.display.set_caption("Let`s play")
    displaysuper.fill(Verde)
    Fondos=False
    if dinero<5:
        gameOver()
    Apuestasco=False
    fuente=pygame.font.SysFont(None,30)
    drawText("Wallet: "+str(dinero), fuente, displaysuper,10,10)
    bet5Pos=(-10,250)
    bet5=pygame.image.load("$5.png")
    bet5Rect=bet5.get_rect()
    bet5Rect.topleft=(bet5Pos)
    bet10Pos=(250,220)
    bet10=pygame.image.load("$10.png")
    bet10Rect=bet10.get_rect()
    bet10Rect.topleft=(bet10Pos)
    bet25Pos=(520,225)
    bet25=pygame.image.load("$25.png")
    bet25Rect=bet25.get_rect()
    bet25Rect.topleft=(bet25Pos)
    bet=0
    fuente1=pygame.font.SysFont(None,100)
    drawText("Place your bet: ",fuente1, displaysuper,250,150)
    displaysuper.blit(bet5,bet5Rect)
    displaysuper.blit(bet10,bet10Rect)
    displaysuper.blit(bet25,bet25Rect)
    pygame.display.update()
    while Apuestasco is False:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==MOUSEBUTTONDOWN:
                if event.button==1:
                    if bet5Rect.collidepoint(event.pos):
                        if dinero>=5:
                            bet=5
                            Apuestasco=True
                    if bet10Rect.collidepoint(event.pos):
                        if dinero>=10:
                            bet=10
                            Apuestasco=True
                    if bet25Rect.collidepoint(event.pos):
                        if dinero>=25:
                            bet=25
                            Apuestasco=True
    while Apuestasco is True:
        if len(cartas)<25:
            cartas=crearMazo("cartas.txt")
        jugadorMano, repartidorMano=RepartirCartas(cartas)
        award=playHand(bet,dinero,jugadorMano,repartidorMano,cartas)
        dinero+=award
        pygame.display.update()
        obtApuestas(dinero,cartas)
"""def playHand(bet,dinero,jugadorMano,repartidorMano,cartas):
    pygame.init()
    displaysuper=pygame.display.set_mode((1000,600))
    pygame.display.set_caption("BLACKJACK")
    displaysuper.fill(Verde)
    fuente=pygame.font.SysFont(None,30)
    drawText("Bet placed: "+ str(bet),fuente,displaysuper,10,10)
    drawText("Press H to hit", fuente,displaysuper,10,50)
    drawText("Press S to stand", fuente, displaysuper,10,70)
    drawText("Wallet: $"+str(dinero),fuente,displaysuper,10,30)
    drawText("Player",fuente, displaysuper, 50,310)
    drawText("Dealer", fuente, displaysuper,310,10)
    pcardx,pcardy=(50,340)
    for card in jugadorMano:
        pic=
"""

def drawText(texto, fuente,superficie, x,y ):
    textobj=fuente.render(texto,1,Cream)
    textrect=textobj.get_rect()
    textrect.topleft=(x,y)
    superficie.blit(textobj,textrect)
def jugar():
    pygame.init()
    gamex,gamey=(1000,600)
    displaysuper=pygame.display.set_mode((gamex,gamey))
    pygame.display.set_caption("Blackjack")
    banner=pygame.image.load("pixel-blackjack_big.png")
    playbutton=pygame.image.load("boton2.gif")
    playRect=playbutton.get_rect()
    playRect.topleft=(700,400)
    font=pygame.font.SysFont(None, 30)
    displaysuper.fill(Azul)
    displaysuper.blit(banner, (0,50))
    displaysuper.blit(playbutton,(750,400))
    drawText("¡Click here!",font,displaysuper,650,500)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==MOUSEBUTTONDOWN:
                if event.button==1:
                    if playRect.collidepoint(event.pos):
                        cartas=crearMazo("cartas.txt")
                        obtApuestas(100,cartas)


jugar()



#Fases
#Cartas del Repartidor
#Cartas del jugador
#Repartir y barajar las cartas
