#Ejercicio No 1. Diseñar una función que calcule la cantidad de segundos en un tiempo dado en horas, minutos y segundos.

def ConversorSegundos(horas,min,seg):
    segundosTotales = ((horas*60)*60)+(min*60)+seg
    return segundosTotales


tiempo = [int(input("Dame tu tiempo en HORAS: ")),int(input("Dame tu tiempo en MINUTOS: ")),int(input("Dame tu tiempo en SEGUNDOS: "))]
segundos = ConversorSegundos(*tiempo)
print(f"Hay {segundos} segundos cuando tienes {tiempo[0]} horas con {tiempo[1]} minutos y con {tiempo[-1]} segundos")