# CLASES PRIVADAS

class MiBanco:
    def __init__(self):
        self.__cuentas = []
        
    def agregaCuenta(self,cuenta):
        if not isinstance(cuenta, EstadoCuenta):
            raise ValueError("El argumento debe ser de tipo EstadoCuenta")
        self.__cuentas.append(cuenta)
        return len(self.__cuentas)-1
    
    
    def imprimirCuenta(self,posicionCuenta):
        return f"Estado de cuenta {self.__cuentas[posicionCuenta]}"
    
    
    def movimeinto(self,numeroCuenta,descripcion,monto):
        cuenta = self.__cuentas[numeroCuenta]
        saldoCuenta = cuenta.getSaldo()
        resta = saldoCuenta + monto
        
        if (resta < 0):
            raise ValueError("No se puede hacer esta operación")
        cuenta.movimiento(descripcion.upper(),monto)



class EstadoCuenta:
    
    def __init__(self, nombre, saldoInicial):
        self.__contador = 0
        self.__saldo = saldoInicial
        self.__nombre = nombre
        self.__movimientos = []
        self.__movimiento = ("Deposito inicial", saldoInicial)
        
    def movimiento(self, descripcion, monto):
        movimiento = (descripcion, monto)
        self.__movimientos.append(movimiento)
        self.__saldo += monto
        
    def __str__(self):
        # Estado de cuenta
        print("🟦"*17)
        print("Estado de cuenta")
        print(f"Nombre: {self.__nombre}")
        print(f"Saldo: {self.__saldo}")
        print("Movimientos" + "🔹"*7)
        for movimiento in self.__movimientos:
            print(movimiento)
        print("🔹"*14)
        print("Fin del estado de cuenta")
        return ""

    def getSaldo(self):
        self.__contador += 1
        return self.__saldo



cuentaFernando = EstadoCuenta('Fernando Leon Franco',1500)
cuentaMayra = EstadoCuenta('Mayra Janeth Rodrigez Tinajero',4000)

# Agregar cuentas al banco
banco = MiBanco()

numeroDeCuentaFernando = banco.agregaCuenta(cuentaFernando)
numeroDeCuentaMayra = banco.agregaCuenta(cuentaMayra)
banco.movimeinto(numeroDeCuentaFernando,'PaGo de Terreno',-1500)

banco.imprimirCuenta(numeroDeCuentaFernando)