# Direccion de memoria de la variable

class Personaje:
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    def __str__(self):
        return f'{self.nombre} vida: {self.vida} ataque: {self.ataque} defensa: {self.defensa}'



#Crear personajes y comparar su direccion de memoria
Goku = Personaje('Goku', 100, 20, 10)

Seikened = Goku
idGo = id(Goku)
idSe = id(Seikened)

print(idGo)
print(idSe)