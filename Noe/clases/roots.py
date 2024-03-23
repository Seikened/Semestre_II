import numpy as np

def biseccion(f,a,b,tol=0.00001):
    """
    Esta función implementa el método de biseccion.
    Calcula una solución aproximada de f(x)=0
    Entrada: Expresión de la función f, a,b y la tolerancia TOL
    Salida: Solución aproximada xc
    """
    if( np.sign(f(a))*np.sign(f(b))>=0 ):
        raise Exception("¡No se sataisface la condición f(a)f(b)<0 y el intervalo [a,b] no contiene una raiz para la función dada!")
    
    fa = f(a)
    fb = f(b)
    iterations = 0
    while ((b-a)/2 > tol):
        c  = (a+b)/2
        fc = f(c)

        if(abs(fc) < 0.0001): 
            return c , iterations

        if( np.sign(f(a))*np.sign(f(c))<0 ):
            b  = c
            fb = fc
        else:
            a  = c
            fa = fc

        iterations += 1

    return (a+b)/2, iterations


def punto_fijo(g,x0,iter_max=1000,ea=100,es=0.0001):
    """
    Esta función implementa el método de Punto Fijo.
    Calcula una solución aproximada de g(x) = x
    Entrada: Expresión de la función g, 
    iniciando en el supuesto x0
    Salida: Solución aproximada xc
    """
    
    xc = x0
    iterations = 0
    while ((ea > es ) and ( iter_max > iterations )):
        x0 = xc
        xc = g(x0)
        iterations += 1
        ea = abs((xc - x0)/xc)*100
        
    return xc, iterations, ea

def derivative(f, x, h=1e-5):
    """
    Calcula la derivada numérica de una función en un punto dado utilizando el método de diferencia finita.

    Args:
        f (function): La función para la cual calcular la derivada.
        x (float): El punto en el que se calculará la derivada.
        h (float): El tamaño del paso. Valor predeterminado es 1e-5.

    Returns:
        float: El valor aproximado de la derivada en el punto dado.
    """
    return (f(x + h) - f(x)) / h

def newton_raphson(x_init,f,fdot=None,eps=0.0001,max_it=100,error=100):
    """
    Parámetros de entrada:
    x0: Valor inicial
    f : Función
    fdot: Derivada de la Función
    max_it: Número de iteraciones
    error: |x_{k+1} - x_{k}|
    """
    iterations = 0
    while( (error > eps) and (iterations <= max_it) ):
        x_next = x_init - f(x_init)/(derivative(f,x_init))
        #x_next = x_init - f(x_init)/fdot(x_init)
        error  = abs(x_next - x_init)
        x_init = x_next
        iterations += 1
        
    return x_next, iterations, error


def falsa_posicion(f, a, b, tol=1e-6, max_iter=1000):
    """
    Método de la posición falsa para encontrar la raíz de una función f(x) en el intervalo [a, b].
    
    Args:
        f (function): La función para la cual encontrar la raíz.
        a (float): Extremo izquierdo del intervalo.
        b (float): Extremo derecho del intervalo.
        tol (float): Tolerancia para la convergencia. El valor predeterminado es 1e-6.
        max_iter (int): Número máximo de iteraciones permitidas. El valor predeterminado es 1000.
    
    Returns:
        float or None: La aproximación de la raíz encontrada o None si no se pudo encontrar.
    """
    # Verificar que f(a) y f(b) tienen signos opuestos
    if f(a) * f(b) >= 0:
        print("Los extremos del intervalo deben tener signos opuestos.")
        return None
    
    # Inicializar variables
    x0, x1 = a, b
    iteration = 0
    
    # Iterar hasta alcanzar la tolerancia o el número máximo de iteraciones
    while iteration < max_iter:
        # Calcular la aproximación de la raíz
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        
        # Verificar si la aproximación cumple con la tolerancia
        if abs(f(x2)) < tol:
            print(f"Raíz encontrada con tolerancia {tol} en la iteración {iteration}.")
            return x2
        
        # Actualizar los extremos del intervalo
        if f(x2) * f(x0) < 0:
            x1 = x2
        else:
            x0 = x2
        
        iteration += 1
    
    print(f"No se pudo encontrar la raíz después de {max_iter} iteraciones.")
    return None