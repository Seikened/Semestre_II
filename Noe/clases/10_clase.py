
import numpy as np


def Newton(x0,f,df, tol,maxIter=100):
    k = 0
    while k < maxIter:
        # Evaluar si xk es la solición
        if  abs(f(x0)) <= tol:
            # xk es la raiz y el programa termina
            return x0
        else:
            if df(x0) != 0:
                #x(k+1) = xk - f(xk)/f'(xk)
                x1 = x0 - f(x0)/df(x0)
                k += 1
                x0 = x1
    return "Error"

if __name__ == "__main__":
    #function = lambda x: np.cos(x) * np.cosh(x) - 1
    #derivada = lambda x: np.cos(x) * np.sinh(x) - np.sin(x) * np.cosh(x)
    function = lambda x: 1 + 2*x - 3*x**2*np.exp(-x) + 2*x**3*np.sin(x)*np.exp(-x/5)
    derivada = lambda x: 2 - 6*x*np.exp(-x) + 2*np.sin(x)*np.exp(-x/5) - 6*x**2*np.exp(-x) + 6*x**3*np.cos(x)*np.exp(-x/5) - 2*x**2*np.sin(x)*np.exp(-x/5) - 3*x**2*np.exp(-x) + 6*x**2*np.sin(x)*np.exp(-x/5) - 2*x**3*np.cos(x)*np.exp(-x/5) - 2*x**3*np.sin(x)*np.exp(-x/5)/5
    # la derivada es => 2 - 6x*exp(-x) + 2*sin(x)*exp(-x/5) - 6x^2*exp(-x) + 6x^3*cos(x)*exp(-x/5) - 2x^2*sin(x)*exp(-x/5) - 3x^2*exp(-x) + 6x^2*sin(x)*exp(-x/5) - 2x^3*cos(x)*exp(-x/5) - 2x^3*sin(x)*exp(-x/5)/5
    
    x0 = 6
    tol = .00001
    x = list(range(0,15))
    maxIter = 10000
    raiz = Newton(x0, function, derivada, tol, maxIter)
    print(raiz)
    #listaRaices = [Newton(x0, function, derivada, tol,maxIter) for _ in x]
    #print(listaRaices)
    
    # Graficamos la función
    import matplotlib.pyplot as plt
    x = np.linspace(0,2,100)
    y = function(x)
    plt.plot(x,y)
    plt.grid()
    plt.show()
    

