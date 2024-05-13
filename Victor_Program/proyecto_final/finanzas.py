import time

class Finanzas:
    def __init__(self, saldoaInicial=50):
        self.saldo = saldoaInicial
        self.ultimaVez = time.time()

    def recolectarMonedas(self, ahorros):
        self.saldo += ahorros
        print(f"Has recolectado {ahorros} monedas! Saldo actual: {self.saldo}")

    def reducirSaldo(self, costo):
        if self.saldo >= costo:
            self.saldo -= costo
            return True
        return False

    def dineroPorTiempo(self):
        presente = time.time()
        tiempoTranscurrido = presente - self.ultimaVez
        self.ultimaVez = presente  # Actualiza el último tiempo de chequeo
        minutos = tiempoTranscurrido / 60
        monedasPorMinuto = int(minutos) / 10
        monedasPorHora = int(minutos) / 60 * 2  # Ganancia de 2 monedas por hora
        ganancias = int(monedasPorMinuto + monedasPorHora)
        if ganancias > 0:
            self.recolectarMonedas(ganancias)
            print(f"¡Ganaste {ganancias} monedas mientras no estabas!")
        else:
            print("¡Volviste pronto!")
    
    def chequearRecompensaTiempo(self, intervalo=10):
        presente = time.time()
        if presente - self.ultimaVez >= intervalo:
            self.ultimaVez = presente  # Actualiza el último tiempo de recompensa
            self.recolectarMonedas(1)  # Añade monedas cada intervalo
    
    def obtenerSaldo(self):
        return self.saldo
