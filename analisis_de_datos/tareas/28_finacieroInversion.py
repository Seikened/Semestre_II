ahorro_deseado = 70000
tiempo_meses = 15
tasa = 15 / 100
tasa_mensual = tasa / 12




renta = round(ahorro_deseado/ ((((1+tasa_mensual)**(tiempo_meses)-1)/tasa_mensual)*(1+tasa_mensual)),3)
print(f"La renta mensual es: {renta}")



# Encabezados de la tabla
print(f"{'No. Movimiento':<15} | {'Saldo inicial':<10} | {'Ahorro':<8} | {'Saldo nuevo':<8} | {'Interes':<13} | {'Saldo Final':<10}")
saldo_inicial = 0
salario_final = saldo_inicial
for i in range(tiempo_meses):
    saldo_inicial = salario_final
    ahorro = renta
    saldo_nuevo = saldo_inicial + ahorro
    interes = saldo_nuevo * tasa_mensual
    salario_final = saldo_nuevo + interes


    # Asegúrate de que cada valor esté alineado dentro de su columna respectiva
    print(f"{i + 1:<15} | {saldo_inicial:<13.2f} | {ahorro:<8.2f} | {saldo_nuevo:<11.2f} | {interes:<13.2f} | {salario_final:<10.2f}")


