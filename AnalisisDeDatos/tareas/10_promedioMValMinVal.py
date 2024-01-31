def Max_min(lista):
    pass
def Promedio(lista):
    pass
#-------------#-------------#-------------#-------------#-------------

tam_lista = int(input("De quer tamaño será tu lista de números: "))
lista_num = []
for i in range(tam_lista):
    lista_num.append(num_user = float(input(f"Dame el no. {i+1}: ")))

prom = Promedio(lista_num)
min,max = Max_min(lista_num)

print(f"El valor máximo es: {max} y el mínimo es: {min} y el promedio de tu lista es: {prom}")




