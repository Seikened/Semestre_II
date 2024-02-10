#6. Escriba una función llamada Descendente que recibe como argumento una lista y regresa 
# True (verdadero) si los elementos de la lista están en orden descendente, y False (falso) si no lo están. 
# Es decir, si la lista es [500,450,201,50] la función debe regresar True. 
# Si la lista es [500,450,201,500], entonces debe regresar false.


def Desendiente(listaUser):
    listaOrdenada = listaUser.copy()
    lenLista = len(listaUser)
    for item in range(lenLista - 1):
        for position in range(0, lenLista - item - 1):
            if listaOrdenada[position] < listaOrdenada[position + 1]:

                listaOrdenada[position], listaOrdenada[position + 1] = listaOrdenada[position + 1], listaOrdenada[position]


    listaUserInvertida = listaUser[::-1]
    if listaUserInvertida == listaOrdenada:
        return True
    else:
        return False


tamLista = int(input("¿De qie tamaño quieres tu lista? "))

listaUser = []
for i in range(tamLista):
    num = int(input(f"Introduce tu número {i+1}: "))
    listaUser.append(num)

if Desendiente(listaUser):
    print(f"Tu lista {listaUser} esta bien ordenada")
else:
    print(f"Tu lista {listaUser} no esta bien ordenada")

