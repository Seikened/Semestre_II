import numpy as np
import matplotlib.pyplot as plt
import math

class Root:
    def __init__(self,f=None,a=None,b=None,g=None,df=None,tol=0.00001):
        self.f = f
        self.a = a
        self.b = b
        self.g = g
        self.df = df
        self.tol = tol
        self.max_iter =  100
        self.historico = []
        self.iteraciones = 0
        self.raiz = 0


    def biseccion(self): 
        a = self.a
        b = self.b
        f = self.f
        tol = self.tol
        max_iter = self.max_iter
        text = ""
        
        # Validar que los valores de a, b y f no sean nulos
        if a is None or b is None or f is None:
            raise Exception("Los valores de a, b o f no pueden ser nulos, tienes que definirlos")

        if np.sign(f(a)) == np.sign(f(b)):
            raise Exception("Los escalares a y b, no contienen una raiz")
            
        i = 0
        historico = []
        while i<max_iter:
            m = (a + b)/2
            R = m
            historico.append(R)
            if np.abs(f(m)) < tol:
                i = i+1
                break
            elif np.sign(f(a)) == np.sign(f(m)): 
                a = m
            else: 
                b = m
            i +=1
        historico = np.asarray(historico)
        self.historico = historico
        self.iteraciones = i
        text += ""


    def falsa_posicion(self,f, a, b, tol, max_iter):
        f = self.f
        a = self.a
        b = self.b
        tol = self.tol
        max_iter = self.max_iter
        
        
        # Validar que los valores de a, b y f no sean nulos
        if f  is None or a is None or b is None:
            raise Exception("Los escalares a y b no contienen una raíz entre ellos.")
        historico = []
        
        if np.sign(f(a)) == np.sign(f(b)):
            raise Exception("Los escalares a y b no contienen una raíz entre ellos.")
        
        i = 0
        c = a 
        while i < max_iter:
            c_old = c  
            c = a - ((f(a) * (b - a)) / (f(b) - f(a)))  
            historico.append(c)
            
            if np.abs(f(c)) < tol:  
                break
                
            if np.sign(f(a)) == np.sign(f(c)):
                a = c
            else:
                b = c

            if np.abs(c - c_old) < tol:  
                break
        
            i += 1
        historico = np.asarray(historico)
        self.iteraciones = i
        self.historico = historico  


    def punto_fijo(self,g, a, tol, max_iter):
        g = self.g
        a = self.a
        tol = self.tol
        max_iter = self.max_iter
        # Validar que los valores de g y a no sean nulos
        if g  is None or a is None:
            raise Exception("Los valores de g o a no pueden ser nulos, tienes que definirlos")
        
        historico = []
        x = a  
        for i in range(max_iter):
            x_nuevo = g(x)  
            historico.append(x_nuevo)
            if np.abs(x_nuevo - x) < tol:  
                break
            x = x_nuevo  
        historico = np.asarray(historico)
        self.historico = historico
        self.iteraciones = i + 1


    def newton(self):
        a = self.a
        f = self.f
        df = self.df
        tol = self.tol
        maxIter = self.max_iter
        
        # Validar que  f, a y df no sean nulos
        if f is None or df is None or a is None:
            raise Exception("Los valores de f, df o a no pueden ser nulos, tienes que definirlos")
        
        k = 0
        while k < maxIter: 
            if  abs(f(a)) <= tol:
                self.raiz = a
                self.iteraciones = k
                return ""
            else:
                if df(a) != 0:
                    x1 = a - f(a)/df(a)
                    self.historico.append(x1)
                    k += 1
                    a = x1
        return "No se encontro la raiz en las iteraciones dadas", k



# ------------------------------------------------------------------------------------------------------------

f = lambda x: 1 + 2*x - 3*x**2*np.exp(-x) + 2*x**3*np.sin(x)*np.exp(-x/5)
df = lambda x: 2 - 6*x*np.exp(-x) + 2*np.sin(x)*np.exp(-x/5) - 6*x**2*np.exp(-x) + 6*x**3*np.cos(x)*np.exp(-x/5) - 2*x**2*np.sin(x)*np.exp(-x/5) - 3*x**2*np.exp(-x) + 6*x**2*np.sin(x)*np.exp(-x/5) - 2*x**3*np.cos(x)*np.exp(-x/5) - 2*x**3*np.sin(x)*np.exp(-x/5)/5
a = 9
b = 19


ecuacionNewton = Root(f=f,a=a,df=df)

ecuacionNewton.newton()

iteraciones = ecuacionNewton.iteraciones
raiz = ecuacionNewton.raiz
historico = ecuacionNewton.historico

print(f"La raiz es: {raiz} y se encontró en {iteraciones} iteraciones con el método de Newton lista de historico: {historico}")





