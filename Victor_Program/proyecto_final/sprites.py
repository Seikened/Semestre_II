import os
import pygame
from config import Config

class SpriteSheet:
    """Clase para manejar el sprite sheet"""
    def __init__(self,nombreArchivo):
        rutaActual = os.path.dirname(__file__) # Ruta del archivo actual
        rutaCompleta = os.path.join(rutaActual, Config.imgFolder, nombreArchivo) # Ruta completa del archivo
        self.sheet = pygame.image.load(rutaCompleta).convert_alpha() # Cargamos la hoja de sprites
        
    def ObtenerSprites(self,x,y,anchura,altura):
        """ Extrae un sprite de las coordenadas x,y con una anchura y altura dadas"""
        sprite = pygame.Surface((anchura,altura),pygame.SRCALPHA)
        sprite.blit(self.sheet,(0,0),(x,y,anchura,altura))
        return sprite



class JardinZenSprites:
    """Clase para gestionar todos los sprites del Jarín Zen"""
    def __init__(self):
        self.spritesheet = SpriteSheet(Config.spritesFile)
        self.fondo = SpriteSheet(Config.fondo)
        
        # Cargamos el fondo
        self.fotoFondo = self.fondo.ObtenerSprites(0,0,Config.ventanaAncho,Config.ventanaAlto)
        # Cargamos los sprites
        self.macetaCafe = self.spritesheet.ObtenerSprites(50, 348, 197, 176)
        self.macetaNegra = self.spritesheet.ObtenerSprites(50, 553, 197, 177)
        self.regadera = self.spritesheet.ObtenerSprites(1445, 388, 404, 249)
        self.plantaFase3 = self.spritesheet.ObtenerSprites(9, 759, 289, 125)
        self.plantaFase2 = self.spritesheet.ObtenerSprites(9, 892, 289, 115)
        self.plantaFase1 = self.spritesheet.ObtenerSprites(50, 1016, 217, 94)
        
    @staticmethod
    def DibujarSprite(screen,sprite,x,y):
        """Dibuja un sprite en la pantalla en las coordenadas x,y"""
        screen.blit(sprite,(x,y))