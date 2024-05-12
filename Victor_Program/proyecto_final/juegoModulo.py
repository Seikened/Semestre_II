# juegoModulo.py
from sprites import JardinZenSprites
import pygame

class Juego():
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.sprites = JardinZenSprites(self.pantalla)
    
    def Recalcula(self, eventos):
        # Actualiza el manejo de eventos de todos los sprites
        self.sprites.manejarEventos(eventos)
    
    def Dibuja(self):
        # Dibuja todos los elementos gráficos del juego
        self.sprites.dibujarTodos()
