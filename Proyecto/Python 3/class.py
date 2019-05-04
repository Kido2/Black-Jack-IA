class Carta:
    palos=["Treboles","Diamantes","Corazones","Picas"]
    rangos=["-","As","2","3","4","5","6","7","8","9","10","J","Q","K"]
    def __init__(self,palo=0, rango=0):
        self.palo =palo
        self.rango =rango
    def __str__(self):
        return self.rangos[self.rango]+' de '+self.palos[self.palo]

a = []
a.append(Carta(1, 3))
print(a)
