# juegoModulo.py
from sprites import JardinZenSprites
import pygame

class Juego():
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.sprites = JardinZenSprites(self.pantalla)
    
    def Recalcula(self, eventos):
        self.sprites.manejarEventos(eventos)
    
    def Dibuja(self):
        self.sprites.dibujarTodos()  # Ya no se pasa self.pantalla aquí
