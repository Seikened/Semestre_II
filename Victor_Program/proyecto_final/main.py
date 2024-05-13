# main.py
import pygame
import os
from juegoModulo import Juego
from config import Config
from tienda import Tienda
from inventario import Inventario
from finanzas import Finanzas
from sesion import Sesion

# Constantes para estados
ESTADO_JUEGO = 'juego'
ESTADO_TIENDA = 'tienda'
ESTADO_INVENTARIO = 'inventario'

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((Config.ventanaAncho, Config.ventanaAlto))
finanzas = Finanzas()
juego = Juego(screen, finanzas)
huerto = juego.jardin.huerto
inventario = Inventario(screen,finanzas, huerto)
tienda = Tienda(screen,finanzas,inventario)


estadoActual = ESTADO_JUEGO

salir = False

# Cargar y reproducir música de fondo
os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.mixer.music.load("ZELDA.mp3")
pygame.mixer.music.play(loops=-1)

sesion = Sesion(finanzas, huerto, inventario)
sesion.cargarSesion()

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
                sesion.guardarSesion()
                salir = True

    screen.fill((0, 0, 0))

    if estadoActual == ESTADO_JUEGO:
        juego.Recalcula(eventos)
        juego.Dibuja()
        finanzas.chequearRecompensaTiempo()
    elif estadoActual == ESTADO_TIENDA:
        tienda.manejarEventos(eventos)
        tienda.renderizar()
    elif estadoActual == ESTADO_INVENTARIO:
        inventario.manejarEventos(eventos)
        inventario.renderizar()
    
    
    finanzas.renderizarSaldo(screen)

    pygame.display.flip()
    pygame.time.wait(int(Config.deltaTiempo * 1000))

pygame.quit()
