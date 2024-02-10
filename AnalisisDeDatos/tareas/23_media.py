#Ejercicio No 4. Escribir una función que reciba una muestra de números en una lista y devuelva su media
import random
def Mediana(num_list):
    total_sum = 0
    for num in num_list:
        total_sum += num
    return total_sum/len(num_list)




lista_numeros = [(random.randint(1,100)) for i in range(10)]
promedio = Mediana(lista_numeros)

print(f"El promedio de {lista_numeros} \n es: {promedio}")