import time
import pygame

class Finanzas:
    def __init__(self, saldoaInicial=50):
        self.saldo = saldoaInicial
        self.ultimaVez = time.time()
        self.fuente = pygame.font.Font(None, 24)  # Define la fuente aquí

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
    
    def renderizarSaldo(self, pantalla):
            textoSaldo = f"Saldo Actual: {int(self.saldo)} monedas"
            superficieTexto = self.fuente.render(textoSaldo, True, (255, 255, 255))
            pantalla.blit(superficieTexto, (10, 10))
    
    def guardar(self):
        # Guarda el saldo actual y la última vez que se modificó
        return {'saldo': self.saldo, 'ultimaVez': self.ultimaVez}

    def cargar(self, data):
        # Carga el saldo y la última vez que se modificó
        self.saldo = data['saldo']
        self.ultimaVez = data['ultimaVez']