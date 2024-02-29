import math as mt
import numpy as np
import matplotlib.pyplot as plt


pi = mt.pi # Declaramos el valor de PI

def f(x):
    """funcion de coseno

    Args:
        x (float): punto de evaluación

    Returns:
        float: coseno evaluado en x
    """
    return mt.cos(x) 

def taylor(x,x0,grado):
    """Serie de Taylor

    Args:
        x (lista): intervalo
        x0 (float): donde se centra la función
        grado (int): iteraciones de Taylor

    Returns:
        lista: valores obtenidos de Taylor
    """
    y = f(x0)
    
    for n in range(1,grado):
        y += (-1)**n * (x-x0)**(2*n) / mt.factorial(2*n)
    return y

def error_relativo(x_values, taylor_values, cos_values):
    """Calcula el error relativo de una serie de Taylor

    Args:
        x_values (lista): intervalo 
        taylor_values (lista): valores obtenidos de Taylor
        cos_values (lista): valores obtenidos de la f(x) = cos x

    Returns:
        list: lista de los errores calculados
    """
    errors = []
    for tv, ev in zip(taylor_values, cos_values):
        if ev != 0:
            error = abs(tv - ev) / abs(ev)
        else:
            error = float('inf') # Infinito si el valor exacto es 0 para evitar división por 0
        errors.append(error)
    return errors