# juegoModulo.py
from sprites import JardinZenSprites
import pygame

class Juego():
    def __init__(self, pantalla,finanzas):
        self.pantalla = pantalla
        self.finanzas = finanzas
        self.sprites = JardinZenSprites(self.pantalla, self.finanzas)
    
    def Recalcula(self, eventos):
        # Actualiza el manejo de eventos de todos los sprites
        self.sprites.manejarEventos(eventos)
    
    def Dibuja(self):
        # Dibuja todos los elementos gráficos del juego
        self.sprites.dibujarTodos()
