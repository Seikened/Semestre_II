
multiplicador  = int(input("Ingresa el numero a multiplicar: "))
rango_inicial = int(input("Desde donde quieres que comience: "))
rango_final = int(input("Hasta donde quieres que termine: "))
for i in range(rango_inicial,rango_final+1):
    print(f"{multiplicador} x {i} = {multiplicador*i}")
    pass