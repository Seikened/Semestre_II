import os
import pygame
from config import Config


def redimensionarSprite(sprite, escala=Config.escala):
    """La escala es un porcentaje de la imagen original. Por ejemplo, si la escala es 50, la imagen se reducirá a la mitad"""
    anchuraOriginal = sprite.get_width()
    alturaOriginal = sprite.get_height()
    anchuraNueva = int(anchuraOriginal * escala / 100)
    return pygame.transform.scale(sprite, (anchuraNueva, int(alturaOriginal * escala / 100)))

class SpriteSheet:
    """Clase para manejar el sprite sheet"""
    def __init__(self,nombreArchivo):
        rutaActual = os.path.dirname(__file__) # Ruta del archivo actual
        rutaCompleta = os.path.join(rutaActual, Config.imgFolder, nombreArchivo) # Ruta completa del archivo
        self.sheet = pygame.image.load(rutaCompleta).convert_alpha() # Cargamos la hoja de sprites
        
    def obtenerSprite(self,x,y,anchura,altura):
        """ Extrae un sprite de las coordenadas x,y con una anchura y altura dadas"""
        sprite = pygame.Surface((anchura,altura),pygame.SRCALPHA)
        sprite.blit(self.sheet,(0,0),(x,y,anchura,altura))
        return sprite



class JardinZenSprites:
    """Clase para gestionar todos los sprites del Jarín Zen"""
    def __init__(self):
            
            self.spritesheet = SpriteSheet(Config.spritesFile)
            self.fondo = SpriteSheet(Config.fondo)

            # Cargar el fondo
            self.fotoFondo = self.fondo.obtenerSprite(0, 0, Config.ventanaAncho, Config.ventanaAlto)

            # Cargar y redimensionar los sprites
            coordenadas = Config.coordenadas
            tamanos = Config.tamanos
            
            # Maceta Café
            macetaCafe = self.spritesheet.obtenerSprite(coordenadas['macetaCafe'][0], coordenadas['macetaCafe'][1], tamanos['macetaCafe'][0], tamanos['macetaCafe'][1])
            self.macetaCafe = redimensionarSprite(macetaCafe)
            
            # Regadera
            regadera = self.spritesheet.obtenerSprite(coordenadas['regadera'][0], coordenadas['regadera'][1], tamanos['regadera'][0], tamanos['regadera'][1])
            self.regadera = redimensionarSprite(regadera)
            
            # Planta fase 1 (por defecto para comenzar)
            plantaFase1 = self.spritesheet.obtenerSprite(coordenadas['plantaFase1'][0], coordenadas['plantaFase1'][1], tamanos['plantaFase1'][0], tamanos['plantaFase1'][1])
            self.plantaFase1 = redimensionarSprite(plantaFase1)
    
    
    
    @staticmethod
    def dibujarSprite(screen,sprite,x,y):
        """Dibuja un sprite en la pantalla en las coordenadas x,y"""
        screen.blit(sprite,(x,y))