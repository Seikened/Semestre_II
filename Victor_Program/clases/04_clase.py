import copy

class Vehiculo:
    def __init__(self, marca, lista, tipo_combustible):
        self.marca = marca
        self.lista = lista
        self.tipo_combustible = tipo_combustible

    def __str__(self):
        return f"Este es un {self.lista} de la marca {self.marca}, funciona con {self.tipo_combustible}."

# Crear una instancia de Vehiculo
mi_vehiculo = Vehiculo("Toyota", [1,2,3,1], "gasolina")

# Clonar el objeto mi_vehiculo
vehiculo_clonado = copy.copy(mi_vehiculo)
vehiculo_clonado.marca = "Nissan"

print(vehiculo_clonado)
print(mi_vehiculo)
