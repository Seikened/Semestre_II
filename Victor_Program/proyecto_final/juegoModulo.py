# Archivo: juegoModulo.py donde se define la clase Juego.

from sprites import JardinZenSprites
from config import Config


class Juego():
    def __init__(self):
        self.sprites = JardinZenSprites()
    
    
    def Recalcula(self,eventos):
        self.sprites.manejarEventos(eventos)
    
    
    def Dibuja(self,screen):
        self.sprites.dibujarTodos(screen)
