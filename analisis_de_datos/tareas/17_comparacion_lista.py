# Ejercicio 5. Realizar un programa que permita cargar dos listas de N valores cada una. 
# Informar con un mensaje cuál de las dos listas tiene un valor acumulado mayor 
# (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")


numLenLista1 = int(input("De que tamaño será tu lista 1: "))
c = 0
sumatoriaLista1 = 0
while c < numLenLista1:
    numUser1 = int(input(f"Cual es tu número {c+1} de tu lista 1: "))
    sumatoriaLista1 += numUser1
    c+=1

numLenLista2 = int(input("De que tamaño será tu lista 2: "))
c = 0
sumatoriaLista2 = 0
while c < numLenLista2:
    numUser2 = int(input(f"Cual es tu número {c+1} de tu lista 2: "))
    sumatoriaLista2 += numUser2
    c+=1

if sumatoriaLista1 > sumatoriaLista2:
    print(f"La lista uno es más grande con un valor total de {sumatoriaLista1}")
elif sumatoriaLista2 > sumatoriaLista1:
    print(f"La lista dos es más grande con un valor total de {sumatoriaLista2}")
else:
    print("Las dos listas son iguales")
