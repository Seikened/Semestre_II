# Ejercicio 4. Realiza un programa que pida 2 números enteros, e imprima los números impares que existen entre los 2 valores
uno = int(input("Dame tu primer número entero: "))
dos = int(input("Dame tu segundo número entero: "))
totalImpares = 0
c = uno
while c < dos:
    if c % 2 != 0:
        print(f"Número impar es: {c}")
        totalImpares += 1
    c+=1
print(f"Termine, hay {totalImpares} de números impares")


