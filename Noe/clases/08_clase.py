import numpy as np
import matplotlib.pyplot as plt
import math

def falsaPosicion(f, a, b, tol, max_iter):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("Los escalares a y b no contienen una raíz entre ellos.")

    historico = []
    i = 0
    c = a  # Inicializar c para que tenga un valor antes del bucle

    while i < max_iter:
        c_old = c  # Guardar el valor anterior de c para comparar después
        c = a - ((f(a) * (b - a)) / (f(b) - f(a)))  # Calcular la nueva aproximación de c
        historico.append(c)

        if np.abs(f(c)) < tol:  # Si f(c) es menor que la tolerancia, hemos encontrado una raíz suficientemente buena
            break

        if np.sign(f(a)) == np.sign(f(c)):
            a = c
        else:
            b = c

        if np.abs(c - c_old) < tol:  # También podemos verificar si la diferencia entre las aproximaciones sucesivas es pequeña
            break

        i += 1

    historico = np.asarray(historico)
    return historico, i + 1  # i + 1 porque la cuenta comienza en 0

if __name__ == '__main__':
    # 1+2x-3x^2e^(-x)+2x^3sen(x)e^(-x/5)
    f = lambda x: 1 + 2*x - 3*x**2*np.exp(-x) + 2*x**3*np.sin(x)*np.exp(-x/5)

    a = 9
    b = 10
    epsilon = 0.00001
    max_iter = 100

    R, i = falsaPosicion(f, a, b, epsilon, max_iter)
    
    
    print('Raíz: ', R[-1], 'en', i, 'iteraciones')
    print('f(R)= ', f(R[-1]))


    x = np.linspace(a, b, 100)
    y = f(x)

    plt.plot(np.arange(1, i+1), R, '-*', label='Raices')
    plt.xlabel('Iteración')
    plt.ylabel('Raiz')
    plt.grid()
    plt.legend()
    plt.show()
    
    
    x = np.arange(a, b+1, 0.01)
    roots = f(R)
    plt.plot(x, f(x), label='f(x)')
    plt.plot(R, roots, '-*', label='Raices')
    plt.plot(R[-1], roots[-1], 'o', label='Raiz')
    plt.grid()
    plt.legend()
    plt.show()
