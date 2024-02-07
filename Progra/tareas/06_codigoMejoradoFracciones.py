# Modificar el programa de fracciones realizado en clase, agregando las siguientes funciones:
# 1.- Agregue una función llamada Simplifica, que recibe como argumento el numerador y denominador de una fracción, y regresa (return) el numerador y denominador simplificados. Por ejemplo, si una fracción es 18/24, la función debe regresar 3/4.

# 2.- Agregue una función llamada Producto, que recibe como argumento el numerador y denominador de dos fracciones, regresa (return) el resultado de mul􏰀plicar ambas fracciones. El valor de retorno también 􏰀ene que ser en la forma de fracción simplificada: numerador y denominador.

# 3.- Agregue una función llamada División, que recibe como argumento el numerador y denominador de dos fracciones, regresa (return) el resultado de dividir la primera fracción entre la segunda. El valor de retorno también 􏰀ene que ser en la forma de fracción simplificada: numerador y denominador.



class Fraccion:
    def __init__(self,numerador = 1 ,denominador = 1):
        self.numerador = numerador
        self.denominador = denominador
        
    
    



# Operaciones de Fracciones 

# FUNCIONES
# --------------------------------------------------------------------------------------------------------------------------------------------
def Suma(fraccionUno, fraccionDos):
    numerador = (fraccionUno.numerador * fraccionDos.denominador) + (fraccionDos.numerador * fraccionUno.denominador)
    denominador = fraccionUno.denominador * fraccionDos.denominador
    resultadoSuma = Fraccion(numerador,denominador)
    return Simplifica(resultadoSuma)

def Producto(fraccionUno, fraccionDos):
    numerador = fraccionUno.numerador * fraccionDos.numerador
    denominador = fraccionUno.denominador * fraccionDos.denominador
    resultadoProducto = Fraccion(numerador,denominador)
    return Simplifica(resultadoProducto)

def Division(fraccionUno, fraccionDos):
    numerador = fraccionUno.numerador * fraccionDos.denominador
    denominador = fraccionUno.denominador * fraccionDos.numerador
    resultadoDivision = Fraccion(numerador,denominador)
    return Simplifica(resultadoDivision)


def Simplifica(resultadoFraccion):
    nuevoNumerador = resultadoFraccion.numerador
    nuevoDenominador =  resultadoFraccion.denominador
    i = 2
    while True:
        if (nuevoNumerador%i == 0 ) and (nuevoDenominador%i == 0):
            nuevoNumerador = nuevoNumerador//i
            nuevoDenominador = nuevoDenominador//i
        else:
            break
        i += 1
    return Fraccion(nuevoNumerador,nuevoDenominador)

def Mcd(numUno,numDos):
    while numDos != 0:
        numUno,numDos = numDos, numUno%numDos
    return numUno
# --------------------------------------------------------------------------------------------------------------------------------------------

# Código
f1 = Fraccion(1,2)
f2 = Fraccion(21,5)
# Suma
fr = Suma(f1,f2)
print(f"\n La suma de {f1.numerador}/{f1.denominador} + {f2.numerador}/{f2.denominador} es {fr.numerador}/{fr.denominador} \n")
# Producto
fr = Producto(f1,f2)
print(f"\n El producto de {f1.numerador}/{f1.denominador} * {f2.numerador}/{f2.denominador} es {fr.numerador}/{fr.denominador} \n")
# Division
fr = Division(f1,f2)
print(f"\n La division de {f1.numerador}/{f1.denominador} / {f2.numerador}/{f2.denominador} es {fr.numerador}/{fr.denominador} \n")