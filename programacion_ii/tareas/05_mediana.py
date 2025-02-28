#7. Escriba una función llamada Mediana que recibe como argumento una lista de valores flotantes y regresa el 
# promedio de esa lista como un flotante. La función debe trabajar bien con listas de cualquier tamaño. 
# Para calcular la mediana primero debe ordenar la lista y después tomar el valor que se encuentre 
# en la mitad de la lista. Si la lista tiene un numero non de elementos, debe tomar el elemento que 
# queda exactamente en la mitad (ejemplo, si la lista tiene 5 elementos, la mediana es el tercer 
# elemento de la lista ordenada). Si la lista tiene un numero par, puede tomar el elemento que se
# encuentra uno arriba de la mitad (por ejemplo, si tiene 6 elementos, puede tomar el elemento en la cuarta posición).

def Ascendiente(listaUser):
    listaOrdenada = listaUser.copy()
    lenLista = len(listaUser)
    for item in range(lenLista - 1):
        for position in range(0, lenLista - item - 1):
            if listaOrdenada[position] > listaOrdenada[position + 1]:
                listaOrdenada[position], listaOrdenada[position + 1] = listaOrdenada[position + 1], listaOrdenada[position]
                
    return listaOrdenada

def Mediana(listaUser):
    listaOrdenada = Ascendiente(listaUser)
    totalLista = len(listaOrdenada)
    if totalLista%2 == 0: # Si la lista es par
        return ((listaOrdenada[totalLista//2-1]) + (listaOrdenada[(totalLista//2)]))/2
    else:
        return listaOrdenada[(totalLista//2)]


# Aquí empieza
tamLista = int(input("¿De qie tamaño quieres tu lista? "))

listaUser = []
for i in range(tamLista):
    num = float(input(f"Introduce tu número {i+1}: "))
    listaUser.append(num)


mediana = Mediana(listaUser)

print(f"Tu mediana es {mediana} de tu lista {Ascendiente(listaUser)}")




lista = [1,26,3,9,5]

lista = lista.sort()

lista = sorted(lista)