import random, pygame, os, time

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

def imprimirmano(mano):
    for cada_carta in mano:
        print(cada_carta)

for palo in palos.keys():
    for nombre_carta in range(1, 14):
        baraja.append(Cartas(palo, nombre_carta).__str__())


def mostrarcartas(mano, x, y):
    for cartas in mano:
        foto = pygame.image.load(cartas+'.PNG')
        gameDisplay.blit(foto, (x, y))
        x += 55

def text_objects(text, font):
    TextSurface = font.render(text, True, black)
    return TextSurface, TextSurface.get_rect()


def mensaje_en_pantalla(text):
    largeText = pygame.font.Font('freesansbold.ttf', 50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)




game_over = False
dealer = []
jugador = []

pygame.init()
display_width = 800
display_height = 600
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 120, 0)


gameDisplay = pygame.display.set_mode((display_width, display_height))

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    random.shuffle(baraja)
    random.shuffle(baraja)
    random.shuffle(baraja)
    random.shuffle(baraja)

    jugador.append(baraja[-1])
    del baraja[-1]
    jugador.append(baraja[-1])
    del baraja[-1]
    dealer.append(baraja[-1])
    del baraja[-1]
    gameDisplay.fill(green)
    mostrarcartas(dealer, 500, 150)
    mostrarcartas(jugador, 100, 500)
    pygame.display.update()
    turno_jugador = True


    #TODAVIA HAY PROBLEMAS


    while turno_jugador:

        if sum_de_cartas(jugador) > 21:
            pygame.display.update()
            mostrarcartas(jugador, 100, 500)
            mensaje_en_pantalla('Has perdido')
            pygame.display.update()
            time.sleep(2)
            ciclo = False
            turno_jugador = False
            game_over = True

        elif sum_de_cartas(jugador) == 21:
            pygame.display.update()
            mostrarcartas(jugador, 100, 500)
            mensaje_en_pantalla('Has ganado')
            pygame.display.update()
            ciclo = False
            turno_jugador = False
            game_over = True
            turno_dealer = False
        elif sum_de_cartas(jugador) < 21:
            ciclo = True


        while ciclo:
            inputCiclo = input('Quiere pedir o plantarse:  ').lower()
            if inputCiclo == 'pedir' or 'plantarse' or 'plantar' or 'planto':
                ciclo = False

        if inputCiclo == 'pedir':
            jugador.append(baraja[-1])
            del baraja[-1]
            pygame.display.update()
            mostrarcartas(jugador, 100, 500)
            pygame.display.update()
            turno_jugador = True
            turno_dealer = False
            game_over = False



        elif inputCiclo == 'plantarse' or 'plantar' or 'planto':
            turno_jugador = False
            turno_dealer = True

    while turno_dealer:
        pygame.display.update()
        mostrarcartas(dealer, 500, 150)
        pygame.display.update()

        if sum_de_cartas(dealer) == 21:
            pygame.display.update()
            mostrarcartas(dealer, 500, 150)
            mensaje_en_pantalla('El dealer ha  ganado')
            pygame.display.update()
            turno_dealer = False
            game_over = True
            turno_jugador = False

        if sum_de_cartas(dealer) > 21 and sum_de_cartas(jugador) < 21:
            pygame.display.update()
            mostrarcartas(dealer, 500, 150)
            mostrarcartas(jugador, 100, 500)
            mensaje_en_pantalla('El dealer ha perdido')
            pygame.display.update()
            turno_dealer = False
            game_over = True
            turno_jugador = False

        elif sum_de_cartas(dealer) >= sum_de_cartas(jugador) and sum_de_cartas(dealer) > 21:
            mostrarcartas(dealer, 500, 150)
            mensaje_en_pantalla('El dealer ha ganado')
            pygame.display.update()
            turno_dealer = False
            game_over = True
            turno_jugador = False

        elif sum_de_cartas(dealer) == sum_de_cartas(jugador) and sum_de_cartas(dealer) < 21:
            mostrarcartas(dealer, 500, 150)
            mensaje_en_pantalla('El dealer ha ganado')
            pygame.display.update()
            turno_dealer = False
            game_over = True
            turno_jugador = False


        elif sum_de_cartas(dealer) <= 17:
            dealer.append(baraja[-1])
            del baraja[-1]
            turno_dealer = True
            turno_jugador = False
            game_over = True

        elif sum_de_cartas(jugador) < 21 and sum_de_cartas(dealer) > 21:
            mostrarcartas(jugador, 100, 500)
            mensaje_en_pantalla('Has ganado')
            pygame.display.update()
            turno_dealer = False
            game_over = True
            turno_jugador = False

        elif sum_de_cartas(jugador) > sum_de_cartas(dealer) and sum_de_cartas(jugador) < 21 and sum_de_cartas(dealer) < 21:
            mostrarcartas(jugador, 100, 500)
            mensaje_en_pantalla('Has ganado')
            pygame.display.update()
            turno_dealer = False
            game_over = True
            turno_jugador = False

        elif sum_de_cartas(jugador) < sum_de_cartas(dealer) and sum_de_cartas(jugador) < 21 and sum_de_cartas(dealer) < 21:
            mostrarcartas(jugador, 100, 500)
            mensaje_en_pantalla('Has Perdido')
            pygame.display.update()
            turno_dealer = False
            game_over = True
            turno_jugador = False

pygame.quit()
quit()
