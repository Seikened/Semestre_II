import pygame
from config import Config

class Tienda:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.fuente = pygame.font.Font(None, 24)
        self.articulos = Config.items
        self.activa = False
        self.hoveredItemIndex = None  # Índice del artículo sobre el que está el cursor

    def renderizar(self):
        if not self.activa:
            return

        # Configuración del fondo de la tienda
        fondoTienda = pygame.Surface((300, 200))
        fondoTienda.fill((34, 139, 34))
        rectFondoTienda = fondoTienda.get_rect(center=(Config.ventanaAncho // 2, Config.ventanaAlto // 2))
        self.pantalla.blit(fondoTienda, rectFondoTienda.topleft)
        pygame.draw.rect(self.pantalla, (255, 255, 255), rectFondoTienda, 3)

        # Título de la tienda
        superficieTitulo = self.fuente.render("Tienda de Jardinería", True, (255, 255, 255))
        self.pantalla.blit(superficieTitulo, (rectFondoTienda.left + 10, rectFondoTienda.top + 10))

        # Renderizar cada artículo de la tienda
        for i, articulo in enumerate(self.articulos):
            y_pos = rectFondoTienda.top + 50 + i * 30
            texto = f"{articulo['nombre']} - ${articulo['precio']}"
            colorTexto = (255, 255, 255) if i != self.hoveredItemIndex else (200, 200, 200)  # Cambio de color si es hovered
            superficieTexto = self.fuente.render(texto, True, colorTexto)
            self.pantalla.blit(superficieTexto, (rectFondoTienda.left + 10, y_pos))

    def manejarEventos(self, eventos):
        if not self.activa:
            return
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rectFondoTienda = pygame.Rect(0, 0, 300, 200)  # Rectángulo del fondo de la tienda
        rectFondoTienda.center = (Config.ventanaAncho // 2, Config.ventanaAlto // 2)

        self.hoveredItemIndex = None
        for i, articulo in enumerate(self.articulos):
            y_pos = rectFondoTienda.top + 50 + i * 30
            item_rect = pygame.Rect(rectFondoTienda.left + 10, y_pos, 280, 30)
            if item_rect.collidepoint(mouse_x, mouse_y):
                self.hoveredItemIndex = i  # Establece el índice del artículo hovered

        for evento in eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if self.hoveredItemIndex is not None:
                    # Código para manejar la compra del artículo hovered
                    print(f"Comprado: {self.articulos[self.hoveredItemIndex]['nombre']}")
    
    def toggle_activa(self):
        self.activa = not self.activa