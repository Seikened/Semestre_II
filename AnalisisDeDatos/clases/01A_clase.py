Num = 5
Num = int(input("Hola ingresa tremendo número: "))

print(Num)

# Si un número es mayor a 10



if Num > 10:
    print(f"{Num} Si es mayor")
else:
    print(f"{Num} no es mayor")
    


match Num:
    case _ if (Num < 10):
        print("Genial")
    case 9:
        print("Hola")
    case 5:
        print("Pesimo")


if  Num > 10:
    if Num < 15:
        print("El valor el valor es mayor a 10 y menor a 15")
    else:
        print("El valor es mayor a 10 pero no menor a 15")
else:
    print("El valor es menor a 10")

# Conjunciones y disyunciones
if (Num > 10) and (Num < 15):
    print("El número esta entre 10 y 15")
else:
    print("El valor esta fuera del rango entre 10 y 15")


NumSemana = int(input("Favor de especificar el npumero de día "))

match NumSemana:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("No estas metniendo un día valido de la semana")

edadBebe = int(input("¿Qué edad tienes? "))

match edadBebe:
    case _ if edadBebe <= 3:
        print("Es un bebé")
    case _ if edadBebe <= 12:
        print("Niño")
    case _ if edadBebe <= 17:
        print("Adolescente")
    case _ if edadBebe <= 30:
        print("Joven")
    case _ if edadBebe <= 45:
        print("Joven Mayor")
    case _ if edadBebe <= 60:
        print("Adulto")
    case _ :
        print("Mayor")
        


#--------------------Reto-------------------------
cantidadBilletes = 1678

# Billetes de 500
cantidadBilletes500 = cantidadBilletes // 500
restante = cantidadBilletes % 500

# Billetes de 200
cantidadBilletes200 = restante // 200
restante = restante % 200

# Billetes de 100
cantidadBilletes100 = restante // 100
restante = restante % 100

# Billetes de 50
cantidadBilletes50 = restante // 50
restante = restante % 50

# Billetes de 20
cantidadBilletes20 = restante // 20
restante = restante % 20

# Monedas de 10
cantidadMoneda10 = restante // 10
restante = restante % 10

# Monedas de 5
cantidadMoneda5 = restante // 5
restante = restante % 5

# Monedas de 1
cantidadMoneda1 = restante // 1

print(f"""
Cantidad de billetes de 500: {cantidadBilletes500}
Cantidad de billetes de 200: {cantidadBilletes200}
Cantidad de billetes de 100: {cantidadBilletes100}
Cantidad de billetes de 50: {cantidadBilletes50}
Cantidad de billetes de 20: {cantidadBilletes20}
Cantidad de monedas de 10: {cantidadMoneda10}
Cantidad de monedas de 5: {cantidadMoneda5}
Cantidad de monedas de 1: {cantidadMoneda1}
""")
