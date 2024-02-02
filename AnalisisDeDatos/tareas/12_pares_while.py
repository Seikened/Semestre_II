# Ejercicio 1. De la siguiente lista , indicar cuantos números son pares

lista = [8,14,22,3,7,28,36,49,52]

c = 0
pares = 0
while c < len(lista):
    i = lista[c]
    if i % 2 == 0:
        pares += 1
    c += 1

print(f"Hay {pares} pares")