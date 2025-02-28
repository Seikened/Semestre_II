#Ejercicio No 7. Escribir una función que reciba una nuestra de números en una lista y devuelva el número menor

import random

def menor_lista(lista):
    menor = 9999999
    for num in lista:
        menor = num if num < menor else menor
    return menor

lista = [random.randint(1,100) for i in range(20)]
menorLista = menor_lista(lista)
print(f"El menor de la lista {lista}\n es {menorLista}")
