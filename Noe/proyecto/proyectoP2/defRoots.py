import numpy as np
import matplotlib.pyplot as plt

class Root:
    def __init__(self,f,a,b=None,g=None,df=None,tol=0.00001,max_iter=100):
        self.f = f
        self.a = a
        self.b = b
        self.g = g
        self.df = df
        self.tol = tol
        self.max_iter = max_iter
        self.historico = []
        self.iteraciones = 0
        self.raices = []


    def biseccion(self): 
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




    def falsa_posicion(f, a, b, tol, max_iter):
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





    def punto_fijo(g, a, tol, max_iter):
        historico = []
        x = a  # Iniciar con el valor inicial x0

        for i in range(max_iter):
            x_nuevo = g(x)  # Calcular el nuevo punto usando g(x)
            historico.append(x_nuevo)

            if np.abs(x_nuevo - x) < tol:  # Verificar la condición de parada
                break

            x = x_nuevo  # Actualizar x para la próxima iteración

        historico = np.asarray(historico)
        return historico, i + 1  # i + 1 para contar la iteración inicial


    def newton(a,f,df, tol,maxIter=100):
        k = 0
        while k < maxIter:
            # Evaluar si xk es la solición
            if  abs(f(a)) <= tol:
                # xk es la raiz y el programa termina
                return a, k
            else:
                if df(a) != 0:
                    #x(k+1) = xk - f(xk)/f'(xk)
                    x1 = a - f(a)/df(a)
                    k += 1
                    a = x1
        return "No se encontro la raiz en las iteraciones dadas", k
