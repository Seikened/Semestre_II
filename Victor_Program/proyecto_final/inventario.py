# inventario.py
import pygame
from config import Config

class Inventario:
    def __init__(self, pantalla, capacidad=10):
        self.pantalla = pantalla
        self.capacidad = capacidad
        self.slots = [{'id': None, 'cantidad': 0} for _ in range(capacidad)]
        self.activa = False
        self.fuente = pygame.font.Font(None, 24)
        self.hoveredItemIndex = None  # Índice del slot sobre el que está el cursor

    def agregarItem(self, item_id, cantidad=1):
        for slot in self.slots:
            if slot['id'] == item_id:
                slot['cantidad'] += cantidad
                return True
            elif slot['id'] is None:
                slot['id'] = item_id
                slot['cantidad'] = cantidad
                return True
        return False

    def quitarItem(self, item_id, cantidad=1):
        for slot in self.slots:
            if slot['id'] == item_id and slot['cantidad'] >= cantidad:
                slot['cantidad'] -= cantidad
                if slot['cantidad'] == 0:
                    slot['id'] = None
                return True
        return False

    def renderizar(self):
        if not self.activa:
            return
        
        altura_fondo = 60 + 30 * self.capacidad  # Ajuste dinámico del fondo según la cantidad de slots
        fondoInventario = pygame.Surface((300, altura_fondo))
        fondoInventario.fill((139, 69, 19))  # Marrón tipo madera
        rectFondoInventario = fondoInventario.get_rect(center=(Config.ventanaAncho // 2, Config.ventanaAlto // 2))
        self.pantalla.blit(fondoInventario, rectFondoInventario.topleft)
        pygame.draw.rect(self.pantalla, (255, 255, 255), rectFondoInventario, 3)  # Borde blanco

        textoTitulo = self.fuente.render("Inventario", True, (255, 255, 255))
        self.pantalla.blit(textoTitulo, (rectFondoInventario.left + 10, rectFondoInventario.top + 10))

        for i, slot in enumerate(self.slots):
            y_pos = rectFondoInventario.top + 50 + i * 30
            item_info = f"{slot['id'] if slot['id'] else 'Vacío'} x {slot['cantidad']}" if slot['id'] else "Vacío"
            colorTexto = (255, 255, 255) if i != self.hoveredItemIndex else (200, 200, 200)
            texto_slot = self.fuente.render(item_info, True, colorTexto)
            self.pantalla.blit(texto_slot, (rectFondoInventario.left + 10, y_pos))

    def manejarEventos(self, eventos):
        if not self.activa:
            return
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rectFondoInventario = pygame.Rect(0, 0, 300, 60 + 30 * self.capacidad)
        rectFondoInventario.center = (Config.ventanaAncho // 2, Config.ventanaAlto // 2)
        
        self.hoveredItemIndex = None
        for i, slot in enumerate(self.slots):
            y_pos = rectFondoInventario.top + 50 + i * 30
            item_rect = pygame.Rect(rectFondoInventario.left + 10, y_pos, 280, 30)
            if item_rect.collidepoint(mouse_x, mouse_y):
                self.hoveredItemIndex = i

    def toggle_activa(self):
        self.activa = not self.activa
