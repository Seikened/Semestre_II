#3. Escriba una función llamada PreguntaLista que reciba como argumento un número entero mayor que 1 llamado n.
# Esta función debe preguntar al usuario por n números y agregarlos a una lista. 
# La función debe regresar (return) la lista con los n números.


def PreguntaLista(x):
    lista = []
    for i in range(x):
        Num = int(input(f"Introduce tu número {i+1}: "))
        lista.append(Num)
    return lista


numeroRepeticiones = int(input("¿Qué tamaño tiene tu lista? "))

ListaDeNumeros = PreguntaLista(numeroRepeticiones)

print(ListaDeNumeros)