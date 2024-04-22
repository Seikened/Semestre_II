import sympy as sp
import os
import time
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Limpia la pantalla
os.system('cls' if os.name == 'nt' else 'clear')

x = sp.symbols('x')  # Define x como símbolo matemático

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

def animar_sumas_riemann(f, a, b, n, delta_x, metodo):
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

# Imprime un mensaje de bienvenida con estilo arcoíris
imprimir_arcoiris("Bienvenido al cálculo de Sumas de Riemann")

funcion_usuario = input("Ingrese la función a evaluar en términos de x: ")
intervalo_a = float(input("Ingrese el intervalo a: "))
intervalo_b = float(input("Ingrese el intervalo b: "))
n = int(input("Ingrese el número de subintervalos: "))
delta_x = (intervalo_b - intervalo_a) / n
f = sp.lambdify(x, sp.sympify(funcion_usuario))

# Define las funciones para cada método de Riemann
def extremo_izquierdo(f, n, delta_x, intervalo_a):
    sumatoria = 0
    for i in range(1, n+1):
        extremo_izquierdo = intervalo_a + (i - 1) * delta_x
        sumatoria += f(extremo_izquierdo) * delta_x
    return sumatoria

def extremo_derecho(f, n, delta_x, intervalo_a):
    sumatoria = 0
    for i in range(1, n+1):
        extremo_derecho = intervalo_a + i * delta_x
        sumatoria += f(extremo_derecho) * delta_x
    return sumatoria

def punto_medio(f, n, delta_x, intervalo_a):
    sumatoria = 0
    for i in range(1, n+1):
        punto_medio = intervalo_a + (i - 0.5) * delta_x
        sumatoria += f(punto_medio) * delta_x
    return sumatoria


# Calcula los resultados para cada método
resultado_extremo_izq = extremo_izquierdo(f, n, delta_x, intervalo_a)
resultado_extremo_der = extremo_derecho(f, n, delta_x, intervalo_a)
resultado_punto_medio = punto_medio(f, n, delta_x, intervalo_a)

# Imprime los resultados finales con efecto arcoíris
imprimir_arcoiris(f"Resultado de la regla del extremo izquierdo: {resultado_extremo_izq}")
imprimir_arcoiris(f"Resultado de la regla del extremo derecho: {resultado_extremo_der}")
imprimir_arcoiris(f"Resultado de la regla del punto medio: {resultado_punto_medio}")

# Anima las sumas de Riemann para cada método
animar_sumas_riemann(f, intervalo_a, intervalo_b, n, delta_x, 'izquierda')
animar_sumas_riemann(f, intervalo_a, intervalo_b, n, delta_x, 'derecha')
animar_sumas_riemann(f, intervalo_a, intervalo_b, n, delta_x, 'medio')
