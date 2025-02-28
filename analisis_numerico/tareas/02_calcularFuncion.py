
import numpy as np
import matplotlib.pyplot as plt


def Calcular_funcion(f, x):
    """
    Calcula el valor de una función matemática en un punto dado.
    
    Parámetros:
    f -- función matemática a evaluar
    x -- valor numérico en el que se evaluará la función
    
    Retorna:
    Valor de la función f evaluada en el punto x.
    """
    return f(x)


def f(x):
    """
    Calcula la función matemática y = sin(x) + 2x.
    
    Parámetros:
    x -- valor numérico para calcular la función
    
    Retorna:
    Resultado de la función y = sin(x) + 2x.
    """
    return np.sin(x) + 2 * x

if __name__ == "__main__":

    dominio_x = list(range(-100, 101))
    
    valores_y = []
    for xi in dominio_x:
        yi = Calcular_funcion(f, xi)
        valores_y.append(yi)
    
    
    
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    plt.plot(dominio_x, valores_y, label='y = sin(x) + 2x')
    plt.title('Gráfica de la función y = sin(x) + 2x')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()
