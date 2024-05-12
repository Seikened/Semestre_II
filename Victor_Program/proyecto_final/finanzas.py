import time

class Finanzas:
    def __init__(self, saldo_inicial=50):
        self.saldo = saldo_inicial
        self.ultimaVez = time.time()

    def recolectarMonedas(self, ahorros):
        self.saldo += ahorros
        print(f"Has recolectado {ahorros} monedas! Saldo actual: {self.saldo}")

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
    
    def obtenerSaldo(self):
        return self.saldo
