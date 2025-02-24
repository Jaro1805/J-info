import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QMessageBox, QPushButton,
                            QLineEdit, QHBoxLayout, QVBoxLayout, QStyle)
from PyQt6.QtGui import QFont, QPixmap, QIcon, QColor


class indice(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(200, 50, 500, 400)
        self.setWindowTitle('Menu de Opciones')
        self.menu()
        self.show()

    def menu(self):
        label_mensaje = QLabel(self)
        btn_menu_1 = QPushButton('opcion 1')
        btn_menu_2 = QPushButton('opcion 2')
        btn_menu_3 = QPushButton('opcion 3')
        btn_menu_4 = QPushButton('opcion 4')
        btn_menu_5 = QPushButton('opcion 5')
        btn_menu_6 = QPushButton('opcion 6')

        #---------------------- iconos ----------------------------
        urlIcon = '/Users/jose/Documents/Developer/Projet-tesis/Icon/'
       
        btn_menu_1.setIcon(QIcon(urlIcon + 'table-list-solid.svg'))
        # btn_menu_2.setIcon(QIcon(urlIcon + 'table-list-solid.svg'))
        # btn_menu_3.setIcon(QIcon(urlIcon + 'table-list-solid.svg'))
        # btn_menu_4.setIcon(QIcon(urlIcon + 'table-list-solid.svg'))
        # btn_menu_5.setIcon(QIcon(urlIcon + 'table-list-solid.svg'))
        # btn_menu_6.setIcon(QIcon(urlIcon + 'table-list-solid.svg'))

        #---------------------- iconos ----------------------------
        #----------------------Layouts----------------------------

        fila_1 = QHBoxLayout()
        fila_2 = QHBoxLayout()
        fila_title = QHBoxLayout()
        content = QVBoxLayout()

        fila_title.addWidget(label_mensaje)

        fila_1.addWidget(btn_menu_1)
        fila_1.addWidget(btn_menu_2)
        fila_1.addWidget(btn_menu_3)

        fila_2.addWidget(btn_menu_4)
        fila_2.addWidget(btn_menu_5)
        fila_2.addWidget(btn_menu_6)

        content.addLayout(fila_title)
        content.addLayout(fila_1)
        content.addLayout(fila_2)

        self.setLayout(content)
        #----------------------fin Layouts----------------------------

        #------------ Mensaje de Menu--------------------
        label_mensaje.setText('Tools')
        label_mensaje.setFixedSize(100, 50)
        label_mensaje.setFont(QFont('Arial Black', 20))
        #------------ fin Mensaje de Menu--------------------

        
        btn_menu_1.setMinimumSize(90, 90)
        btn_menu_2.setMinimumSize(90, 90)
        btn_menu_3.setMinimumSize(90, 90)
        btn_menu_4.setMinimumSize(90, 90)
        btn_menu_5.setMinimumSize(90, 90)
        btn_menu_6.setMinimumSize(90, 90)
        

     
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = indice()
    sys.exit(app.exec())