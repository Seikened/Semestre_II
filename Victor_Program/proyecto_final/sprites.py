import os
import pygame
import random
from config import Config

debug = False

def depurarSprite(nombre, coordenadas, posicion, escala, tamanos, numero_objeto):
    x1, y1, x2, y2 = coordenadas
    # Colores
    cyan = "\033[36m"
    green = "\033[32m"
    yellow = "\033[33m"
    magenta = "\033[35m"
    reset = "\033[0m"
    
    
    
    if debug == True:
        print(f"Depurando {nombre}:")
        print(f"  {cyan}Coordenadas{reset} | x1: {green}{x1}{reset}, y1: {green}{y1}{reset}, x2: {green}{x2}{reset}, y2: {green}{y2}{reset}")
        print(f"  Posición inicial - {magenta}{posicion}{reset}")
        print(f"  Escala aplicada - {yellow}{escala}%{reset}")
        print(f"  Dimensiones después de escalar - Ancho: {yellow}{tamanos[0]}{reset}, Alto: {yellow}{tamanos[1]}{reset}")
        print(f"  Número de objeto: {magenta}{numero_objeto}{reset}")
    else:
        pass



def redimensionarSprite(sprite, escala):
    """ Redimensiona un sprite según la escala dada """
    anchura, altura = sprite.get_size()
    nuevaAnchura = int(anchura * escala / 100)
    nuevaAltura = int(altura * escala / 100)
    return pygame.transform.scale(sprite, (nuevaAnchura, nuevaAltura))


def calcularPosicionX(maceta, planta):
    # Calcular el centro horizontal de la maceta y de la planta
    centro_x_maceta = maceta.posicion[0] + maceta.sprite.get_width() / 2
    centro_x_planta = planta.sprite.get_width() / 2
    
    # Ajustar la posición x de la planta para que quede centrada con la maceta
    nueva_posicion_x = centro_x_maceta - centro_x_planta
    return nueva_posicion_x


def calcularPosicionY(maceta, planta):
    # Usar centroSprite para el ajuste vertical
    ajuste_y = Config.centroSprite[maceta.tipoMaceta] - Config.centroSprite[planta.nombreSprite]
    nueva_posicion_y = maceta.posicion[1] + ajuste_y
    
    # Ajustar para que el borde inferior de la planta quede justo sobre el borde superior de la maceta
    nueva_posicion_y -= planta.sprite.get_height() / 2
    
    return nueva_posicion_y


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
        self.movil = True # Si el objeto se puede mover

    def ManejarEventoArrastrable(self, evento):
        if not self.movil:
            return
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
        
        # Asociación con la planta
        self.contienePlanta = False
        self.planta = None
        # Asociación con la el huerto
        self.enHuerto = False
        self.posicionHuerto = None
        
        # Atributos de la maceta
        self.tipoMaceta = 'cafe'
        self.idMaceta = Maceta.numeroMacetas
        Maceta.numeroMacetas += 1
        
        # Para depuración
        depurarSprite(nombreSprite, (x, y, x2, y2), posicion, Config.escala, Config.tamanos[nombreSprite], Maceta.numeroMacetas)
    
    
    def cambiarMacetaNegra(self):
        x,y,x2,y2 = Config.coordenadas['macetaNegra']
        anchura, altura = Config.tamanos['macetaNegra']
        sprite = SpriteSheet(Config.spritesFile).obtenerSprite(x, y, anchura, altura)
        self.sprite = redimensionarSprite(sprite,Config.escala)
        self.tipoMaceta = 'negra'
        
        # Para depuración
        depurarSprite('macetaNegra', (x, y, x2, y2), Config.posiciones['macetaNegra'], Config.escala, Config.tamanos['macetaNegra'], Maceta.numeroMacetas)
    
    def plantarPlanta(self, planta):
        self.contienePlanta = True
        self.planta = planta
        planta.enMaceta = True
        x, y = self.posicion
        planta.posicion = (x , y - 10)
        planta.maceta = self
        
    
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
        self.maceta = None
        self.idPlanta = Planta.numeroPlantas
        self.edad = 1
        self.movil = False
        Planta.numeroPlantas += 1
        
        # Para depuración
        depurarSprite(nombreSprite, (x, y, x2, y2), posicion, Config.escala, Config.tamanos[nombreSprite], Planta.numeroPlantas)

    def faseDosCrecimiento(self):
        self.nombreSprite = 'plantaFase2'
        x,y,x2,y2 = Config.coordenadas[self.nombreSprite]
        anchura, altura = Config.tamanos[self.nombreSprite]
        sprite = SpriteSheet(Config.spritesFile).obtenerSprite(x, y, anchura, altura)
        self.sprite = redimensionarSprite(sprite,Config.escala)
        
        # Para depuración
        depurarSprite('plantaFase2', (x, y, x2, y2), Config.posiciones['plantaFase2'], Config.escala, Config.tamanos['plantaFase2'], Planta.numeroPlantas)
    
    
    def faseTresCrecimiento(self):
        self.nombreSprite = 'plantaFase3'
        x,y,x2,y2 = Config.coordenadas[self.nombreSprite]
        anchura, altura = Config.tamanos[self.nombreSprite]
        sprite = SpriteSheet(Config.spritesFile).obtenerSprite(x, y, anchura, altura)
        self.sprite = redimensionarSprite(sprite,Config.escala)
        
        # Para depuración
        depurarSprite('plantaFase3', (x, y, x2, y2), Config.posiciones['plantaFase3'], Config.escala, Config.tamanos['plantaFase3'], Planta.numeroPlantas)
    
    def cambiarFaseCrecimiento(self):
        if self.edad > 100 and self.edad <= 200:
            self.faseDosCrecimiento()
        elif self.edad > 200:
            self.faseTresCrecimiento()
    
    def crecer(self,multiplicador=1):
        self.edad += multiplicador
        self.cambiarFaseCrecimiento()
        print(f"La edad de la planta es: {self.edad}")
    
    
    def Dibujar(self, pantalla):
        return super().Dibujar(pantalla)



class Particula:
    def __init__(self, posicion, pantalla):
            self.pantalla = pantalla
            self.posicion = list(posicion)
            self.tiempoVida = 30  # Reducido para que las partículas desaparezcan más rápido
            # Inicialización de la velocidad con una componente vertical hacia arriba
            self.velocidad = [random.uniform(-2, 2), random.uniform(-1, -0.1)]
            self.gravedad = 0.05  # Aceleración debido a la gravedad
            self.tamano = (2, 2)  # Tamaño de la partícula


    def actualizar(self):
        """Actualiza la posición de la partícula, aplica gravedad y reduce su tiempo de vida."""
        if self.tiempoVida > 0:
            self.velocidad[1] += self.gravedad  # Aplica gravedad incrementando la velocidad en y
            self.posicion[0] += self.velocidad[0]
            self.posicion[1] += self.velocidad[1]
            self.tiempoVida -= 1
            self.mostrar()
        else:
            return False  # Indica que debe ser eliminada
        return True

    def mostrar(self):
            """Dibuja la partícula en la pantalla como un pequeño rectángulo (píxel)."""
            pygame.draw.rect(self.pantalla, (0, 122, 255), pygame.Rect(self.posicion[0], self.posicion[1], *self.tamano))



class Regadera(SpriteArrastrable):
    def __init__(self, pantalla, huerto,nombreSprite='regadera'):
        x , y, x2, y2 = Config.coordenadas[nombreSprite]
        anchura, altura = Config.tamanos[nombreSprite]
        sprite = SpriteSheet(Config.spritesFile).obtenerSprite(x, y, anchura, altura)
        posicion = Config.posiciones[nombreSprite]
        super().__init__(redimensionarSprite(sprite,Config.escala), posicion)
        self.huerto = huerto
        self.pantalla = pantalla
        self.particulas = []


    def regarPlanta(self, posicion, planta):
        """Genera partículas en la posición centrada del sprite de la planta y hace crecer la planta."""
        centroX = planta.posicion[0] + planta.sprite.get_width() // 2
        centroY = planta.posicion[1] + planta.sprite.get_height() // 2
        posicion_central = (centroX, centroY)

        for _ in range(20):  # Genera varias partículas para un efecto más denso
            self.particulas.append(Particula(posicion_central, self.pantalla))
        planta.crecer(Config.potenciaRiego)
        # Restablece la regadera a su posición original
        self.posicion = Config.posiciones['regadera']

    def actualizarParticulas(self):
        """Actualiza y filtra las partículas activas."""
        self.particulas = [p for p in self.particulas if p.actualizar()]

    def ManejarEventoArrastrable(self, evento):
        super().ManejarEventoArrastrable(evento)
        if evento.type == pygame.MOUSEBUTTONUP:
            # Verificar si la regadera está sobre alguna planta
            for maceta in self.huerto.macetas:
                if maceta.contienePlanta and self.sprite.get_rect(topleft=self.posicion).colliderect(maceta.planta.sprite.get_rect(topleft=maceta.planta.posicion)):
                    posicionPlanta = (maceta.posicion[0], maceta.posicion[1] - 20)
                    self.regarPlanta(posicionPlanta, maceta.planta)
                    break

    def Dibujar(self, pantalla):
        super().Dibujar(pantalla)
        for particula in self.particulas:
            particula.mostrar()
        self.actualizarParticulas()



class Huerto:
    def __init__(self):
        x, y = Config.posiciones['huerto']
        self.filas = 3
        self.columnas = 3
        self.espacios = [[None for _ in range(self.columnas)] for _ in range(self.filas)]
        self.macetas = []
        self.espacio_x = 75  # Espacio entre columnas
        self.espacio_y = 75  # Espacio entre filas
        self.base_x = x  # Coordenada x inicial
        self.base_y = y  # Coordenada y inicial

    def agregarMaceta(self, maceta):
        print("Agregando maceta al huerto")
        for fila in range(self.filas):
            for columna in range(self.columnas):
                if self.espacios[fila][columna] is None:
                    x = self.base_x + columna * self.espacio_x
                    y = self.base_y + fila * self.espacio_y
                    maceta.posicion = (x, y)
                    maceta.enHuerto = True
                    maceta.posicionHuerto = (fila, columna)
                    maceta.movil = False  # Asegurar que la maceta no se mueva una vez colocada
                    print(f"Print estado de movilidad de la maceta: {maceta.movil}")
                    if maceta.planta:
                        maceta.planta.movil = False  # También inmovilizar la planta
                        print(f"Print estado de movilidad de la maceta: {maceta.movil} y planta: {maceta.planta.movil}")
                    self.espacios[fila][columna] = maceta
                    self.macetas.append(maceta)
                    return True  # Detener después de colocar una maceta para evitar duplicados
        print("No hay espacio disponible en el huerto")
        return False


    def dibujarHuerto(self, pantalla):
        # Dibuja un fondo de cuadrícula para el huerto
        for fila in range(self.filas):
            for columna in range(self.columnas):
                rect = pygame.Rect(self.base_x + columna * self.espacio_x,
                                   self.base_y + fila * self.espacio_y,
                                   self.espacio_x, self.espacio_y)
                pygame.draw.rect(pantalla, (200, 200, 200), rect, 1)
        # Dibuja las macetas en su posición actual
        for maceta in self.macetas:
            maceta.Dibujar(pantalla)
            if maceta.contienePlanta:
                maceta.planta.Dibujar(pantalla)

    def manejarEventosHuerto(self, eventos):
        """Distribuye eventos a las macetas en el huerto."""
        for evento in eventos:
            for maceta in self.macetas:
                maceta.ManejarEventoArrastrable(evento)
                if maceta.planta:
                    maceta.planta.ManejarEventoArrastrable(evento)



class JardinZenSprites:
    """Clase para gestionar todos los sprites del Jardín Zen."""

    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.fondo = Fondo()
        self.huerto = Huerto() # Espacios de 100 píxeles entre macetas
        self.regadera = Regadera(pantalla, self.huerto)
        
        # Inicializar macetas y plantas
        self.inicializarMacetasYPlantas()

    def inicializarMacetasYPlantas(self):
        # Crear y agregar macetas y asociarlas con plantas y ambas con el huerto
        multiplicador = 50
        for _ in range(5):
            maceta = Maceta()
            planta = Planta()
            self.huerto.agregarMaceta(maceta)       
            maceta.plantarPlanta(planta)
            maceta.cambiarMacetaNegra()
            planta.crecer(multiplicador)
            multiplicador += 50

    def dibujarTodos(self):
        """Dibuja todos los objetos en la pantalla."""
        self.fondo.Dibujar(self.pantalla)
        self.huerto.dibujarHuerto(self.pantalla)
        self.regadera.Dibujar(self.pantalla)

    def manejarEventos(self, eventos):
        """Distribuye eventos a los objetos correspondientes."""
        for evento in eventos:
            self.huerto.manejarEventosHuerto(eventos)
            self.regadera.ManejarEventoArrastrable(evento)