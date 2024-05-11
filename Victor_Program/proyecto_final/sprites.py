import os
import pygame
from config import Config


def redimensionarSprite(sprite, escala):
    """ Redimensiona un sprite según la escala dada """
    anchura, altura = sprite.get_size()
    nuevaAnchura = int(anchura * escala / 100)
    nuevaAltura = int(altura * escala / 100)
    return pygame.transform.scale(sprite, (nuevaAnchura, nuevaAltura))




class SpriteSheet:
    def __init__(self, nombreArchivo):
        """Clase para manejar el sprite sheet"""
        rutaCompleta = os.path.join(os.path.dirname(__file__), Config.imgFolder, nombreArchivo)
        self.sheet = pygame.image.load(rutaCompleta).convert_alpha()
        
    def obtenerSprite(self, x, y, ancho, alto):
        """ Extrae un sprite de las coordenadas x, y con una anchura y altura dadas"""
        sprite = pygame.Surface((ancho, alto), pygame.SRCALPHA)
        sprite.blit(self.sheet, (0, 0), (x, y, ancho, alto))
        return sprite


class SpriteArrastrable:
    def __init__(self, sprite, posicion):
        self.sprite = sprite
        self.posicion = posicion
        self.estaArrastrando = False
        self.desplazamientoX = 0
        self.desplazamientoY = 0

    def ManejarEventoArrastrable(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN and self.sprite.get_rect(topleft=self.posicion).collidepoint(evento.pos):
            self.estaArrastrando = True
            self.desplazamientoX = self.posicion[0] - evento.pos[0]
            self.desplazamientoY = self.posicion[1] - evento.pos[1]
        elif evento.type == pygame.MOUSEBUTTONUP:
            self.estaArrastrando = False
        elif evento.type == pygame.MOUSEMOTION and self.estaArrastrando:
            self.posicion = (evento.pos[0] + self.desplazamientoX, evento.pos[1] + self.desplazamientoY)

    def Dibujar(self, pantalla):
        pantalla.blit(self.sprite, self.posicion)

class Fondo:
    def __init__(self):
        x,y,ancho,alto = Config.coordenadas['fondo']
        sprite = SpriteSheet(Config.fondo).obtenerSprite(x, y, ancho, alto)
        self.sprite = redimensionarSprite(sprite,100)
        self.posicion = (0,0)
    
    def Dibujar(self, pantalla):
        pantalla.blit(self.sprite, self.posicion)


class Maceta(SpriteArrastrable):
    
    numeroMacetas = 0
    
    def __init__(self,nombreSprite= 'macetaCafe'):
        x,y,x2,y2 = Config.coordenadas[nombreSprite]
        anchura, altura = Config.tamanos[nombreSprite]
        sprite = SpriteSheet(Config.spritesFile).obtenerSprite(x, y, anchura, altura)
        posicion = Config.posiciones[nombreSprite]
        super().__init__(redimensionarSprite(sprite,Config.escala), posicion)
        self.contienePlanta = False
        self.tipoMaceta = 'cafe'
        self.idMaceta = Maceta.numeroMacetas
        Maceta.numeroMacetas += 1
        
        # Para depuración
        print(f"coordenadas: x1:{x}, y1:{y}, x2:{x2}, y2:{y2}")
        print(f"nombreSprite: {nombreSprite}")
        print(f"Possicion: {Config.posiciones[nombreSprite]}")
        print(f"numeroMacetas: {Maceta.numeroMacetas}")
        print(f"escala: {Config.escala}")
        print(f"Tamaño de la imagen: {Config.tamanos[nombreSprite]}")
        
    def cambiarMacetaNegra(self):
        x,y,x2,y2 = Config.coordenadas['macetaNegra']
        anchura, altura = Config.tamanos['macetaNegra']
        sprite = SpriteSheet(Config.spritesFile).obtenerSprite(x, y, anchura, altura)
        self.sprite = redimensionarSprite(sprite,Config.escala)
        self.tipoMaceta = 'negra'
        
        # Para depuración
        print(f"coordenadas: x1:{x}, y1:{y}, x2:{x2}, y2:{y2}")
        print(f"nombreSprite: macetaNegra")
        print(f"Possicion: {Config.posiciones['macetaNegra']}")
        print(f"numeroMacetas: {Maceta.numeroMacetas}")
        print(f"escala: {Config.escala}")
        print(f"Tamaño de la imagen: {Config.tamanos['macetaNegra']}")

    def Dibujar(self, pantalla):
        return super().Dibujar(pantalla)


class Planta(SpriteArrastrable):
    
    numeroPlantas = 0
    
    def __init__(self,nombreSprite= 'plantaFase1'):
        x,y,x2,y2 = Config.coordenadas[nombreSprite]
        anchura, altura = Config.tamanos[nombreSprite]
        sprite = SpriteSheet(Config.spritesFile).obtenerSprite(x, y, anchura, altura)
        posicion = Config.posiciones[nombreSprite]
        super().__init__(redimensionarSprite(sprite,Config.escala), posicion)
        self.nombreSprite = nombreSprite
        self.enMaceta = False
        self.idPlanta = Planta.numeroPlantas
        Planta.numeroPlantas += 1
        
        # Para depuración
        print(f"coordenadas: x1:{x}, y1:{y}, x2:{x2}, y2:{y2}")
        print(f"nombreSprite: {nombreSprite}")
        print(f"Possicion: {Config.posiciones[nombreSprite]}")
        print(f"numeroPlantas: {Planta.numeroPlantas}")
        print(f"escala: {Config.escala}")
        print(f"Tamaño de la imagen: {Config.tamanos[nombreSprite]}")

    def faseDosCrecimiento(self):
        x,y,x2,y2 = Config.coordenadas['plantaFase2']
        anchura, altura = Config.tamanos['plantaFase2']
        sprite = SpriteSheet(Config.spritesFile).obtenerSprite(x, y, anchura, altura)
        self.sprite = redimensionarSprite(sprite,Config.escala)
        self.nombreSprite = 'plantaFase2'
        
        # Para depuración
        print(f"coordenadas: x1:{x}, y1:{y}, x2:{x2}, y2:{y2}")
        print(f"nombreSprite: plantaFase2")
        print(f"Possicion: {Config.posiciones['plantaFase2']}")
        print(f"numeroPlantas: {Planta.numeroPlantas}")
        print(f"escala: {Config.escala}")
        print(f"Tamaño de la imagen: {Config.tamanos['plantaFase2']}")
        
    
    
    def faseTresCrecimiento(self):
        x,y,x2,y2 = Config.coordenadas['plantaFase3']
        anchura, altura = Config.tamanos['plantaFase3']
        sprite = SpriteSheet(Config.spritesFile).obtenerSprite(x, y, anchura, altura)
        self.sprite = redimensionarSprite(sprite,Config.escala)
        self.nombreSprite = 'plantaFase3'
        
        # Para depuración
        print(f"coordenadas: x1:{x}, y1:{y}, x2:{x2}, y2:{y2}")
        print(f"nombreSprite: plantaFase3")
        print(f"Possicion: {Config.posiciones['plantaFase3']}")
        print(f"numeroPlantas: {Planta.numeroPlantas}")
        print(f"escala: {Config.escala}")
        print(f"Tamaño de la imagen: {Config.tamanos['plantaFase3']}")
    
    def Dibujar(self, pantalla):
        return super().Dibujar(pantalla)


class Regadera(SpriteArrastrable):
    
    def __init__(self,nombreSprite= 'regadera'):
        x,y,x2,y2 = Config.coordenadas[nombreSprite]
        anchura, altura = Config.tamanos[nombreSprite]
        sprite = SpriteSheet(Config.spritesFile).obtenerSprite(x, y, anchura, altura)
        posicion = Config.posiciones[nombreSprite]
        super().__init__(redimensionarSprite(sprite,Config.escala), posicion)
        self.nombreSprite = nombreSprite
        self.contieneAgua = False
        
        # Para depuración
        print(f"coordenadas: x1:{x}, y1:{y}, x2:{x2}, y2:{y2}")
        print(f"nombreSprite: {nombreSprite}")
        print(f"Possicion: {Config.posiciones[nombreSprite]}")
        print(f"escala: {Config.escala}")
        print(f"Tamaño de la imagen: {Config.tamanos[nombreSprite]}")
    
    def Dibujar(self, pantalla):
        return super().Dibujar(pantalla)

class JardinZenSprites:
    """Clase para gestionar todos los sprites del Jarín Zen"""
    def __init__(self):
            self.fondo = Fondo()
            self.macetaCafe = Maceta()
            self.regadera = Regadera()
            self.plantaFase1 = Planta()

    def dibujarTodos(self, pantalla):
            """Dibuja todos los objetos en la pantalla"""
            self.fondo.Dibujar(pantalla)
            self.macetaCafe.Dibujar(pantalla)
            self.regadera.Dibujar(pantalla)
            self.plantaFase1.Dibujar(pantalla)

    def manejarEventos(self, eventos):
        """Distribuye eventos a los objetos correspondientes"""
        for evento in eventos:
            self.macetaCafe.ManejarEventoArrastrable(evento)
            self.regadera.ManejarEventoArrastrable(evento)
            self.plantaFase1.ManejarEventoArrastrable(evento)