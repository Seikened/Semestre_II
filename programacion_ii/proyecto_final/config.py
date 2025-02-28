# Archivo de configuración para el proyecto final

class Config:
    # Tamaño de la ventana
    ventanaAncho = 735
    ventanaAlto = 1033
    deltaTiempo = 0.0167  # Este valor es para 60 FPS
    pantallaTitulo = "Jardín Zen - Fase 1"
    
    # Potencia de riego
    potenciaRiego = 10
    

    # Rutas de los recursos
    imgFolder = "img"
    spritesFile = "sprites.png"
    fondo = "fondo.jpeg"
    
    escala = 20  # Escala de los sprites
    
    # Coordenadas iniciales (x, y) y finales (x2, y2)
    coordenadas = {
        'fondo': (0, 0, 735, 1033),
        'macetaCafe': (50, 348, 247, 524),
        'macetaNegra': (50, 553, 247, 730),
        'regadera': (1445, 388, 1849, 637),
        'plantaFase3': (9, 759, 298, 884),
        'plantaFase2': (9, 892, 298, 1007),
        'plantaFase1': (50, 1016, 267, 1110)
    }

    # Función para calcular las dimensiones a partir de las coordenadas iniciales y finales
    def calcularDimensiones(coord):
        return coord[2] - coord[0], coord[3] - coord[1]

    # Centro vertical (y) para cada sprite
    centroSprite = {
        'macetaCafe': (524 + 348) // 2,
        'macetaNegra': (730 + 553) // 2,
        'regadera': (637 + 388) // 2,
        'plantaFase3': 854,
        'plantaFase2': 997,
        'plantaFase1': 1099
    }

    # Tamaños calculados utilizando la función `calcularDimensiones`
    tamanos = {
        'macetaCafe': calcularDimensiones(coordenadas['macetaCafe']),
        'macetaNegra': calcularDimensiones(coordenadas['macetaNegra']),
        'regadera': calcularDimensiones(coordenadas['regadera']),
        'plantaFase3': calcularDimensiones(coordenadas['plantaFase3']),
        'plantaFase2': calcularDimensiones(coordenadas['plantaFase2']),
        'plantaFase1': calcularDimensiones(coordenadas['plantaFase1'])
    }

    # Posiciones iniciales en pantalla
    posiciones = {
        'huerto': (305, 600),
        'fotoFondo': (0, 0),
        'macetaCafe': (322, 615),
        'macetaNegra': (300, 100),
        'regadera': (392, 464),
        'plantaFase3': (600, 300),
        'plantaFase2': (400, 300),
        'plantaFase1': (55, 666)
    }


# Tienda de items
    items = [
        {
            id: 'macetaCafe',
            'nombre': 'Maceta Café',
            'precio': 100
        },
        {
            id: 'macetaNegra',
            'nombre': 'Maceta Negra',
            'precio': 150
        },
        {
            id: 'plantaFase1',
            'nombre': 'Mini palmera',
            'precio': 150
        }
    ]