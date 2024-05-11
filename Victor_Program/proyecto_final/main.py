# Archivo: main.py 

import sys, pygame
from juegoModulo import *
from config import Config

pygame.init()
pygame.font.init()  # Inicializa el módulo de fuentes
font_size = 24
font = pygame.font.Font(None, font_size)  # None para usar la fuente predeterminada
text_color = (255, 255, 255)

# Creamos la ventana de juego
tamano = (Config.ventanaAncho, Config.ventanaAlto)
deltaTiempo_s = Config.deltaTiempo
screen = pygame.display.set_mode(tamano)
juego1 = Juego()

salir = False

while not salir:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir = True
    # Entrada por teclado
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        salir = True
    
    # Aquí recalculamos todas las variables 
    juego1.Recalcula()
    
    # Aquí redibujamos todos los objetos.
    screen.fill((0, 0, 0))
    juego1.Dibuja(screen)

    # Renderiza el texto y colócalo en la pantalla


    # Actualiza la pantalla
    pygame.display.flip()
    pygame.time.wait(int(deltaTiempo_s * 1000))

pygame.display.quit()
print("fin del Juego")