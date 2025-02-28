# Resuelve el ejercicio aquí.
import matplotlib.pyplot as plt
import math

def Calcular_ley_enfriamiento_newton(tiempo, cuerpo, k, e, temp_inicial):
    """
    Calcula la temperatura de un cuerpo en un tiempo dado.
    Las entradas son:
    tiempo -- tiempo en segundos
    cuerpo -- temperatura del cuerpo en grados centígrados
    k -- constante de enfriamiento
    e -- constante de Euler
    temp_inicial -- temperatura inicial del cuerpo en grados centígrados
    Y devuelve la temperatura del cuerpo en grados centígrados.
    """
    return ((temp_inicial - cuerpo) * (e ** (-k * tiempo))) + cuerpo

if __name__ == "__main__":
    lista_tiempo = list(range(0,41))
    cuerpo = 15
    k = 0.0367
    e = 2.71828
    temp_inicial = 30
    
    valores_enfriamento = []
    for tiempo in lista_tiempo:
        print("Tiempo: ", tiempo, "Temperatura: ", Calcular_ley_enfriamiento_newton(tiempo, cuerpo, k, e, temp_inicial))
        valores_enfriamento.append(Calcular_ley_enfriamiento_newton(tiempo, cuerpo, k, e, temp_inicial))
    
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(lista_tiempo, valores_enfriamento, color = 'm',linewidth = 2.5, linestyle ='-', label = 'Enfriamiento')
    plt.title("Enfriamiento de un baso de agua")
    plt.xlabel("Tiempo")
    plt.ylabel("Temperatura")
    plt.grid()
    plt.legend()
    plt.show()