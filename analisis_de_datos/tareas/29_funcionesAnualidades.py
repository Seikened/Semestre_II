import math as mt


# ANUEALIDAD VENCIDA ================================= VALOR FUTURO ===================
#========= 1 VALOR FUTURO ==========

valorFuturo = lambda renta,interes,periodos :  renta * ( ( ( (1+interes)**(periodos) ) - 1 ) / ( interes ) )
#========= 2 RENTA ==========

rentaVencida = lambda interes,periodos,valorFuturo : valorFuturo / ( ( ( (1+interes)**(periodos) ) - 1  ) / ( interes ) )
#========= 3 NÚMERO DE PERIODOS ==========

periodo = lambda interes,valorFuturo, renta : ( mt.log( ( ( valorFuturo * interes ) / ( renta ) ) + 1 ) ) / ( mt.log( 1 + interes ) )


#========= 4 TASA DE INTERÉS ==========
def TasaDeInteresVencidaVF(montoOriginal, renta, periodos):
    interes = 0.001  
    monto = renta * ( ( ( (1+interes)**(periodos) ) - 1 ) / ( interes ) )

    while abs(montoOriginal - monto) >= 0.01:
        interes += 0.0001  
        monto = renta * ( ( ( (1+interes)**(periodos) ) - 1 ) / ( interes ) ) 

    interes = round(interes, 3)  
    print(f"Interés de {interes * 100}%")
    return interes



# ANUALIDAD VENCIDA ================================= VALOR ACTUAL ===================
#========= 5 VALOR ACTUAL ==========
valorActual = lambda renta, interes, periodos : renta * ( ( 1-(1+interes)**(-periodos) ) / interes )

#========= 6 RENTA ==========
rentaAnticipada = lambda interes, periodos, valorActual : (valorActual * interes) / ( 1 - (1 + interes)**(-periodos) )

#========= 7 NÚMERO DE PERIODOS ==========
periodoAnticipada = lambda interes, capital, renta : (mt.log(1 - (capital * interes / renta)) / mt.log(1 + interes))

#========= 8 TASA DE INTERÉS ==========
def TasaDeInteresVencidaVA(montoOriginal, renta, periodos):
    interes = 0.001  
    monto = renta * ( ( 1-(1+interes)**(-periodos) ) / interes )

    while abs(montoOriginal - monto) >= 0.01:
        interes += 0.0001  
        monto = renta * ( ( 1-(1+interes)**(-periodos) ) / interes )

    interes = round(interes, 3)  
    print(f"Interés de {interes * 100}%")
    return interes




# ANUALIDAD ANTIICIPADA ================================= VALOR FUTURO ===================
#========= 9 VALOR FUTURO ==========
valorActualAnticipada = lambda renta, interes, periodos: renta * (1 + (1 - (1 + interes) ** (-periodos + 1)) / interes)

#========= 10 RENTA ==========
rentaAnticipadaFuturo = lambda capitalFuturo, interes, periodos: capitalFuturo * interes / (1 + interes - (1 + interes) ** (-periodos + 1))

#========= 11 NÚMERO DE PERIODOS ==========
periodoAnticipadaFuturo = lambda monto, renta, interes: (mt.log((monto / renta) + 1) * interes + 1) / mt.log(1 + interes) - 1

#========= 12 TASA DE INTERÉS ==========
def TasaDeInteresAnticipadaVF(montoOriginal, renta, periodos):
    interes = 0.001  
    monto = renta * (1 + (1 - (1 + interes) ** (-periodos + 1)) / interes)

    while abs(montoOriginal - monto) >= 0.01:
        interes += 0.0001  
        monto = renta * (1 + (1 - (1 + interes) ** (-periodos + 1)) / interes)

    interes = round(interes, 3)  
    print(f"Interés de {interes * 100}%")
    return interes

# ANUALIDAD ANTIICIPADA ================================= VALOR ACTUAL ===================
#========= 13 VALOR ACTUAL ==========
capitalFuturo = lambda renta, interes, periodos: renta * ((1 + interes) ** (periodos + 1) - 1) / interes - 1

#========= 14 RENTA ==========
rentaAnticipadaActual = lambda montoActual, interes, periodos: montoActual / (((1 + interes) ** (periodos + 1) - 1) / interes)

#========= 15 NÚMERO DE PERIODOS ==========
periodoAnticipadaActual = lambda capital, renta, interes: 1 - (mt.log(1 + interes - (capital / renta) * interes) / mt.log(1 + interes))
#========= 16 TASA DE INTERÉS ==========
def TasaDeInteresAnticipadaVA(montoOriginal, renta, periodos):
    interes = 0.001  
    monto = renta * ((1 + interes) ** (periodos + 1) - 1) / interes - 1

    while abs(montoOriginal - monto) >= 0.01:
        interes += 0.0001  
        monto = renta * ((1 + interes) ** (periodos + 1) - 1) / interes - 1

    interes = round(interes, 3)  
    print(f"Interés de {interes * 100}%")
    return interes