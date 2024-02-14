#Ejercicio No 5. Escribir una función que reciba una muestra de números en una lista y devuelva la suma de sus cuadrados
import random

suma_cuadrados = lambda num_list: sum((num**2) for num in num_list) # Suma de la lista

listaNumeros = [random.randint(1,100) for i in range(10)] # Genera lista aleatoria

sumaTotal = suma_cuadrados(listaNumeros)
print(f"De tu lista {listaNumeros} la suma de todos al cuadrado es {sumaTotal}")