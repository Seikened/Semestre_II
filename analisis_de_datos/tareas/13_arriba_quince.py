# Ejercicio 2. De la siguiente lista [8,14,22,3,7,28,36,49,52], indicar cuantos números están por encima de 15

lista = [8,14,22,3,7,28,36,49,52]

c = 0
arribaQuince = 0
while c < len(lista):
    i = lista[c]
    if i > 15:
        arribaQuince += 1
    c += 1

print(f"Hay {arribaQuince} números arriba del 15")