# Archivo: main.py 

import pygame
from juegoModulo import Juego
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

# Asegúrate de pasar la pantalla al constructor de Juego
juego1 = Juego(screen)

salir = False

while not salir:
    eventos = pygame.event.get()
    for event in eventos:
        if event.type == pygame.QUIT:
            salir = True
    # Entrada por teclado
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        salir = True
    
    # Aquí recalculamos todas laNs variables 
    juego1.Recalcula(eventos)
    
    # Aquí redibujamos todos los objetos.
    screen.fill((0, 0, 0))
    juego1.Dibuja()  # Asegúrate de que el método Dibuja ya no necesita la pantalla como argumento

    # Renderiza el texto y colócalo en la pantalla


    # Actualiza la pantalla
    pygame.display.flip()
    pygame.time.wait(int(deltaTiempo_s * 1000)) # Espera el tiempo necesario para 60 FPS

pygame.display.quit()
print("fin del Juego")
