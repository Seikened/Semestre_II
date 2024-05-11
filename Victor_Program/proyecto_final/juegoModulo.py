# Archivo: juegoModulo.py donde se define la clase Juego.

from sprites import JardinZenSprites
from config import Config


class Juego():
    def __init__(self):
        
        # Cargamos los sprites desde el archivo sprites sheet
        self.sprites = JardinZenSprites()
    
    
    def Recalcula(self):
        pass
    
    
    def Dibuja(self,screen):
        posiciones = Config.posiciones
        # Dibuja todos los objetos en la pantalla
        objetos = [
            (self.sprites.fotoFondo, *posiciones['fotoFondo']),
            (self.sprites.macetaCafe, *posiciones['macetaCafe']),
            (self.sprites.regadera, *posiciones['regadera']),
            (self.sprites.plantaFase1, *posiciones['plantaFase1'])
        ]
        for objeto, x, y in objetos:
            JardinZenSprites.dibujarSprite(screen, objeto, x, y)
