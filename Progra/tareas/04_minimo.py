#5. Escriba una función llamada Minimo que recibe como argumento una lista de valores 
# enteros y regresa el valor más bajo de esa lista como un entero.
# Nota: La función no debe alterar la lista original.



def Minimo(listaNumeros):
    numeroMenor = 99999
    for i in listaNumeros:
        if i<= numeroMenor:
            numeroMenor = i 
    return numeroMenor

cantidadNumeros = int(input("¿De que tamaño sera tu lista? "))
lista = []
for i in range(cantidadNumeros):
    num = int(input("Introduce tu número: "))
    lista.append(num)

numMenor = Minimo(lista)
print(numMenor)

