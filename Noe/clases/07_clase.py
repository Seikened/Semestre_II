import numpy as np
import matplotlib.pyplot as plt
import math


def biseccion(f, a, b, tol, max_iter): 
    # aproxima una raiz R, de f en el intervalo (a,b)
    
    # combrobar si existe una raiz entre a y b, si no, regresa un error y termina el programa
    # si sign(f(a)) = sign(f(b)): error
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("Los escalares a y b, no contienen una raiz")
        
    # iniciamos las iteraciones
    i = 0
    historico = []
    while i<max_iter:
        # obtener el punto medio
        # m = (a+b)/2
        m = (a + b)/2
        R = m
        historico.append(R)
    
        # verificamos si se cumple el criterio de paro
        # terminamos el ciclo
        if np.abs(f(m)) < tol:
            i = i+1
            break
        elif np.sign(f(a)) == np.sign(f(m)): # caso donde m es una mejora de a
            a = m
        else: #elif np.sign(f(b)) == np.sign(f(m)): # caso donde m es una mejora de b
            b = m

        # incrementamos las iteraciones
        i +=1
        
    historico = np.asarray(historico)
    return historico, i





if __name__ == '__main__':
    
    f = lambda x: 1 + 2*x - 3*x**2*np.exp(-x) + 2*x**3*np.sin(x)*np.exp(-x/5)
    a = 9.5027
    b = 9.5028
    epsilon = 0.00001
    max_iter = math.ceil(math.log2(np.abs(b-a)/epsilon) - 1)
    print('Max iter: ', max_iter)
    
    R, i = biseccion(f, a, b, epsilon, max_iter)
    print('Raiz: ', R[-1], 'en ', i, 'iteraciones')
    print('f(R)= ', f(R[-1]))
    
    x = np.linspace(a,b,100)
    
    y = f(x)
    
    # for i in range(len(x)):
    #     y.append(f(x[i]))
    
    
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