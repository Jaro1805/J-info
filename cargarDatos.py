import sys
from PyQt6.QtWidgets import (QApplication, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, 
                             QDialog, QTextEdit, QWidget, QLineEdit)
from PyQt6.QtGui import QFont, QIcon

class cargarDatos(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.setWindowTitle('J-Info')
        self.flag = '1'
        self.motrarData()

    def motrarData(self):
        self.setGeometry(200, 50, 800, 600)
        self.setMinimumSize(600, 600)
        
        #_______________________Variables_______________________
        self.label_title = QLabel(self)
        self.window_content = QTextEdit(self)
        self.input_data = QLineEdit(self)
        self.btn_search = QPushButton(self)
        self.btn_Adj = QPushButton('Adjuntar', self)

        #_______________________Layout_______________________
        layout_title = QHBoxLayout()
        layout_file = QHBoxLayout()
        layout_file2 = QHBoxLayout()
        layout_button = QHBoxLayout()
        content = QVBoxLayout()

        #_______________________Layout Title_______________________
        if self.flag == '1':
            name = 'Ficha de Cliente'

        self.label_title.setText(name)
        self.label_title.setFont(QFont('Arial Black', 16))
        self.label_title.setFixedSize(190, 50)

        #_________________________Content_________________________

        self.input_data.setPlaceholderText('Buscar...')
        self.input_data.setMinimumWidth(450)
        self.input_data.setMaximumWidth(650)
        self.input_data.setFixedHeight(30)

        urlimg = 'icons/'
        self.btn_search.setIcon(QIcon(urlimg + 'buscar.svg'))
        self.btn_search.setFixedSize(60, 30)

        self.btn_Adj.setFixedSize(90, 40)
        
        self.window_content.setReadOnly(True)
        self.window_content.setFont(QFont('Arial', 8))
        self.window_content.setMinimumHeight(300)
        self.window_content.setMaximumHeight(350)
        self.window_content.setMinimumWidth(550)
        self.window_content.setMaximumWidth(750)
        self.window_content.setPlaceholderText('Ficha Cliente ...')

        #_______________________Layout File_______________________
        layout_title.addWidget(self.label_title)
        layout_file.addWidget(self.input_data)
        layout_file.addWidget(self.btn_search)
        layout_file2.addWidget(self.window_content)
        layout_button.addWidget(self.btn_Adj)

        content.addLayout(layout_title)
        content.addLayout(layout_file)
        content.addLayout(layout_file2)
        content.addLayout(layout_button)
        
        self.setLayout(content)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = cargarDatos()
    window.show()
    sys.exit(app.exec())