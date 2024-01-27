from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QIcon  # Corregido aquí
from PyQt5.QtCore import Qt
from pathlib import Path

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Drag & Drop | Convertidor 🔁 & Unificador ⏺️')
        
        self.setWindowIcon(QIcon('/Users/fernandoleonfranco/Documents/Imagnes/icone.ico'))
        self.resize(500, 500)  # Hacer la ventana más cuadrada
        self.setAcceptDrops(True)  # Hacer que la ventana acepte arrastrar y soltar
        self.filepaths = []  # Lista para almacenar las rutas de archivos arrastrados

        layout = QVBoxLayout()

        self.infoLabel = QLabel('Arrastra y suelta tus archivos 📄 .py aquí')
        self.infoLabel.setAlignment(Qt.AlignCenter)  # Centrar el texto
        layout.addWidget(self.infoLabel)

        # Crear el layout horizontal para el botón
        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch(1)  # Espacio antes del botón para centrarlo

        self.button = QPushButton('Procesar Archivos ✅')
        self.button.setFixedSize(200, 50)  # Tamaño del botón
        buttonLayout.addWidget(self.button)  # Añadir el botón al layout horizontal

        buttonLayout.addStretch(1)  # Espacio después del botón para centrarlo

        # Añadir el layout horizontal al layout vertical principal
        layout.addLayout(buttonLayout)

        self.button.clicked.connect(self.procesar_archivos)

        self.setLayout(layout)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            self.filepaths = [str(url.toLocalFile()) for url in urls]  # Actualizar las rutas de archivos
            self.actualizar_info_archivos(self.filepaths)

    def actualizar_info_archivos(self, filepaths):
        num_archivos = len(filepaths)
        nombres_archivos = [Path(f).name for f in filepaths]
        self.infoLabel.setText(f"{num_archivos} archivos cargados:\n" + "\n".join(nombres_archivos))

    def procesar_archivos(self):
        lista_contenidos = []
        
        for ruta in self.filepaths:
            filepath = Path(ruta)
            if filepath.is_file():
                contenido = filepath.read_text(encoding='utf-8')
                lista_contenidos.append("#" + f"{filepath.name}" + "\n" + contenido + "\n" + "-"*50)
                
        contenidos_combinados = "\n".join(lista_contenidos)
        archivo_de_salida = Path('/Users/fernandoleonfranco/Downloads/FERNANDO_TAREAS.txt')
        archivo_de_salida.write_text(contenidos_combinados, encoding='utf-8')
        #print("Tu archivo se genero con exito")
        QMessageBox.information(self, "Proceso completado", "¡Los archivos han sido procesados con éxito!")

if __name__ == '__main__':
    app = QApplication([])
    demo = AppDemo()
    demo.show()
    app.exec_()
