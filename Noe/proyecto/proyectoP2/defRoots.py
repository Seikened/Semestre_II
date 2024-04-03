import numpy as np
import matplotlib.pyplot as plt
import math

class Root:
    def __init__(self,f=None,a=None,b=None,g=None,df=None):
        self.f = f
        self.a = a
        self.b = b
        self.g = g
        self.df = df
        self.tol = .00001
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
        self.raiz = m
        text += ""


    def falsa_posicion(self):
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
        self.raiz = c


    def punto_fijo(self):
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
        self.raiz = x


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
    
    def __str__(self):
        return f"La raiz es: {self.raiz} y se encontró en {self.iteraciones} iteraciones con el método de Newton lista de historico: {self.historico}"



# ------------------------------------------------------------------------------------------------------------

f = lambda x: 1 + 2*x - 3*x**2*np.exp(-x) + 2*x**3*np.sin(x)*np.exp(-x/5)
df = lambda x: 2 - 6*x*np.exp(-x) + 2*np.sin(x)*np.exp(-x/5) - 6*x**2*np.exp(-x) + 6*x**3*np.cos(x)*np.exp(-x/5) - 2*x**2*np.sin(x)*np.exp(-x/5) - 3*x**2*np.exp(-x) + 6*x**2*np.sin(x)*np.exp(-x/5) - 2*x**3*np.cos(x)*np.exp(-x/5) - 2*x**3*np.sin(x)*np.exp(-x/5)/5
a = 18
b = 19
g_de_x = lambda x: np.arcsin((-1 - 2*x + 3*x**2 * np.exp(-x)) / (2*x**3 * np.exp(-x/5)))


ec_biseccion = Root(f=f,a=a,b=b)
ec_false_position = Root(f=f,a=a,b=b)
ec_punto_fijo = Root(g=g_de_x,a=a)
ec_newton = Root(f=f,a=a,df=df)


# Resuelvo la ecuaciónes
ec_biseccion.biseccion()
ec_false_position.falsa_posicion()
#ec_punto_fijo.punto_fijo()
ec_newton.newton()

# print de cada ecuación
print("Bisección")

print(ec_biseccion)
print("-"*50)
print("Falsa posición")
print(ec_false_position)
print("-"*50)
print("Punto fijo")
#print(ec_punto_fijo)
#print("-"*50)
print("Newton")
print(ec_newton)