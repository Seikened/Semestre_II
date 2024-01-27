# Completa el ejercicio aquí
import math
import numpy as np


sin = math.sin()

#Define la función aquí
def Calcular_funcion(f,x): #Agregar los parámetros de entrada
    
    return f(x)

def f(x):
    """
    Esta función calcula:
    Parametros de entrada:
    x: valor del dominio
    Parametros de salida:
    x+2: el valor de la función lineal x+ 2
    """
    return x + 2

def f(x):
    return (sin(x)+(2*x))

if __name__ == "__main__":
    
    x = list(range(-100,101))
    valor = Calcular_funcion(f,x)
    print(valor)
    #Crear una lista de números para el dominio de la función (valores de X) con valores de -100 a 100

    # Crear una lista de números donde se usa la función usada en el inciso anterior. Los valores de x a ingresar son los creados en el inciso b)
    
    # Crea la gráfica aquí