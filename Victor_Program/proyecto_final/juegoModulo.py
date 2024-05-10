from sprites import JardinZenSprites


class Juego():
    def __init__(self):
        
        # Cargamos los sprites desde el archivo sprites sheet
        self.sprites = JardinZenSprites()
    
    
    def Recalcula(self):
        pass
    
    
    def Dibuja(self,screen):
        # Dibuja todos los objetos en la pantalla
        objetos = [
            (self.sprites.fotoFondo, 0, 0),
            (self.sprites.macetaNegra, 300, 100),
            (self.sprites.macetaCafe, 100, 100),
            (self.sprites.regadera, 500, 100),
            (self.sprites.plantaFase1, 200, 300),
            (self.sprites.plantaFase2, 400, 300),
            (self.sprites.plantaFase3, 600, 300)
        ]

        for objeto, x, y in objetos:
            JardinZenSprites.DibujarSprite(screen, objeto, x, y)