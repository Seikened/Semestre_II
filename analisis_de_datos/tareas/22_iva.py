#Ejercicio No 3. Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA

iva = lambda subTotal: subTotal*1.16

subTotalVenta = int(input("Dame el subtotal de tu venta: "))

total_con_iva = iva(subTotalVenta)
print(f"El total ya con iva es {total_con_iva}")