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
        self.text = ""


    def biseccion(self):
        
        """Esto es una función que calcula la raiz de una función f, en un intervalo (a,b) usando el método de bisección
        Raises:Exception: Si los valores de a, b y f son nulos
        Returns:_type_: historico, i
        """
        
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

        text += "| {:^10} | {:^10} | {:^10} | {:^10} | {:^10} | {:^10} | {:^10} |\n".format("Iteración", "a", "b", "m", "f(a)", "f(b)", "f(m)")
        text += "-" * 92 + "\n"
        
        while i<max_iter:
            m = (a + b)/2
            R = m
            historico.append(R)
            
            f_a = f(a)
            f_b = f(b)
            f_m = f(m)
            
            # Añadir los valores para la iteración actual a la variable text
            text += "|{:^12}|{:^12.8f}|{:^12.8f}|{:^12.8f}|{:^12.8f}|{:^12.8f}|{:^12.8f}|\n".format(i+1, a, b, m, f_a, f_b, f_m)
            
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
        self.text += text


    def falsa_posicion(self):
        f = self.f
        a = self.a
        b = self.b
        tol = self.tol
        max_iter = self.max_iter
        text = ""
        
        
        # Validar que los valores de a, b y f no sean nulos
        if f  is None or a is None or b is None:
            raise Exception("Los escalares a y b no contienen una raíz entre ellos.")
        historico = []
        
        if np.sign(f(a)) == np.sign(f(b)):
            raise Exception("Los escalares a y b no contienen una raíz entre ellos.")
        
        i = 0
        c = a 
        text += "| {:^10} | {:^10} | {:^10} | {:^10} | {:^10} | {:^10} | {:^10} |\n".format("Iteración", "a", "b", "c", "f(a)", "f(b)", "f(c)")
        text += "-" * 92 + "\n"
        while i < max_iter:
            c_old = c  
            c = a - ((f(a) * (b - a)) / (f(b) - f(a)))  
            historico.append(c)
            
            
            f_a = f(a)
            f_b = f(b)
            f_c = f(c)

            # Añadir los valores para la iteración actual a la variable text
            text += "|{:^12}|{:^12.8f}|{:^12.8f}|{:^12.8f}|{:^12.8f}|{:^12.8f}|{:^12.8f}|\n".format(i+1, a, b, c, f_a, f_b, f_c)

            i += 1
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
        self.text = text


    def punto_fijo(self):
        g = self.g
        a = self.a
        tol = self.tol
        max_iter = self.max_iter
        text = ""
        
        # Validar que los valores de g y a no sean nulos
        if g is None or a is None:
            raise Exception("Los valores de g o a no pueden ser nulos, tienes que definirlos")
        
        historico = []
        x = a
        text += "| {:^10} | {:^10} | {:^10} |\n".format("Iteración", "x", "g(x)")
        text += "-" * 40 + "\n"
        
        for i in range(max_iter):
            x_nuevo = g(x)
            historico.append(x_nuevo)
            
            # Añadir los valores para la iteración actual a la variable text
            text += "|{:^12}|{:^12.8f}|{:^12.8f}|\n".format(i+1, x, x_nuevo)
            
            if np.abs(x_nuevo - x) < tol:
                break
            x = x_nuevo
        
        historico = np.asarray(historico)
        self.historico = historico
        self.iteraciones = i + 1
        self.raiz = x
        self.text = text



    def newton(self):
        a = self.a
        f = self.f
        df = self.df
        tol = self.tol
        maxIter = self.max_iter
        text = ""
        
        # Validar que  f, a y df no sean nulos
        if f is None or df is None or a is None:
            raise Exception("Los valores de f, df o a no pueden ser nulos, tienes que definirlos")
        
        k = 0
        while k < maxIter: 
            if  abs(f(a)) <= tol:
                self.raiz = a
                self.iteraciones = k
                self.historico.append(a)
                self.text = text
                return ""
            else:
                if df(a) != 0:
                    x1 = a - f(a)/df(a)
                    self.historico.append(x1)
                    if k == 0:
                        text += "| {:^10} | {:^10} | {:^10} | {:^10} | {:^10} |\n".format("Iteración", "x", "f(x)", "f'(x)", "x+1")
                        text += "-" * 66 + "\n"
                    text += "|{:^12}|{:^12.8f}|{:^12.8f}|{:^12.8f}|{:^12.8f}|\n".format(k+1, a, f(a), df(a), x1)
                    k += 1
                    a = x1
                    
        return "No se encontro la raiz en las iteraciones dadas", k
    
    def __str__(self):
        return f"\n {self.text} \n Raiz encontrada: {self.raiz} \n Iteraciones: {self.iteraciones}"




































































































































































































































































































































































print("CODIGO DE FERNANDO Y LAS BEBES ME ESTAN COPIANDO")

















































































































































































































































































































