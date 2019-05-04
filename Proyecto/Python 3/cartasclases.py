class Carta:
    palos=["Treboles","Diamantes","Corazones","Picas"]
    rangos=["-","As","2","3","4","5","6","7","8","9","10","J","Q","K"]
    def __init__(self,palo=0, rango=0):
        self.palo =palo
        self.rango =rango
    def __str__(self):
        return self.rangos[self.rango]+" de "+self.palos[self.palo]
class Baraja:
    def __init__(self):
        self.cartas = []
        for palo in range(4):
            for rango in range(1,14):
                self.cartas.append(Carta(palo,rango))
    def __str__(self):
        s = ""
        for i in range(len(self.cartas)):
            s = s + str(self.cartas[i]) + "\n"
        return s

print(Baraja())
