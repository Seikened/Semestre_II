# main.py
import pygame
from juegoModulo import Juego
from config import Config
from tienda import Tienda
from inventario import Inventario
from finanzas import Finanzas

# Constantes para estados
ESTADO_JUEGO = 'juego'
ESTADO_TIENDA = 'tienda'
ESTADO_INVENTARIO = 'inventario'

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((Config.ventanaAncho, Config.ventanaAlto))
tienda = Tienda(screen)
inventario = Inventario(screen)
finanzas = Finanzas()

estadoActual = ESTADO_JUEGO
juego = Juego(screen, finanzas)

salir = False

while not salir:
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            salir = True
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_t:
                if estadoActual != ESTADO_TIENDA:
                    estadoActual = ESTADO_TIENDA
                    tienda.activa = True
                    inventario.activa = False
                else:
                    estadoActual = ESTADO_JUEGO
                    tienda.activa = False
            if evento.key == pygame.K_i:
                if estadoActual != ESTADO_INVENTARIO:
                    estadoActual = ESTADO_INVENTARIO
                    inventario.activa = True
                    tienda.activa = False
                else:
                    estadoActual = ESTADO_JUEGO
                    inventario.activa = False
            if evento.key == pygame.K_ESCAPE:
                salir = True

    screen.fill((0, 0, 0))

    if estadoActual == ESTADO_JUEGO:
        juego.Recalcula(eventos)
        juego.Dibuja()
    elif estadoActual == ESTADO_TIENDA:
        tienda.manejarEventos(eventos)
        tienda.renderizar()
    elif estadoActual == ESTADO_INVENTARIO:
        inventario.manejarEventos(eventos)
        inventario.renderizar()

    pygame.display.flip()
    pygame.time.wait(int(Config.deltaTiempo * 1000))

pygame.quit()
