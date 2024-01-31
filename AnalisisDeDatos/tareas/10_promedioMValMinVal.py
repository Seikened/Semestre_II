import random

def Max_min(lista):
    max = -9999999
    min = 9999999
    for num in lista:
        if num >= max:
            max = num
        if num <= min:
            min = num
    return min,max



def Promedio(lista):
    sum = 0
    for num in lista:
        sum += num
    return round(sum / (len(lista)),2)



#-------------#-------------#-------------#-------------#-------------

tam_lista = int(input("De que tamaño será tu lista de números: "))
lista_num = []
for i in range(tam_lista):
    #input(f"Dame el no. {i+1}: ")
    lista_num.append( round( random.uniform(1,10) , 2 ) )

prom = Promedio(lista_num)
min,max = Max_min(lista_num)

print(f"Tu lista es: {lista_num} y el valor máximo es: {max} y el mínimo es: {min} y el promedio de tu lista es: {prom}")




