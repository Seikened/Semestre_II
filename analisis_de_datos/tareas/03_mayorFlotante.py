

def MayorMenor(listaNumeros):
    
    numeroMayor = -9999999
    numeroMenor = 9999999
    for i in listaNumeros:
        if i >= numeroMayor:
            numeroMayor = i
        if i <= numeroMenor:
            numeroMenor = i
    return print(f"""
El número mayor es {numeroMayor}
El número menor es {numeroMenor}""")

eleccionUser = int(input("¿Cuántos números desea ingresar? "))
listaNumeros = []
for i in range(eleccionUser):
    numeroFlotante = float(input(f"Introduce tu número {i+1}: "))
    listaNumeros.append(numeroFlotante)

MayorMenor(listaNumeros)