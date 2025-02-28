# CLASES PRIVADAS

class EstadoCuenta:
    
    def __init__(self,nombre,saldoInicial):
        self.__contador = 0
        self.__saldo = saldoInicial
        self.__nombre = nombre
        self.__movimientos = []
        self.__Movimeinto = ("Deposito inicial",saldoInicial)
        
    def Movimeintos(self,descripcion,monto):
        movimiento = (descripcion,monto)
        self.__movimientos.append(movimiento)
        self.__saldo += monto
        
    def __str__(self):
        #Estado de cuenta
        print("-"*30)
        print("Estado de cuenta")
        print(f"Nombre: {self.__nombre}")
        print(f"Saldo: {self.__saldo}")
        print("Movimientos------")
        for movimiento in self.__movimientos:
            print(movimiento)
        print("Fin del estado de cuenta")
        return ""

    def getSaldo(self):
        self.__contador += 1
        return self.__saldo

    def setSaldo(self,saldo):
        self.__saldo = saldo

cuentaFernando = EstadoCuenta("Fernando",1000)
print(cuentaFernando)
#Movimientos
cuentaFernando.Movimeintos("Deposito",1000)
cuentaFernando.Movimeintos("Retiro",-250)
print(cuentaFernando)

# Puedo ver afuera del objeto todos los movimientos y modificarlos
cuentaFernando.__nombre = "GERADRDO"
cuentaFernando.setSaldo(1000000)
print(cuentaFernando)

#print(cuentaFernando.getSaldo())


# #Publico y privado

# class Miclase():
#     def __init__(self):
#         self.propiedadPublica = "Soy publica"
#         self.__propiedadPrivada = "Soy privada"

#     def imprime(self):
#         print(f"Publica: {self.propiedadPublica}")
#         print(f"Privada: {self.__propiedadPrivada}")
        
#     def __privado(self):
#         print("Soy un metodo privado")
        
#     def publico(self):
#         print("Soy un metodo publico")
#         self.__privado()



# clase = Miclase()

# print(clase.propiedadPublica)


# #Intento de modificar la propiedad privada
# clase.propiedadPublica = "Modifico la propiedad publica"
# clase.__propiedadPrivada = "Modifico la propiedad privada"

# clase.imprime()

# clase.publico()

