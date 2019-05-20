import random, pygame, time, sys
from pygame.locals import *
from random import randint

palos = {'D': 'Diamantes', 'P':'Picas', 'T': 'Treboles', 'C': 'Corazones'}
nombre = {1: 'Az', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K'}


baraja = []

class Cartas:
    def __init__(self, palo=0, nombre=0):
        self.palo = palo
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def getPalo(self):
        return self.palo

    def __str__(self):
        return nombre[self.getNombre()] +' de '+ palos[self.getPalo()]


def sum_de_cartas(mano):
    suma = 0
    for carta in mano:
        if carta[0].isdigit() and carta[1].isdigit():
            suma += 10

        elif carta[0].isdigit():
            suma += int(carta[0])

        elif carta[0] in 'JQK':
            suma += 10

        elif carta[0] == 'A':
            if suma >= 11:
                suma += 1
            else:
                suma += 11
    return suma

#imprime una mano
def imprimirmano(mano):
    for cada_carta in mano:
        print(cada_carta)

#crea la baraja con todas las cartas

for palo in palos.keys():
    for nombre_carta in range(1, 14):
        baraja.append(Cartas(palo, nombre_carta).__str__())

#muestra las cartas de una mano

def mostrarcartas(mano, x, y):
    for cartas in mano:
        foto = pygame.image.load('Cartas/'+cartas+'.PNG')
        foto = pygame.transform.scale(foto,(90, 150))
        gameDisplay.blit(foto, (x, y))
        x += 70

def text_objects(text, font, colour):
    TextSurface = font.render(text, True, colour)
    return TextSurface, TextSurface.get_rect()

#crea mensaje en pantalla

def mensaje_en_pantalla(text, x, y):
    largeText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = text_objects(text, largeText, white)
    TextRect.center = ((x), (y))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def mensaje_en_pantalla_2(text, x, y):
    largeText = pygame.font.Font('freesansbold.ttf', 40)
    TextSurf, TextRect = text_objects(text, largeText, Cream)
    TextRect.center = ((x), (y))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()


#Crea la tabla para jugar

def board():
    pygame.init()
    ventana=pygame.display.set_mode((1290,650))
    pygame.display.set_caption("Real Blackjack")
    board=pygame.image.load("Cartas/board.PNG")
    board=pygame.transform.scale(board,(1290,650))
    ventana.blit(board,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

#Juega toda la baraja

def seguir():
    seguir_ciclo = True
    mensaje_en_pantalla('Presione r para jugar otra ronda', display_width/4, display_height/4)
    while seguir_ciclo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_r:
                    if len(jugador) > 0:
                        for valor in range(0, len(jugador)):
                            del jugador[0]
                        for valor1 in range(0, len(dealer)):
                            del dealer[0]
                    turno_jugador = True
                    game_over = False
                    seguir_ciclo = False

            else:
                seguir_ciclo = True

#crea pantalla del fin del juego

def gameOver():
    pygame.init()
    ventana = pygame.display.set_mode((1290, 650))
    gameover = pygame.image.load("Cartas/gameover.jpg")
    gameover = pygame.transform.scale(gameover,(1290,650))
    ventana.blit(gameover,(0,0))
    pygame.display.update()
    ciclo1 = True
    while ciclo1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()



pygame.init()



dealer = []
jugador = []


white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 120, 0)
Negro=(0,0,0)
Azul=(0,0,128)
Cream=(255,255,204)
Verde=(0,128,0)

display_width = 1000
display_height = 650
gameDisplay = pygame.display.set_mode((display_width, display_height))


#Se crea el menu del juego con el boton para jugar
banner=pygame.image.load("Cartas/pixel-blackjack_big.png")
banner = pygame.transform.scale(banner,(1000,650))
playbutton=pygame.image.load("Cartas/boton2.gif")
playRect=playbutton.get_rect()
playRect.topleft=(700,400)
gameDisplay.fill(Azul)
gameDisplay.blit(banner, (0,0))
gameDisplay.blit(playbutton,(750,400))
mensaje_en_pantalla_2("Click here!",650,500)
pygame.display.update()
ciclo_inicio = True

while ciclo_inicio:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            if playRect.collidepoint(event.pos):
                game_over = False
                ciclo_inicio = False
            else:
                game_over = True


while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    board()

#Se baraja el mazo de cartas
    random.shuffle(baraja)
    random.shuffle(baraja)
    random.shuffle(baraja)
    random.shuffle(baraja)
#Se reparten las cartas iniciales al jugador y al dealer
    jugador.append(baraja[-1])
    del baraja[-1]
    jugador.append(baraja[-1])
    del baraja[-1]
    dealer.append(baraja[-1])
    del baraja[-1]
#Se muestran las cartas iniciales del dealer y del jugador
    pygame.display.update()
    mostrarcartas(dealer, 600, 117)
    mostrarcartas(jugador, 100, 500)
#Se muestran los mensajes de pedir y plantarse
    mensaje_en_pantalla("Presione 'h' para pedir carta", 150, 100)
    mensaje_en_pantalla("Presione 'p' para plantarse", 150, 70)

    pygame.display.update()
    turno_jugador = True

    while turno_jugador:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        if sum_de_cartas(jugador) > 21:
            mostrarcartas(jugador, 100, 500)
            mensaje_en_pantalla_2('El dealer ha ganado', display_width/2+100, display_height/2-250)
            pygame.display.update()
            ciclo = False
            turno_jugador = False
            turno_dealer = False



        elif sum_de_cartas(jugador) == 21:
            mostrarcartas(jugador, 100, 500)
            mensaje_en_pantalla_2('Has ganado', display_width/2+100, display_height/2-250)
            pygame.display.update()
            ciclo = False
            turno_jugador = False
            turno_dealer = False


        elif sum_de_cartas(jugador) < 21:
            ciclo =True


        while ciclo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_h:
                        jugador.append(baraja[-1])
                        del baraja[-1]
                        mostrarcartas(jugador, 100, 500)
                        pygame.display.update()
                        turno_jugador = True
                        turno_dealer = False
                        ciclo = False

                if event.type == pygame.KEYDOWN:
                    if event.key == K_p:
                        turno_jugador = False
                        turno_dealer = True
                        ciclo = False


    while turno_dealer:

        mostrarcartas(dealer, 600, 117)
        pygame.display.update()

        if sum_de_cartas(dealer) == 21:
            mostrarcartas(dealer, 600, 117)
            mensaje_en_pantalla_2('El dealer ha  ganado', display_width/2+100, display_height/2-250)
            pygame.display.update()
            turno_dealer = False
            turno_jugador = False
            pygame.time.wait(1000)

        if sum_de_cartas(dealer) > 21 and sum_de_cartas(jugador) < 21:
            mostrarcartas(dealer, 600, 117)
            mostrarcartas(jugador, 100, 500)
            mensaje_en_pantalla_2('El dealer ha perdido', display_width/2+100, display_height/2-250)
            pygame.display.update()
            turno_dealer = False
            turno_jugador = False



        elif sum_de_cartas(dealer) >= sum_de_cartas(jugador) and sum_de_cartas(dealer) > 21:
            mostrarcartas(dealer, 600, 117)
            mensaje_en_pantalla_2('El dealer ha ganado', display_width/2+100, display_height/2-250)
            pygame.display.update()
            turno_dealer = False
            turno_jugador = False


        elif sum_de_cartas(dealer) == sum_de_cartas(jugador) and sum_de_cartas(dealer) < 21:
            mostrarcartas(dealer, 600, 117)
            mensaje_en_pantalla_2('El dealer ha ganado', display_width/2+100, display_height/2-250)
            pygame.display.update()
            turno_dealer = False
            turno_jugador = False



        elif sum_de_cartas(dealer) < 17:
            dealer.append(baraja[-1])
            del baraja[-1]
            turno_dealer = True
            turno_jugador = False
            pygame.time.wait(1000)

        elif sum_de_cartas(jugador) < 21 and sum_de_cartas(dealer) > 21:
            mostrarcartas(jugador, 100, 500)
            mensaje_en_pantalla_2('Has ganado', display_width/2+100, display_height/2-250)
            pygame.display.update()
            turno_dealer = False
            turno_jugador = False


        elif sum_de_cartas(jugador) > sum_de_cartas(dealer) and sum_de_cartas(jugador) < 21 and sum_de_cartas(dealer) < 21:
            mostrarcartas(jugador, 100, 500)
            mensaje_en_pantalla_2('Has ganado', display_width/2+100, display_height/2-250)
            pygame.display.update()
            turno_dealer = False
            turno_jugador = False


        elif sum_de_cartas(jugador) < sum_de_cartas(dealer) and sum_de_cartas(jugador) < 21 and sum_de_cartas(dealer) < 21:
            mostrarcartas(jugador, 100, 500)
            mensaje_en_pantalla_2('El dealer ha ganado', display_width/2+100, display_height/2-250)
            pygame.display.update()
            turno_dealer = False
            turno_jugador = False

#Si hay mas de 7 cartas en la baraja se puede seguir
    if len(baraja) > 7:
        seguir()
        pygame.time.wait(1000)
#Si hay menos de 7 cartas en la baraja se acaba el juego
    else:
        pygame.time.wait(2000)
        gameOver()
        game_over = True
