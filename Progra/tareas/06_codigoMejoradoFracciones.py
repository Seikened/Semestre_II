# Modificar el programa de fracciones realizado en clase, agregando las siguientes funciones:
# 1.- Agregue una función llamada Simplifica, que recibe como argumento el numerador y denominador de una fracción, y regresa (return) el numerador y denominador simplificados. Por ejemplo, si una fracción es 18/24, la función debe regresar 3/4.

# 2.- Agregue una función llamada Producto, que recibe como argumento el numerador y denominador de dos fracciones, regresa (return) el resultado de mul􏰀plicar ambas fracciones. El valor de retorno también 􏰀ene que ser en la forma de fracción simplificada: numerador y denominador.

# 3.- Agregue una función llamada División, que recibe como argumento el numerador y denominador de dos fracciones, regresa (return) el resultado de dividir la primera fracción entre la segunda. El valor de retorno también 􏰀ene que ser en la forma de fracción simplificada: numerador y denominador.



class Fraccion:
    def __init__(self,numerador = 1 ,denominador = 1):
        self.numerador = numerador
        self.denominador = denominador
    # SUMA
    def Suma(self, otra_fraccion):
        numerador = (self.numerador * otra_fraccion.denominador) + (otra_fraccion.numerador * self.denominador)
        denominador = self.denominador * otra_fraccion.denominador
        resultadoSuma = Fraccion(numerador,denominador)
        return resultadoSuma.Simplifica()

    # PRODUCTO
    def Producto(self, otra_fraccion):
        numerador = self.numerador * otra_fraccion.numerador
        denominador = self.denominador * otra_fraccion.denominador
        resultadoProducto = Fraccion(numerador,denominador)
        return resultadoProducto.Simplifica()

    # DIVISIÓN
    def Division(self, otra_fraccion):
        numerador = self.numerador * otra_fraccion.denominador
        denominador = self.denominador * otra_fraccion.numerador
        resultadoDivision = Fraccion(numerador,denominador)
        return resultadoDivision.Simplifica()

    # SIMPLIFICAR
    def Simplifica(self):
        mcd = self.Mcd(self.numerador,self.denominador)
        nuevoNumerador = self.numerador// mcd
        nuevoDenominador = self.denominador// mcd
        return Fraccion(nuevoNumerador,nuevoDenominador)

    # MÁXIMO COMÚN DIVISOR
    def Mcd(self,numUno,numDos):
        while numDos != 0:
            numUno,numDos = numDos, numUno%numDos
        return numUno


# --------------------------------------------------------------------------------------------------------------------------------------------

# Código
f1 = Fraccion(1,2)
f2 = Fraccion(21,5)
# Suma
fr =f1.Suma(f2)

print(f"\n La suma de {f1.numerador}/{f1.denominador} + {f2.numerador}/{f2.denominador} es {fr.numerador}/{fr.denominador} \n")
# Producto
fr =f1.Producto(f2)
print(f"\n El producto de {f1.numerador}/{f1.denominador} * {f2.numerador}/{f2.denominador} es {fr.numerador}/{fr.denominador} \n")
# Division
fr =  f1.Division(f2)
print(f"\n La division de {f1.numerador}/{f1.denominador} / {f2.numerador}/{f2.denominador} es {fr.numerador}/{fr.denominador} \n")
