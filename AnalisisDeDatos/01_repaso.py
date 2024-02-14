# 1) Solicitar un valor en pesos y presentarlo en dolares y euros
def EurosDolares(pesos):
    pesos_a_euros = pesos*(.054)
    pesos_a_dolares = pesos*(.059)
    return pesos_a_dolares,pesos_a_euros
# 2) Pedir un importe y presentar el iva y el total general (Monto mas iva)
Iva = lambda subTotal:subTotal*1.16

# 3) Pedir un valor en segundos, y presentarlo en Horas:Minutos:Segundos  4000 s-->01:06:40 
def FormateadorHoras(segundos):
    segundos_restantes=0
    horas= segundos//3600
    segundos_restantes = segundos%3600
    minutos = segundos_restantes//60
    segundos_restantes = segundos_restantes%60
    return f"{horas}:{minutos}:{segundos_restantes}:"

# 4) [IF] Pedir 3 numeros y mostrarlos en forma ordenada descendente-----------------------------------------------
def OrdenadoDesendentre(listaNumeros):
    for i in range(len(listaNumeros)-1):
        for num in listaNumeros:
            if num < listaNumeros[i+1]:
                listaNumeros[i],listaNumeros[i+1] = listaNumeros[i+1],listaNumeros[i]
    return listaNumeros


# 5) [FUNCIONES TEXTO] Solicitar una frase de 3 palabras y mostrar las palabras separadas---------------------------------------------------------
def Frase(frase):
    listaPalabras = []
    palabra = ""
    for i,caracter in enumerate(frase):
        if caracter == " ":
            palabra = frase[0:i]
            listaPalabras.append(palabra)
    return listaPalabras


# 6) Calcular la hipotenusa (pidiendo ambos lados:opuesto y adyacente)
def Hipotenusa(ca,co):
    return ((ca**2)+(co**2))^(1/2)


# 7) [IF] Solicitar un numero e indicar si es impar
def Impar(numero):
    if numero%2==0:
        return f"Par"
    else:
        return f"Impar"


# 8) [ELIF] Pedir una calificacion (5 al 10), e indicar la leyenda:10-excelente, 9-muy bien, 8-Bien, 7-Regular, 6-Mal, 5-Reprobado
def CalculadorCalificaciones(calificacion):
    match calificacion:
        case 10:
            return "excelente"
        case 9:
            return "muy bien"
        case 8:
            return "bien"
        case 7:
            return "Regular"
        case 6:
            return "Mal"
        case 5:
            return "Reprobado"
        case _:
            return "Fuera del rango"



# 9) [FOR] Pedir 5 numeros, y presentar la suma, el conteo y el promedio

def NumerosSumados(listaNumeros):
    conteo = 0
    suma = 0
    for num in listaNumeros:
        suma += num
        conteo +=1
    promedio = suma/conteo
    return f"Suma: {suma} ,Conteo: {conteo}, Promedio: {promedio}"


# 10) [FOR] Pedir un numero e indicar si es un numero primo
def IfNumeroPrimo(numero):
    if numero < 2:
        primo="No es primo"
    else:
        raiz= int(numero**(0.5))+1
        primo=True
        for num in range(2,raiz):
            if numero%num == 0:
                primo=False
                break
        if primo:
            return f"Tu número {numero} es primo"
        else:
            return f"Tu número {numero} No es primo"



# 11) [FOR] Escribe un programa que indique cuantos años pares existen entre 1950 y 2010
def ContadorYearImpars(yearOne,yearTwo):
    quantityYear = abs(yearOne-yearTwo)+1
    listYearsImpars = []
    for year in range(0,quantityYear):
        if year%2!=0:
            listYearsImpars.append(year)
    return len(listYearsImpars)

# 12) Escribir un numero de 5 dígitos e indicar si se trata de una capicua
def Capicua(numero):
    #19,215
    primerNumero = numero // 10000
    resNum = numero%10000
    segundoNumero = resNum//1000
    resNum = resNum%1000
    tercerNumero = resNum//100
    resNum = resNum%100
    cuartoNumero = resNum//10
    resNum = resNum%10
    quintoNumero = resNum

    if (primerNumero==quintoNumero) and (segundoNumero==cuartoNumero):
        return f"{numero} ES UNA CAPICUA"
    else:
        return f"{numero} NO ES UNA CAPICUA"


# 13) [FOR] Del listado (10,111,13,15,45,63,25,96) indicar cuantos numeros son impares
def Impareslistado(listaNumeros):
    impares = 0
    for num in listaNumeros:
        if num%2 !=0:
            impares+=1
    return impares


#lista = [10, 111, 13, 15, 45, 63, 25, 96]

#print(f"La cantidad de impares son: {Impareslistado(lista)}")



# 14) [FOR] Preguntar primero cuantos números, posterior solicitar cada uno de esos numeros y mostrar la sumatoria
def Sumatoria(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma

#tamanoLista = int(input("Ingresa el tamaño de tu lista: "))
#listaNumeros = []
#for i in range(tamanoLista):
#    listaNumeros.append(int(input(f"Ingresa valor {i+1} para sumarlo después: ")))
#print(Sumatoria(listaNumeros))



# 15) [FOR] Programa que pida 4 calificaciones (0-10), posteriormente calcular el promedio e indicar su clasificacion: 
# 0.0-5.9: E
# 6.0-6.9: D
# 7.0-7.9: C
# 8.0-8.9: B
# 9.0-10: A

def CalculadorCalificacionesLetra(calif):
    
    if 10>=calif>=9:
        return "A"
    elif 8.9>=calif>=8:
        return "B"
    elif 7.9>=calif>=7:
        return "C"
    elif 6.9>=calif>=6:
        return "D"
    elif 5.9>=calif>=0:
        return "E"

# cantidadCalificaciones = int(input("Cuantas calificaiones vas a meter? "))
# listaCalificaciones = []
# for i in range(cantidadCalificaciones):
#     listaCalificaciones.append(float(input(f"Ingresa tu calificación {i+1} de {cantidadCalificaciones}=> ")))
# for calif in listaCalificaciones:
#     print(CalculadorCalificacionesLetra(calif))
    



# Adicionales
# 16) Escribe un programa que dado un monto, indique los billetes a entregar: Denominaciones: 500, 200, 100, 50, 20, 10, 5, 1
def Cajero(monto):
    # 1516
    listaDenominaciones = [500,200, 100, 50, 20, 10, 5, 1]
    listaBilles = []
    for denominacion in listaDenominaciones:
        cantidadDenominacion = monto//denominacion
        monto -= cantidadDenominacion*denominacion
        listaBilles.append(cantidadDenominacion)
    return listaBilles


# 17) Escribe un programa que pida un valor y calcule y muestre su factorial
def Factorial(numero):
    sumatoria = 1
    for num in range(1,numero+1):
        sumatoria *= num
    return sumatoria



# 18) Escribe un programa que pida 3 valores e indique cuando son iguales

# valor1 = input("Ingresa el primer valor: ")
# valor2 = input("Ingresa el segundo valor: ")
# valor3 = input("Ingresa el tercer valor: ")

# if (valor1 == valor2) and (valor2 == valor3):
#     print("Todos los valores son iguales.")
# else:
#     print("No todos los valores son iguales.")


# 19) Escribe un programa que pida un valor en Metros, y muestre su equivalencia en Pies y en Yardas
def ConversorMedidas(metros):
    pies = metros * 3.28084
    yardas =  metros*1.09361
    return f"{metros} metros son {pies} pies y son {yardas} yardas."


# 20) Escribe un programa que pida un número y diga si es multiplo de 5

# numero = int(input("Dame un número: "))
# if numero%5 ==0:
#     print("Es multiplo de 5")
# else:
#     print("No es multiplo de 5")
    

# ESTRUCTURAS REPETITIVAS
listaEstructuras = [8,14,22,3,7,28,36,49,52]
# 21) Usando FOR y WHILE. De la siguiente lista [8,14,22,3,7,28,36,49,52], indicar cuantos números son pares
### FOR---------
pares = 0
for num in listaEstructuras:
    if num%2==0:
        pares +=1
print(f"Total de pares {pares}")

### WHILE-------
pares = 0
c = 0
while c < len(listaEstructuras):
    if listaEstructuras[c]%2==0:
        pares +=1
    c+=1
print(f"Total de pares {pares}")



# 22) Usando FOR y WHILE. De la siguiente lista [8,14,22,3,7,28,36,49,52], indicar cuantos números están por encima de 15
### FOR---------
encima = 0
for num in listaEstructuras:
    if num>15:
        encima +=1
print(f"Total de números encima de 15: {encima}")

### WHILE-------
encima = 0
c = 0
while c < len(listaEstructuras):
    if listaEstructuras[c]>15:
        encima +=1
    c+=1
print(f"Total de números encima de 15: {encima}")



# 23) Usando FOR y WHILE. De la siguiente lista [8,14,22,3,7,28,36,49,52], indicar la cantidad de valores, la sumatoria y su promedio
### FOR---------
sumatoria = 0
cantidad = len(listaEstructuras)
for num in listaEstructuras:
    sumatoria +=num

promedio = sumatoria/cantidad

print(f"Promedio: {promedio}, Sumatoria:{sumatoria}, Total de elementos: {cantidad}")

### WHILE-------
sumatoria = 0
c = 0
while c < len(listaEstructuras):
    sumatoria += listaEstructuras[c]
    c+=1
promedio = sumatoria/c
print(f"Promedio: {promedio}, Sumatoria:{sumatoria}, Total de elementos: {c}")



# 24) Usando FOR y WHILE. Del ejercicio anterior, calcular el La Varianza y Desviación Estándar Poblacional
### FOR---------
sumatoria = 0
cantidad = len(listaEstructuras)
for num in listaEstructuras:
    sumatoria +=num


promedio = sumatoria/cantidad
diferencia = 0
for num in listaEstructuras:
    diferencia += (num-promedio)**2

desviacion = (diferencia/cantidad)**(1/2)
varianza = desviacion**2
print(f"Promedio: {promedio}, Sumatoria:{sumatoria}, Total de elementos: {cantidad}, Desviación estándar:{desviacion}, Varianza:{varianza}")

### WHILE-------
sumatoria = 0
c = 0
while c < len(listaEstructuras):
    sumatoria += listaEstructuras[c]
    c+=1

promedio = sumatoria/c
diferencia = 0
c = 0
while c<len(listaEstructuras):
    diferencia += (listaEstructuras[c]-promedio)**2
    c+=1
    
desviacion = (diferencia/cantidad)**(1/2)
varianza = desviacion**2

print(f"Promedio: {promedio}, Sumatoria:{sumatoria}, Total de elementos: {c}, Desviación estándar:{desviacion}, Varianza:{varianza}")



# 25) Usando FOR y WHILE. Realiza un programa que pida 2 números enteros, e imprima los números impares que existen entre los 2 valores

numeroUno = 5
numeroDos = 30

### FOR ----------
for num in range(numeroUno,numeroDos+1):
    if num%2 !=0:
        print(f"Numero impar => {num}")
### WHILE --------
c= numeroUno
while c<= numeroDos:
    if c%2 !=0:
        print(f"Numero impar while => {c}")
    c+=1