# Programa que pida las ventas realizadas y calcule la comisión. Si la venta es superior a $10,000 que otorgue una comisión del 12% 
# de lo contrario que solo otorgue el 4%


ventasUsuario = float(input("Ingresa tus ventas: "))
com = 0
if ventasUsuario > 10000:
    com = ventasUsuario * (.12)
else:
    com = ventasUsuario * (.04)
print(f"Tu comisión de tu venta de {ventasUsuario} es: {com}")