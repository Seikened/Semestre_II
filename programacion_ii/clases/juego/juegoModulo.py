import pygame
from config import Config
import random




class Juego():
    def __init__(self):
        x1=20
        y1=20
        x2=Config.canchaAncho-20
        y2=Config.canchaAlto-20
        
        self.cancha = Cancha(x1,y1,x2,y2)
        
        self.pelotas = [Pelota(Config.canchaAncho//2, Config.canchaAlto//2) for _ in range(500)]
        
        xRaqueta = x1 + 30
        yRaqueta = Config.canchaAlto/2
        
        self.raqueta = Raqueta(xRaqueta,yRaqueta,Config.raquetaAncho,Config.raquetaAlto,pygame.K_w,pygame.K_s)
        
        
        
        self.raqueta2 = Raqueta(x2 - 30,yRaqueta,Config.raquetaAncho,Config.raquetaAlto,pygame.K_UP,pygame.K_DOWN)


    def Dibuja(self,screen):
        # Cancha
        self.cancha.Dibuja(screen)
        # Pelotas
        for pelota in self.pelotas:
            pelota.Dibuja(screen)
        # Raquetas
        self.raqueta.Dibuja(screen)
        self.raqueta2.Dibuja(screen)
        


    def Recalcula(self):
        # Actualizar la pos de la pelotas
        for pelota in self.pelotas:
            pelota.ActualizaPosicion(self.cancha)
            self.raqueta.DetectaColision(pelota)
            self.raqueta2.DetectaColision(pelota)
        # movimiento de las raquetas
        self.raqueta.ActualizaPosicion(pygame.key.get_pressed())
        self.raqueta2.ActualizaPosicion(pygame.key.get_pressed())


class Raqueta:
    def __init__(self,x,y,ancho,alto,key_up,key_down):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.color = Config.raquetaColor
        self.key_up = key_up
        self.key_down = key_down
    
    def Dibuja(self,screen):
        x1 = self.x - self.ancho/2
        y1 = self.y - self.alto/2
        rect=(x1,y1,self.ancho,self.alto)
        pygame.draw.rect(screen,self.color,rect)
    
    def ActualizaPosicion(self,key):
        if self.y - self.alto/2 > 20:
            if key[self.key_up]:
                self.y -= 20
        if self.y + self.alto/2 < 580:
            if key[self.key_down]:
                self.y += 20
    
    def DetectaColision(self,pelota):
        raqueta_centro_x = self.x
        raqueta_centro_y = self.y
        # Definir los límites de la raqueta
        raqueta_left = raqueta_centro_x - self.ancho / 2
        raqueta_right = raqueta_centro_x + self.ancho / 2
        raqueta_top = raqueta_centro_y - self.alto / 2
        raqueta_bottom = raqueta_centro_y + self.alto / 2
        # "Rectángulo" de la pelota
        pelota_left = pelota.x - pelota.radio
        pelota_right = pelota.x + pelota.radio
        pelota_top = pelota.y - pelota.radio
        pelota_bottom = pelota.y + pelota.radio
        # Comprobar colisión (Sacado de chat)
        if (pelota_right >= raqueta_left and pelota_left <= raqueta_right and
            pelota_bottom >= raqueta_top and pelota_top <= raqueta_bottom):
            
            # Determinar si la colisión es más horizontal o vertical (Sacado de chat)
            overlap_left = pelota_right - raqueta_left
            overlap_right = raqueta_right - pelota_left
            overlap_top = pelota_bottom - raqueta_top
            overlap_bottom = raqueta_bottom - pelota_top
            # Encuentra el mínimo solapamiento (Sacado de chat)
            min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)
            # Resuelve la colisión basada en el mínimo solapamiento (Sacado de chat)
            if min_overlap == overlap_left:
                pelota.x = raqueta_left - pelota.radio
                pelota.velocidadX = -pelota.velocidadX
            elif min_overlap == overlap_right:
                pelota.x = raqueta_right + pelota.radio
                pelota.velocidadX = -pelota.velocidadX
            elif min_overlap == overlap_top:
                pelota.y = raqueta_top - pelota.radio
                pelota.velocidadY = -pelota.velocidadY
            elif min_overlap == overlap_bottom:
                pelota.y = raqueta_bottom + pelota.radio
                pelota.velocidadY = -pelota.velocidadY

class Pelota():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidadX = 100
        self.velocidadY = 100
        self.radio = Config.relotaRadio
        self.color = Config.pelotaColor
        self.VelocidadAleatoria()
    
    def VelocidadAleatoria(self):
        self.velocidadX = int(random.randint(100,300))
        self.velocidadY = int(random.randint(100,300))
    
    def ActualizaPosicion(self,cancha):
        self.x += self.velocidadX * Config.deltaTiempo
        self.y += self.velocidadY * Config.deltaTiempo
    
        # Rebota en el borde de la cancha verde (No en la pantalla completa)
        
        # Esta es la pared derecha
        if self.x + self.radio > cancha.x2:
            self.velocidadX = -self.velocidadX
            self.x = cancha.x2 - self.radio
        
        # Esta es la pared izquierda
        if self.x - self.radio < cancha.x1:
            self.velocidadX = -self.velocidadX
            self.x = cancha.x1 + self.radio
        
        # Esta es la pared de abajo
        if self.y + self.radio > cancha.y2:
            self.velocidadY = -self.velocidadY
            self.y = cancha.y2 - self.radio
        
        # Esta es la pared de arriba
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