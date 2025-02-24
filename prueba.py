import sys
from PyQt6.QtWidgets import (QApplication, QLineEdit, QLabel, QPushButton, QWidget, 
                             QDialog, QMessageBox, QCheckBox, QHBoxLayout, 
                             QVBoxLayout, QStyle, QGridLayout, QTextEdit)
from PyQt6.QtGui import (QFont, QIcon)

class Crear_Row(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.flag = '1'
        self.crearow()

    def crearow(self):
        self.setGeometry(100, 100, 350, 300)
        self.setFixedHeight(300)
        self.setFixedWidth(350)
        self.setWindowTitle("Crear")
        
        # Variables
        self.label_title = QLabel(self)
        self.input_name_row = QLineEdit(self)
        self.input_data = QTextEdit(self)
        self.btn_save = QPushButton(self)
        self.btn_cancel = QPushButton(self)
        
        # Layouts
        layouts_title = QHBoxLayout()
        layouts_file = QHBoxLayout()
        layouts_file_2 = QHBoxLayout()
        layouts_button = QHBoxLayout()
        content = QVBoxLayout()
        
        # Configuración de elementos
        self.label_title.setText('Crear')
        self.label_title.setFont(QFont('Arial Black', 16))
        self.label_title.setFixedSize(70, 30)
        
        if self.flag == '1':
            valueContent = 'Nombre de la tabla'
        elif self.flag == '2':
            valueContent = 'Numero de Proceso'
            
        self.input_name_row.setPlaceholderText(valueContent)
        self.input_name_row.setFixedSize(250, 30)
        
        self.input_data.setPlaceholderText('Descripcion...')
        self.input_data.setFixedSize(250, 100)
        
        self.btn_save.setText('Guardar')
        self.btn_save.setMaximumHeight(30)
        self.btn_cancel.setText('Cancelar')
        self.btn_cancel.setMaximumHeight(30)
        
        # Organización de layouts
        layouts_title.addWidget(self.label_title)
        layouts_file.addWidget(self.input_name_row)
        layouts_file_2.addWidget(self.input_data)
        layouts_button.addWidget(self.btn_save)
        layouts_button.addWidget(self.btn_cancel)
        
        content.addLayout(layouts_title)
        content.addLayout(layouts_file)
        content.addLayout(layouts_file_2)
        content.addLayout(layouts_button)
        
        self.setLayout(content)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Crear_Row()
    window.show()
    sys.exit(app.exec())