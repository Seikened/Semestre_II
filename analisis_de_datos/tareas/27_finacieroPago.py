valor_actual_pesos = 20000
tiempo_meses = 5
tasa = 70 / 100
tasa_mensual = tasa / 12

renta = round((valor_actual_pesos * tasa_mensual) / (1 - (1 + tasa_mensual) ** (-tiempo_meses)), 3)

salario_final = valor_actual_pesos

# Encabezados de la tabla
print(f"{'No. Movimiento':<15} | {'Saldo':<10} | {'Interes':<8} | {'Pago':<8} | {'Amortizacion':<13} | {'Saldo Final':<10}")

for i in range(tiempo_meses):
    saldo = salario_final
    interes = saldo * tasa_mensual
    pago = renta
    amortizacion = pago - interes
    salario_final = saldo - amortizacion

    # Asegúrate de que cada valor esté alineado dentro de su columna respectiva
    print(f"{i + 1:<15} | {saldo:<10.2f} | {interes:<8.2f} | {pago:<8.2f} | {amortizacion:<13.2f} | {salario_final:<10.2f}")
