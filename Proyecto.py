import random
import os

palos = {'D': 'Diamantes', 'E':'Espadas', 'T': 'Treboles', 'C': 'Corazones'}
nombre = {1: 'Az', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K'}


baraja = []
#crea todas la baraja
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

    def Valor(self):
        if self.nombre > 9:
            return 10
        elif self.nombre == 1:
            return 1 or 11
        else:
            return self.nombre


def sum_de_cartas(mano):
    sum_de_mano = 0
    for cada_carta in mano:
        sum_de_mano += cada_carta.Valor()
    return sum_de_mano

def imprimirmano(mano):
    for cada_carta in mano:
        print(cada_carta)

for palo in palos.keys():
    for nombre_carta in range(1, 14):
        baraja.append(Cartas(palo, nombre_carta))



game_over = False
dealer = []
jugador = []


while not game_over:

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

    turno_jugador = True


    #TODAVIA HAY PROBLEMAS

    while turno_jugador:
        os.system('cls')
        print('El dealer tiene :')
        imprimirmano(dealer)
        print('La suma de las cartas es ',sum_de_cartas(dealer))
        print()
        print('El jugador tiene: ')
        imprimirmano(jugador)
        print('La suma de las cartas es ', sum_de_cartas(jugador))


        if sum_de_cartas(jugador) > 21:
            print('El jugador ha perdido')
            os.system('cls')
            print('El dealer tiene :')
            imprimirmano(dealer)
            print('La suma de las cartas es ',sum_de_cartas(dealer))
            print()
            print('El jugador tiene: ')
            imprimirmano(jugador)
            print('La suma de las cartas es ', sum_de_cartas(jugador))
            ciclo = False
            turno_jugador = False
            game_over = True

        elif sum_de_cartas(jugador) == 21:
            print('El jugador ha ganado')
            ciclo = False
            turno_jugador = False
            game_over = True
            turno_dealer = False
        else:
            ciclo = True

        while ciclo:
            inputCiclo = input('Quiere pedir o plantarse:  ').lower()
            if inputCiclo == 'pedir' or 'plantarse' or 'plantar' or 'planto':
                ciclo = False

        if inputCiclo == 'pedir':
            jugador.append(baraja[-1])
            del baraja[-1]
            if sum_de_cartas(jugador) > 21:
                print('El jugador ha perdido ')
                turno_jugador = False
                turno_dealer = False
                game_over = True

        elif inputCiclo == 'plantarse' or 'plantar' or 'planto':
            turno_jugador = False
            turno_dealer = True

    while turno_dealer:
        os.system('cls')
        print('El dealer tiene :')
        imprimirmano(dealer)
        print('La suma de las cartas es ',sum_de_cartas(dealer))
        print()
        print('El jugador tiene: ')
        imprimirmano(jugador)
        print('La suma de las cartas es ', sum_de_cartas(jugador))

        if sum_de_cartas(dealer) == 21:
            print('El dealer ha ganado ')
            turno_dealer = False
            game_over = True
            turno_jugador = False

        if sum_de_cartas(dealer) > 21 and sum_de_cartas(jugador) < 21:
            print('El jugador ha ganado')
            turno_dealer = False
            game_over = True
            turno_jugador = False

        elif sum_de_cartas(dealer) >= sum_de_cartas(jugador) and sum_de_cartas(dealer) > 21:
            print('El dealer ha ganado ')
            turno_dealer = False
            game_over = True
            turno_jugador = False

        elif sum_de_cartas(dealer) == sum_de_cartas(jugador) and sum_de_cartas(dealer) < 21:
            print('El dealer ha ganado ')
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
            print('El jugador ha ganado')
            turno_dealer = False
            game_over = True
            turno_jugador = False

        elif sum_de_cartas(jugador) > sum_de_cartas(dealer) and sum_de_cartas(jugador) < 21:
            print('El jugador ha ganado')
            turno_dealer = False
            game_over = True
            turno_jugador = False

        elif sum_de_cartas(jugador) < sum_de_cartas(dealer) and sum_de_cartas(jugador) < 21:
            print('El dealer ha ganado ')
            turno_dealer = False
            game_over = True
            turno_jugador = False

print()
print('Juego terminado')
