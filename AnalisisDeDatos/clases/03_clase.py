#  Ciclo while
c = 0
while c < 10:
    c += 1
    print(f"El valor de C es {c}")
    



datos = ["Alex", "Role",25,1.67,True]
x = 0
while x < len(datos):
    print(f"Valor: {datos[x]}")
    x += 1
    

# Determinar un salto

a = 0

while a < 10:
    a += 1
    if a == 5:
        print("Salta a la siguiente iteración")
        continue
    print(f"El valor de a es {a}")



# EJERCICIO 1
# PREGUNTAR VALORES HASTA QUE SE INGRESE UN -1 (el registro de -1 no se cuenta en la suma ni en el promedio de los valores)
user = 0
suma = 0
r = 0

while user != -1:
    user = int(input("Ingrese un valor: "))
    suma += user
    r += 1

print(f"""
- La suma de los valores ingresados es: {suma+1}
- El promedio de los valores ingresados es: {(suma+1)/(r-1)}
- La cantidad de valores ingresados es: {r-1}""")


# Pedir un número e indicar cuantos pares hay entre el 1 y el número ingresado
cont = 1
num = int(input("Ingrese un número: "))
pares = 0
while cont <= num:
    if cont % 2 == 0:
        pares += 1
    cont += 1
print(f"La cantidad de números pares entre 1 y {num} es: {pares}")


print("------------------------------------------------------------------------------------------------------------------------")

datos = [15,3,10,4,21,6,7,8,11,14,23]


cantidadValores = 0
sumaDatos = 0
paresValores = 0
valoresmayoresDIez = 0
multiplosTres = 0
deviasionEstandar = 0

i = 0

while i < len(datos):
    cantidadValores += 1
    sumaDatos += i
    if i % 2 == 0:
        paresValores += 1
    if i > 10:
        valoresmayoresDIez += 1
    if i % 3 == 0:
        multiplosTres += 1
    i += 1

promediovalores = sumaDatos/cantidadValores

sumatoria = 0

while i < len(datos):
    sumatoria += (datos[i]-promediovalores)**2

vanriaza = (sumaDatos/cantidadValores)**(.5)
desvEstandar = vanriaza**2

print(f"""
- La cantidad de valores ingresados es: {cantidadValores}
- La suma de los valores ingresados es: {sumaDatos}
- La cantidad de valores pares es: {paresValores}
- La cantidad de valores mayores a 10 es: {valoresmayoresDIez}
- La cantidad de valores multiplos de 3 es: {multiplosTres}
- El promedio de los valores ingresados es: {promediovalores}

- Varianza {vanriaza}
- Desviación estándar {desvEstandar} """)
