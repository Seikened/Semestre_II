#Ejercicio No 6. Crea un programa que pida dos números enteros al usuario y diga si alguno de ellos es múltiplo del otro.

multiplo_num = lambda numOne,numTwo: f" {numOne} y {numTwo}  son multiplos" if (numOne%numTwo == 0) or (numTwo%numOne == 0) else f" {numOne} y {numTwo} no son multiplos"


numeroUno,numDos = int(input("Dame tu primer numero: ")),int(input("Dame tu segundo número: "))
print(multiplo_num(numeroUno,numDos))