import sys 
from PyQt6.QtWidgets import (QApplication, QLineEdit, QLabel, QPushButton, QWidget, QDialog, QMessageBox, QTextEdit,
                             QHBoxLayout, QVBoxLayout, QStyle, QGridLayout)
from PyQt6.QtGui import (QFont, QIcon)

class EditMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.edit_data()

    def edit_data(self):
        self.setGeometry(100, 100, 350, 300)
        self.setFixedHeight(300)
        self.setFixedWidth(350)
        self.setWindowTitle("Editar Data")
        
        #--------------------------------------------- Variables
        label_title = QLabel(self)
        input_search = QLineEdit(self)
        input_data = QTextEdit(self)
        btn_save = QPushButton(self)
        btn_cancel = QPushButton(self)
        btn_search = QPushButton(self)


        #--------------------------------------------- Layouts
        layouts_title = QHBoxLayout()
        layouts_file = QHBoxLayout()
        layouts_file_2 = QHBoxLayout()
        layouts_button = QHBoxLayout()
        content = QVBoxLayout()

        #---------------------------------------------  layouts_title
        label_title.setText('Editar')
        label_title.setFont(QFont('Arial Black', 16))   
        label_title.setFixedSize(70, 30)

        #--------------------------------------------- layouts_file
        input_search.setPlaceholderText('Buscar...')
        input_search.setFixedSize(250, 30)

        urlIcon = '/Users/jose/Documents/Developer/Projet-tesis/Icon/'
        btn_search.setIcon(QIcon(urlIcon + 'buscar.svg'))
        btn_search.setFixedSize(30, 30)


        #------------------------------------------------ layouts_file_2
        input_data.setPlaceholderText('Descripcion...')
        input_data.setFixedSize(300, 100)

        #--------------------------------------------- layouts_button
        btn_save.setText('Guardar') 
        btn_save.setFixedHeight(40)

        btn_cancel.setText('Cancelar')
        btn_cancel.setFixedHeight(40)

        #--------------------------------------------- Layouts
        layouts_title.addWidget(label_title)

        layouts_file.addWidget(input_search)
        layouts_file.addWidget(btn_search)

        layouts_file_2.addWidget(input_data)

        layouts_button.addWidget(btn_save)
        layouts_button.addWidget(btn_cancel)

        content.addLayout(layouts_title)
        content.addLayout(layouts_file)
        content.addLayout(layouts_file_2)
        content.addLayout(layouts_button)

        self.setLayout(content)
        # label_title.setMaximumHeight(30)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EditMain()
    window.show()
    sys.exit(app.exec())    