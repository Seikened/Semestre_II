import math as mt



cuadrado_de_x = lambda x: (x**2) + (3*x) + (1)
cubo_mas_cos = lambda x: (x**3) + (mt.cos(x)) + (1)
euler = lambda x: (mt.exp(2*x)) + (2*x)



print("Bienvenido al menú interactivo para el cálculo de tres funciones.")
while(True): # Se crea ciclo infinito
    print(""" ¿Qué quieres hacer? Escribe una opción
              1) Evaluar en x^2+3x+1
              2) Evaluar en x^3+cos(x)+1
              3) Evaluar en e^2x + 2x
              4) Salir
            """)
    opcion = int(input())
    match opcion:
        case 1:
            x = float(input("Introduce el valor de x: "))
            #Aquí mandas llamar la función para el punto 1.
            valor = cuadrado_de_x(x)
            # Aquí usas el print con .format()
            print(f"Valor de x ({x}) evaluada en x^2+3x+1 = {valor}")
        case 2:
            x = float(input("Introduce el valor de x: "))
            #Aquí mandas llamar la función para el punto 2.
            valor = cubo_mas_cos(x)
            # Aquí usas el print con .format()
            print(f"Valor de x ({x}) evaluada en x^3+cos(x)+1 = {valor}")
        case 3:
            x = float(input("Introduce el valor de x: "))
            #Aquí mandas llamar la función para el punto 3.
            valor = euler(x)
            # Aquí usas el print con .format()
            print(f"Valor de x ({x}) evaluada en e^2x + 2x = {valor}")
        case 4:
            print("Hasta luego")
            break
        case _:
            print("No se reconoce el comando u opción")