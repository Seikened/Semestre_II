#Ejercicio 3. De la siguiente lista [8,14,22,3,7,28,36,49,52], indicar la cantidad de valores, la sumatoria y su promedio
lista = [8,14,22,3,7,28,36,49,52]

c = 0
sumatoria = 0
while c < len(lista):
    i = lista[c]
    sumatoria += i
    c += 1

promedio = sumatoria/c
print(f"""
El promedio es {promedio} 
La cantidad de valores es: {c}
La sumatoria es {sumatoria}""")