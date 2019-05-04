import cartasclases

Miarchivo=open("cartas.txt", "w")
Baraja=cartasclases.Baraja()
Miarchivo.write(Baraja)
Miarchivo.close()
