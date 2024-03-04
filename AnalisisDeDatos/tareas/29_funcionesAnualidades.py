import math as mt


# ANUEALIDAD VENCIDA
#========= 1 VALOR FUTURO ==========
valorFuturo = lambda renta,interes,periodos :  renta * ( ( ( (1+interes)**(periodos) ) - 1 ) / ( interes ) )
#========= 2 RENTA ==========
renta = lambda interes,periodos,valorFuturo : valorFuturo / ( ( ( (1+interes)**(periodos) ) - 1  ) / ( interes ) )
#========= NÚMERO DE PERIODOS ==========
periodo = lambda interes,valorFuturo, renta : ( mt.log( ( ( valorFuturo * interes ) / ( renta ) ) + 1 ) ) / ( mt.log( 1 + interes ) )
#========= TASA DE INTERÉS ==========
def interes(renta, periodos, valorFut, interes_inicial=0.01):
    interes = interes_inicial
    valorFut_calculado = valorFuturo(renta, interes, periodos)
    tolerancia = 0.01
    max_iteraciones = 100000
    iteracion = 0

    while abs(valorFut_calculado - valorFut) > tolerancia and iteracion < max_iteraciones:
        interes += 0.001  # Ajustas el interés en cada iteración
        valorFut_calculado = valorFuturo(renta, interes, periodos)  # Recalculas el valor futuro con el nuevo interés
        iteracion += 1
        print(f"Iteración {iteracion}: Tasa de interés = {interes:.3f}, Valor Futuro Calculado = {valorFut_calculado:.2f}")

    if iteracion == max_iteraciones:
        print("No se encontró una solución en el número máximo de iteraciones.")
    else:
        print(f"Solución encontrada: Tasa de interés = {interes:.3f}, Valor Futuro = {valorFut_calculado:.2f}")

    return interes

# Testing the 'interes' function
renta_value = 13000
periodos_value = 5
valorFuturo_value = 3000
interes_value = 0.1


result = interes(renta_value, periodos_value, valorFuturo_value, interes_value)
print(result)

# ANUALIDAD ANTICIPADA
