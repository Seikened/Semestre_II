# Ejercicio No 2. Función que pida como parámetro un año, y que regrese una leyenda que diga si es Bisiesto o no lo es.

ComprobadorBisiesto = lambda year: (year % 4) == 0

preguntaUser = int(input("Dame el año que deseas comprobar: "))
if ComprobadorBisiesto(preguntaUser):
    print(f"El año {preguntaUser} si es bisiesto")
else:
    print(f"El año {preguntaUser} no es bisiesto")
