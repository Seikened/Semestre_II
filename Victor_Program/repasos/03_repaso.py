import numpy as np
import random as rd



pesoPromedioDeUnHuevo = 60
desviacionEstandar = 4
cantidadDeHuevosEnElPaquete = 36
humbralDeDeteccion = 2100


def PesoDeUnHuevo():
    return rd.gauss(pesoPromedioDeUnHuevo, desviacionEstandar)

cajaDeHuevos = [PesoDeUnHuevo() for i in range(cantidadDeHuevosEnElPaquete)]

pesoTotalDelPaquete = sum(cajaDeHuevos)

# Realizar simulacion de 1000 paquetes

cantidadDePaquetes = 1000000
listaPesoToatalDePaquetes = []
for i in range(cantidadDePaquetes):
    cajaDeHuevos = [PesoDeUnHuevo() for i in range(cantidadDeHuevosEnElPaquete)]
    listaPesoToatalDePaquetes.append(sum(cajaDeHuevos))



menorPeso = min(listaPesoToatalDePaquetes)
mayorPeso = max(listaPesoToatalDePaquetes)
desviacionEstandar = np.std(listaPesoToatalDePaquetes)

print(f"El peso total del paquete es {pesoTotalDelPaquete} gramos")

print("Analisis de los paquetes---------------------------------")
print(f"El peso menor de los paquetes es {menorPeso} gramos")
print(f"El peso mayor de los paquetes es {mayorPeso} gramos")

print(f"La desviacion estandar de los paquetes es {desviacionEstandar} gramos")

contadorHuevosSospechosos = 0
for caja in listaPesoToatalDePaquetes:
    if caja > humbralDeDeteccion:
        contadorHuevosSospechosos += 1


print(f"La cantidad de paquetes con huevos sospechosos es {contadorHuevosSospechosos}")







class Remlque():
    def __init__(self,noRuedas, pesoMaximo):
        self.noRuedas = noRuedas
        self.pesoMaximo = pesoMaximo
        self.pesoActual = 0
        


class DobleRemolque(Remlque):
    def __init__(self, noRuedas, pesoMaximo):

        self.pesoRemolque2 = 0
        