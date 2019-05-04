def dayName(n):
    if n==1:
        n="lunes"
    elif n==2:
        n="Martes"
    elif n==3:
        n="Miercoles"
    elif n==4:
        n="Jueves"
    elif n==5:
        n="Viernes"
    elif n==6:
        n="Sabado"
    elif n==7:
        n="Domingo"
    elif n>7 or n<1:
        n=None
    return n
n=int(input("Ingrese un numero perteneciente a un dia de la semana:"))

# NOTE: --------------------------------------------------------------
import sys
def test(pasa):
    lnum = sys._getframe(1).f_lineno
    if pasa:
        msg = "Prueba en la línea {0} ok.".format(lnum)
    else:
        msg = "Prueba en la línea {0} FALLÓ.".format(lnum)
    print(msg)
def testSuite():
    test ( dayName (1) == "lunes")
    test (dayName (5) == "Viernes")
    test (dayName (42) == None)

testSuite()
