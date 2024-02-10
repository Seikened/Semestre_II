# Ejercicio 6. De la siguiente lista [16,25,16,99,48,67,37,10,42,56,29,79,34,55], 
# Mostrar para cada valor: El Valor, su valor al cuadrado, su raíz cuadrada y su recíproco.

lista = [16,25,16,99,48,67,37,10,42,56,29,79,34,55]

print(f"{'VALOR':<10} | {'CUADRADO':<10} | {'RAÍZ CUADRADA':<14} | {'RECÍPROCO':<10}")  
print("-" * 55)  

c = 0
while c < len(lista):
    n = lista[c]
    cuadrado = n**2
    raiz = n**(1/2)
    reciproco = 1/n
    print(f"{n:<10} | {cuadrado:<10.2f} | {raiz:<14.2f} | {reciproco:<10.2f}")
    c+=1