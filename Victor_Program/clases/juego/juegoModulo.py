import pygame
from config import Config





class Juego():
    def __init__(self):
        x1=20
        y1=20
        x2=Config.canchaAncho-20
        y2=Config.canchaAlto-20
        
        self.cancha = Cancha(x1,y1,x2,y2)
        self.pelota = Pelota(Config.canchaAncho//2,Config.canchaAlto//2)
        
        xRaqueta = x1 + 30
        yRaqueta = Config.canchaAlto/2
        
        self.raqueta = Raqueta(xRaqueta,
                               yRaqueta,
                               Config.raquetaAncho,
                               Config.raquetaAlto,
                               pygame.K_w,
                               pygame.K_s)
        
        
        
        self.raqueta2 = Raqueta(x2 - 30,
                                yRaqueta,
                                Config.raquetaAncho,
                                Config.raquetaAlto,
                                pygame.K_UP,
                                pygame.K_DOWN)


    def Dibuja(self,screen):
        self.cancha.Dibuja(screen)
        self.pelota.Dibuja(screen)
        self.raqueta.Dibuja(screen)
        self.raqueta2.Dibuja(screen)


    def Recalcula(self):
        self.pelota.ActualizaPosicion(self.cancha)
        self.raqueta.ActualizaPosicion(pygame.key.get_pressed())
        self.raqueta2.ActualizaPosicion(pygame.key.get_pressed())

class Raqueta:
    def __init__(self,x,y,ancho,alto,key_up,key_down):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.color = (255,0,0)
        self.key_up = key_up
        self.key_down = key_down
    
    def Dibuja(self,screen):
        x1 = self.x - self.ancho/2
        y1 = self.y - self.alto/2
        rect=(x1,y1,self.ancho,self.alto)
        pygame.draw.rect(screen,self.color,rect)
    
    def ActualizaPosicion(self,key):
        if key[self.key_up]: self.y -= 20
        if key[self.key_down]: self.y += 20


class Pelota():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidadX = Config.pelotaVelX
        self.velocidadY = Config.pelotaVelY
        self.radio = Config.relotaRadio
        self.color = Config.pelotaColor
    
    def ActualizaPosicion(self,cancha):
        self.x += self.velocidadX * Config.deltaTiempo
        self.y += self.velocidadY * Config.deltaTiempo
    
        # Rebota en el borde de la cancha verde (No en la pantalla completa)
        if self.x + self.radio > cancha.x2:
            self.velocidadX = -self.velocidadX
            self.x = cancha.x2 - self.radio
        if self.x - self.radio < cancha.x1:
            self.velocidadX = -self.velocidadX
            self.x = cancha.x1 + self.radio
        if self.y + self.radio > cancha.y2:
            self.velocidadY = -self.velocidadY
            self.y = cancha.y2 - self.radio
        if self.y - self.radio < cancha.y1:
            self.velocidadY = -self.velocidadY
            self.y = cancha.y1 + self.radio


    def Dibuja(self,screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radio)



class Cancha():
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def Dibuja(self,screen):
        ancho = self.x2 - self.x1
        alto = self.y2 - self.y1
        rect=(self.x1,self.y1,ancho,alto)
        pygame.draw.rect(screen,Config.chanchaColor,rect)
