import numpy as np
import matplotlib.pyplot as plt

def puntoFijo(g, x0, tol, max_iter):
    historico = []
    x = x0  # Iniciar con el valor inicial x0

    for i in range(max_iter):
        x_nuevo = g(x)  # Calcular el nuevo punto usando g(x)
        historico.append(x_nuevo)

        if np.abs(x_nuevo - x) < tol:  # Verificar la condición de parada
            break

        x = x_nuevo  # Actualizar x para la próxima iteración

    historico = np.asarray(historico)
    return historico, i + 1  # i + 1 para contar la iteración inicial

if __name__ == '__main__':
    # La función g(x) definida según tu imagen
    f = lambda x: 1 + 2*x - 3*x**2*np.exp(-x) + 2*x**3*np.sin(x)*np.exp(-x/5)
    g_de_x = lambda x: x - np.arcsin((-1 - 2*x + 3*x**2 * np.exp(-x)) / (2*x**3 * np.exp(-x/5)))

    x0 = 9  # Punto de inicio
    epsilon = 0.00001
    max_iter = 100

    # Inicia el método de punto fijo
    R, i = puntoFijo(g_de_x, x0, epsilon, max_iter)
    
    # Imprimir los resultados
    print('Punto fijo: ', R[-1], 'en', i, 'iteraciones')
    print('g(R)= ', g_de_x(R[-1]))

    # Graficar la convergencia hacia el punto fijo
    plt.plot(np.arange(1, i+1), R, '-*', label='Puntos fijos')
    plt.xlabel('Iteración')
    plt.ylabel('Punto fijo')
    plt.grid()
    plt.legend()
    plt.show()
