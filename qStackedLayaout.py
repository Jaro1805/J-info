import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, 
                             QPushButton, QStackedLayout, QFormLayout,
                             QVBoxLayout, QHBoxLayout, QComboBox, QDateEdit, 
                             QMessageBox, QTextEdit)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt, QDate

class MainWindows(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setFixedSize(500, 500)
        self.setWindowTitle("QStackedLayout")
        self.generate_win()
        self.show()

    def generate_win(self):
        btn1 = QPushButton("Wind 1")
        btn1.clicked.connect(self.change_wind)

        btn2 = QPushButton("Wind 2")
        btn2.clicked.connect(self.change_wind)

        btn3 = QPushButton("Wind 3")
        btn3.clicked.connect(self.change_wind)

        btn_layaouts = QVBoxLayout()
        btn_layaouts.addWidget(btn1)
        btn_layaouts.addWidget(btn2)
        btn_layaouts.addWidget(btn3)

        title = QLabel("Mapa")
        title.setFont(QFont("Arial", 18))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        image_map = QLabel()
        img = QPixmap("imgprueba.png")
        image_map.setPixmap(img)
        wind = self.size()
        image_map.setMaximumSize(wind)
        image_map.setScaledContents(True)

        wind_content = QVBoxLayout()
        wind_content.addWidget(title)
        wind_content.addWidget(image_map)

#----------------------- container 
        container_1 = QWidget()
        container_1.setLayout(wind_content)
#-----------------------------------
        title = QLabel("FormularioP")
        title.setFont(QFont("Arial", 18))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)


        self.nombre = QLineEdit()
        self.nombre.setPlaceholderText("Nombre")
        
        self.apellido = QLineEdit()
        self.apellido.setPlaceholderText("Apellido")

        self.genero_sel = QComboBox()
        self.genero_sel.addItems(["Masculino", "Femenino", "Helicoptero apache"])

        self.fecha = QDateEdit()
        self.fecha.setDisplayFormat("yyyy-MM-dd")
        self.fecha.setMaximumDate(
            QDate.currentDate() #Colocar como fecha maxima el dia de hoy
        )

        self.fecha.setCalendarPopup(True)
        self.fecha.setDate(QDate.currentDate())

        self.tlf = QLineEdit()
        self.tlf.setPlaceholderText("ej: 0412-9999999")

        submit_btn = QPushButton("SUBMIT")
        submit_btn.clicked.connect(self.mostrar_mss)

        file_1 = QHBoxLayout()
        # file_2 = QHBoxLayout()
        # file_3 = QHBoxLayout()
        # file_4 = QHBoxLayout()
        form_content = QFormLayout()

        file_1.addWidget(self.nombre)
        file_1.addWidget(self.apellido)


        form_content.addRow(title)
        form_content.addRow(file_1)
        form_content.addRow("Nacimiento: ", self.fecha)
        form_content.addRow("Telefono: ", self.tlf)
        form_content.addRow("Genero: ", self.genero_sel)
        form_content.addRow(submit_btn)
        self.setLayout(form_content)

        #--------------------Container 2
        container_2 = QWidget()
        container_2.setLayout(form_content)

        title3 = QLabel()
        title3.setFont(QFont("Arial", 18))
        title3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.observacion = QTextEdit()
        form3 = QFormLayout()
        form3.addRow(title3)
        form3.addRow("Observacion", self.observacion)

        #--------------------Container 3
        container_3 = QWidget()
        container_3.setLayout(form3)

        self.stacked = QStackedLayout()
        self.stacked.addWidget(container_1)
        self.stacked.addWidget(container_2)
        self.stacked.addWidget(container_3)

        main = QHBoxLayout()
        main.addLayout(btn_layaouts)
        main.addLayout(self.stacked)

        self.setLayout(main)
        
    def mostrar_mss(self):
        QMessageBox.information(self,
                                "Informacion",
                                f"Nombre: {self.nombre.text()}\n \
                                Apellido: {self.apellido.text()}\n \
                                Telefono: {self.tlf.text()}\n \
                                Genero: {self.genero_sel.currentText()}\n \
                                Fecha de Nacimiento: {self.fecha.text()}",
                                QMessageBox.StandardButton.Ok,
                                QMessageBox.StandardButton.Ok
                                 )

    def change_wind(self):
        nav = self.sender()
        if nav.text().lower() == 'wind 1':
            self.stacked.setCurrentIndex(0)
        elif nav.text().lower() == 'wind 2':
            self.stacked.setCurrentIndex(1)
        elif nav.text().lower() == 'wind 3':
            self.stacked.setCurrentIndex(2)

if __name__=='__main__':
    app = QApplication(sys.argv)
    windows = MainWindows()
    sys.exit(app.exec())