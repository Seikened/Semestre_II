import sympy as sp
import os
import time
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Limpia la pantalla
os.system('cls' if os.name == 'nt' else 'clear')


# Códigos de colores ANSI para el arcoíris
colores_arcoiris = [31, 33, 32, 36, 34, 35]
def imprimir_arcoiris(texto, ciclos=1):
    texto_con_formato = ""
    for desplazamiento_color in range(len(texto)):
        texto_con_formato = ""
        for indice, char in enumerate(texto):
            color_actual = colores_arcoiris[(indice + desplazamiento_color) % len(colores_arcoiris)]
            texto_con_formato += f"\033[{color_actual}m{char}\033[0m"
        print(texto_con_formato, end='\r')
        sys.stdout.flush()
        time.sleep(0.1)
    print()  # Mover a la siguiente línea después de terminar la animación

def animar_sumas_riemann(f, a, b, n, metodo):
    """
    Crea una animación que muestra la construcción de las sumas de Riemann para una función dada.

    Parámetros:
    - f: Función lambda de sympy convertida para evaluación numérica.
    - a: Límite inferior del intervalo de integración.
    - b: Límite superior del intervalo de integración.
    - n: Número de subintervalos.
    - delta_x: Ancho de cada subintervalo.
    - metodo: Método de suma de Riemann ('izquierda', 'derecha', 'medio').

    La función plotea la función 'f' y superpone rectángulos que representan la suma de Riemann
    seleccionada, actualizando la vista para cada subintervalo.
    """
    delta_x = (b - a) / n
    fig, ax = plt.subplots()
    x_vals = np.linspace(a, b, 1000)
    y_vals = f(x_vals)
    ax.plot(x_vals, y_vals, 'r')

    def animate(i):
        ax.clear()
        ax.plot(x_vals, y_vals, 'r')
        ax.set_title(f'Suma de Riemann - Método: {metodo} - Rectángulo {i + 1}/{n}')
        for j in range(i + 1):
            xi = a + j * delta_x
            if metodo == 'izquierda':
                altura = f(xi)
            elif metodo == 'derecha':
                altura = f(xi + delta_x)
            elif metodo == 'medio':
                altura = f(xi + delta_x / 2)
            rect = plt.Rectangle((xi, 0), delta_x, altura, edgecolor='black', facecolor='cyan', alpha=0.5)
            ax.add_patch(rect)

    ani = animation.FuncAnimation(fig, animate, frames=n, repeat=False)
    plt.show()



# Función para calcular el error
def calcular_error(n, metodo):
    
    if metodo == 'izquierda':
        aproximacion = extremo_izquierdo(f, n, intervalo_a)
    elif metodo == 'derecha':
        aproximacion = extremo_derecho(f, n, intervalo_a)
    error = abs(aproximacion - integral_exacta)
    return error

# # Función para graficar los errores
# def graficar_errores():
#     ns = np.arange(5, 201, 1)  # Desde n=5 hasta n=200
#     errores_izquierda = [calcular_error(n, 'izquierda') for n in ns]
#     errores_derecha = [calcular_error(n, 'derecha') for n in ns]

#     plt.figure(figsize=(10, 6))
#     plt.plot(ns, errores_izquierda, label='Error Suma Izquierda', color='red')
#     plt.plot(ns, errores_derecha, label='Error Suma Derecha', color='blue')
#     plt.xlabel('Número de Rectángulos')
#     plt.ylabel('Error')
#     plt.title('Error de las Sumas de Riemann en función del número de rectángulos')
#     plt.legend()
#     plt.grid(True)
#     plt.show()

# # Llamamos a la función para graficar los errores
# graficar_errores()


# Imprime un mensaje de bienvenida con estilo arcoíris
imprimir_arcoiris("Bienvenido al cálculo de Sumas de Riemann")

x = sp.symbols('x')

# funcionUser = input("Ingrese la función a integrar: ")
intervalo_a = -1.5      #int(input("Ingrese el límite inferior del intervalo: ")
intervalo_b = .5        #int(input("Ingrese el límite superior del intervalo: ")
n =  [20,50,100]  #int(input("Ingrese el número de subintervalos: "))


f = lambda x: x**3 - (2*x) + 1   # Agrega "funcionUser" para que el usuario pueda ingresar una función desde la terminal
integral_exacta = sp.integrate(f(x), (x, intervalo_a, intervalo_b)) # Solo se utiliza para gráficos de errores no para el cálculo de las sumas de Riemann
# Define las funciones para cada método de Riemann
def extremo_izquierdo(f, n, intervalo_a):
    delta_x = (intervalo_b - intervalo_a) / n
    sumatoria = 0
    for i in range(1, n+1):
        extremo_izquierdo = intervalo_a + (i - 1) * delta_x
        sumatoria += f(extremo_izquierdo) * delta_x
    return sumatoria

def extremo_derecho(f, n, intervalo_a):
    delta_x = (intervalo_b - intervalo_a) / n
    sumatoria = 0
    for i in range(1, n+1):
        extremo_derecho = intervalo_a + i * delta_x
        sumatoria += f(extremo_derecho) * delta_x
    return sumatoria

def punto_medio(f, n, intervalo_a):
    delta_x = (intervalo_b - intervalo_a) / n
    sumatoria = 0
    for i in range(1, n+1):
        punto_medio = intervalo_a + (i - 0.5) * delta_x
        sumatoria += f(punto_medio) * delta_x
    return sumatoria


# Calcula los resultados para cada método con cada número de subintervalos
resultados_extremo_izq = [extremo_izquierdo(f, n_i, intervalo_a) for n_i in n]
resultados_extremo_der = [extremo_derecho(f, n_i, intervalo_a) for n_i in n]
resultados_punto_medio = [punto_medio(f, n_i, intervalo_a) for n_i in n]


# Imprimir los resultados en la terminal con efecto arcoíris por cada elemento de la lista
for i in range(len(resultados_extremo_izq)):
    # Imprime los resultados finales con efecto arcoíris
    imprimir_arcoiris(f"Resultado de la regla del extremo izquierdo: {resultados_extremo_izq[i]}")
    imprimir_arcoiris(f"Resultado de la regla del extremo derecho: {resultados_extremo_der[i]}")
    imprimir_arcoiris(f"Resultado de la regla del punto medio: {resultados_punto_medio[i]}")
    # Anima las sumas de Riemann para cada método de cada número de subintervalos
    animar_sumas_riemann(f, intervalo_a, intervalo_b, n[i], 'izquierda')
    animar_sumas_riemann(f, intervalo_a, intervalo_b, n[i], 'derecha')
    animar_sumas_riemann(f, intervalo_a, intervalo_b, n[i], 'medio')
