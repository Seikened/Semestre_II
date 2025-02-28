import numpy as np
import matplotlib.pyplot as plt
import math

class Root:
    def __init__(self,f=None,a=None,b=None,g=None,df=None):
        
        """
        Esta clase se utiliza para encontrar raíces de una función mediante diferentes métodos numéricos.

        Atributos:
            f (callable): La función para la cual se buscan las raíces.
            a (float): El límite inferior del intervalo en algunos métodos.
            b (float): El límite superior del intervalo en algunos métodos.
            g (callable): La función utilizada en el método de punto fijo.
            df (callable): La derivada de la función f, utilizada en el método de Newton.
            tol (float): La tolerancia para la convergencia de los métodos.
            max_iter (int): El número máximo de iteraciones permitidas.
            historico (list): Almacena las aproximaciones sucesivas de la raíz en cada iteración.
            iteraciones (int): El número de iteraciones realizadas para encontrar la raíz.
            raiz (float): La aproximación de la raíz encontrada.
            text (str): Almacena información textual sobre el proceso de iteración.
        """
        
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
        """
        Implementa el método de bisección para encontrar la raíz de la función f en el intervalo [a, b].

        Este método divide sucesivamente el intervalo y selecciona el subintervalo que contiene la raíz.
        La convergencia ocurre cuando el ancho del intervalo es menor que la tolerancia especificada.
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
        
        while i < max_iter:
            m = (a + b) / 2
            R = m
            historico.append(R)
            
            f_a = f(a)
            f_b = f(b)
            f_m = f(m)
            
            # Añadir los valores para la iteración actual a la variable text
            text += "|{:^12}|{:^12.8f}|{:^12.8f}|{:^12.8f}|{:^12.8f}|{:^12.8f}|{:^12.8f}|\n".format(i+1, a, b, m, f_a, f_b, f_m)
            
            if np.abs(f_m) < tol:
                break
            elif np.sign(f_a) == np.sign(f_m):
                a = m
            else:
                b = m

            i += 1

        self.historico = np.asarray(historico)
        self.iteraciones = i+1
        self.raiz = m
        self.text += text


    def falsa_posicion(self):
        
        """
        Implementa el método de la falsa posición (regla falsi) para encontrar la raíz de la función f en el intervalo [a, b].

        Este método es similar a la bisección pero usa una línea recta para aproximar la función en el intervalo, seleccionando el punto de intersección con el eje x como la nueva aproximación.
        """
        
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
        
        historico = np.asarray(historico)
        self.iteraciones = i
        self.historico = historico  
        self.raiz = c
        self.text = text


    def punto_fijo(self):
        
        """
        Implementa el método del punto fijo para encontrar una raíz de la función.

        Partiendo de un punto inicial 'a', se itera con la función g(x) hasta que la secuencia converge a un punto fijo, que es una raíz de f.
        """
        
        g = self.g
        x0 = self.a
        tol = self.tol
        max_iter = self.max_iter
        derivada = self.df
        text = ""
        
        historico = []
        x = x0  # Iniciar con el valor inicial x0
        num_iteraciones = 0  # Inicializar contador de iteraciones
    
        text += "| {:^10} | {:^10} | {:^10} |\n".format("Iteración", "x", "g(x)")
        text += "-" * 40 + "\n"
        
        for _ in range(max_iter):
            x_nuevo = g(x)  # Calcular el nuevo punto usando g(x)
            historico.append(x_nuevo)

            if np.abs(x_nuevo - x) < tol:  # Verificar la condición de parada
                break

            # Añadir los valores para la iteración actual a la variable text
            text += "|{:^12}|{:^12.8f}|{:^12.8f}|\n".format(num_iteraciones+1, x, x_nuevo)

            x = x_nuevo  # Actualizar x para la próxima iteración
            num_iteraciones += 1
        
        historico = np.asarray(historico)
        self.historico = historico
        self.iteraciones = num_iteraciones
        self.raiz = x_nuevo
        self.text = text


    def newton(self):
        
        """
        Implementa el método de Newton-Raphson para encontrar la raíz de la función f.

        Este método utiliza la derivada de la función (df) para obtener una mejor aproximación de la raíz partiendo de un punto inicial 'a'. La iteración continúa hasta que se alcanza la convergencia.
        """
        
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


    def graficar(self):
        
        """
        Grafica la función f y las aproximaciones sucesivas de la raíz encontradas por el método numérico utilizado.

        Muestra dos gráficos: uno para la función con las aproximaciones de la raíz y otro para el error absoluto de las aproximaciones en escala logarítmica por iteración.
        """
        
        if self.b is not None:
            X = np.linspace(self.a, self.b, 200, endpoint=True)
        else:
            # Ajuste del rango de X si self.b es None
            X = np.linspace(self.a, max(self.historico), 200, endpoint=True)

        # Verificar si self.f está definido y calcular Y en consecuencia
        if self.f is not None:
            Y = self.f(X)
        else:
            # Usar self.g si self.f es None
            Y = self.g(X)

        fig, ax = plt.subplots(1, 2, figsize=(14, 5))

        # Gráfico de la función y las iteraciones
        ax[0].plot(X, Y, label="$f(x)$" if self.f is not None else "$g(x)$", color='blue')
        ax[0].plot(self.historico, [self.f(x) for x in self.historico] if self.f is not None else [self.g(x) for x in self.historico], 'ro-', label="Iteraciones")
        ax[0].axhline(0, color='black', lw=0.5)
        ax[0].legend()
        ax[0].set_title('Convergencia hacia la raíz')
        ax[0].set_xlabel('x')
        ax[0].set_ylabel('$f(x)$' if self.f is not None else '$g(x)$')
        ax[0].grid(True)

        # Anotación de la raíz
        ax[0].annotate('Raiz', xy=(self.raiz, 0), xytext=(self.raiz, self.f(self.raiz)/2 if self.f is not None else self.g(self.raiz)/2),
                    arrowprops=dict(facecolor='green', shrink=0.05))

        # Gráfico del error por iteración
        ax[1].plot(np.abs([self.f(x) for x in self.historico] if self.f is not None else [self.g(x) for x in self.historico]), 'bo-', label="Error")
        ax[1].set_yscale('log')
        ax[1].legend()
        ax[1].set_title('Error por iteración')
        ax[1].set_xlabel('Iteración')
        ax[1].set_ylabel('|f(x)|' if self.f is not None else '|g(x)|')
        ax[1].grid(True)

        plt.tight_layout()
        plt.show()


    def __str__(self):
        """
        Devuelve una representación en cadena del proceso de iteración, incluyendo las aproximaciones de la raíz, el número de iteraciones y la raíz encontrada.
        """
        return f"\n {self.text} \n Raiz encontrada: {self.raiz} \n Iteraciones: {self.iteraciones}"

