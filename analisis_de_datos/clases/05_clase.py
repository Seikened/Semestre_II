# Pesos a Dólares

def pesos_a_dolares(pesos,tipo_cambio):
    dolares = pesos/tipo_cambio
    return round(dolares,2)

pesos = 30
tipo_cambio = 17.12
dolares = pesos_a_dolares(pesos,tipo_cambio)
print(dolares)


# Calcule el factorial de un número

def factorial(numero):
    fact = 1
    for i in range(1,numero+1):
        fact *= i
    return fact

num = 6
result = factorial(num)
print(result)


# area de un circulo
import math

pi = math.pi
areaCirculo = lambda pi,radio: pi*(radio**2) 

area = areaCirculo(pi,radio=3)
print(round(area,2))


# cantidad de números negativos
def NumNegativos(listaNum):
    negativos = 0
    for num  in listaNum:
        if num <0:
            negativos += 1
    return negativos

lista = [-1,-2,5,-7,6]
cantidadNegativos = NumNegativos(lista)
print(cantidadNegativos)


# Funcion que pida años bisiestos y entre dos fechas que uno ponga


def Years(fechaUno,fechaDos):
    if fechaUno > fechaDos:
        fechaUno,fechaDos = fechaDos,fechaUno
    cuantos = 1
    for year in range(fechaUno,fechaDos):
        if year % 4 == 0:
            cuantos += 1
    return cuantos
bisiesto = Years(1990,2025)
print(f"Años:{bisiesto}")


# Función que pida un número y que regrese su equivalencia en Binario


def DecimalBinario(numB):
    cociente = numB
    listaResiduo = []
    residuo = 1
    while cociente !=0:
        residuo = cociente % 2
        cociente = cociente//2
        listaResiduo.append(residuo)
    listaInversa = listaResiduo[::-1]
    return listaInversa

numero = 353
binario = DecimalBinario(numero)
print(binario)

def BinarioDecimal(binario):
    
    potencia = len(binario)-1
    numero = 0
    
    
    for numBinario in binario:
        numero += numBinario*(2**potencia)
        potencia-= 1
        
    return numero

numeroDelDecimal = BinarioDecimal(binario)
print(numeroDelDecimal)