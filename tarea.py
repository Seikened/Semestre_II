userNumber = str(input("Enter a number: "))
listNumber = []
listaValoresBinarios = []
for i in userNumber:
    listNumber.append(int(i))
for e,i in enumerate(listNumber):
    numeroDecimal = i*(2**e)
    listaValoresBinarios.append(numeroDecimal)
    print(numeroDecimal)

sumaTotal = 0
for i in listaValoresBinarios:
    sumaTotal += i

print(f"Este es tu número {sumaTotal}" )

