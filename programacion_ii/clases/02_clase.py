# Operaciones de Fracciones
def sumaFracciones(a, b, c, d):
    numerador = (a * d) + (b * c)
    denominador = b * d
    return (numerador, denominador)


a = 1
b = 2
c = 1
d = 2
numerador, denominador = sumaFracciones(a, b, c, d)
print(f"\n La suma de {a}/{b} + {c}/{d} es {numerador}/{denominador} \n")


# Si quiero sumar 3 fracciones
a = 1
b = 2
c = 1
d = 2
e = 6
f = 3


numerador, denominador = sumaFracciones(a, b, c, d)
numerador, denominador = sumaFracciones(numerador, denominador, e, f)
print(f"\n La suma de {a}/{b} + {c}/{d} + {e}/{f} es {numerador}/{denominador} \n")