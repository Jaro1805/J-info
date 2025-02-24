import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout,
                              QLineEdit, QPushButton, QMessageBox, QCheckBox)
from PyQt6.QtGui import (QFont, QPixmap)
from registro import RegistrarUsuario
from ventana import indice

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.iniciarLoginWindows()

    def iniciarLoginWindows(self):
        self.setGeometry(250, 250, 370, 300)
        self.setFixedWidth(370)
        self.setFixedHeight(300)
        self.setWindowTitle("Login J-Info")
        self.loginForm()
        self.show()

    def loginForm(self):
        self.is_loged = False
        #------------- variables ---------------------------
        company = QLabel(self)
        label_user = QLabel(self)
        label_pass = QLabel(self)
        btn_login = QPushButton(self)
        btn_register = QPushButton(self)

        self.input_user = QLineEdit(self)
        self.input_pass = QLineEdit(self)
        self.check_pass = QCheckBox(self)

        #------------- Title -------------------------------
        company.setText('J-INFO')
        company.setFont(QFont('Arial black', 20))
        company.move(145, 10)

        #------------- usuario-------------------------------
        label_user.setText('Usuario: ')
        label_user.setFont(QFont('Arial', 12))
        label_user.move(20, 94)

        self.input_user.resize(240, 24)  
        self.input_user.move(90, 90)
        #------------- Fin usuario-------------------------------
        
        #------------- Campo Contraseña--------------------------
        label_pass.setText("Clave: ")
        label_pass.setFont(QFont('Arial', 12))
        label_pass.move(20, 134)

        self.input_pass.resize(240, 24)  
        self.input_pass.move(90, 130)
        self.input_pass.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        self.check_pass.setText("")
        self.check_pass.move(340, 135)
        self.check_pass.toggled.connect(self.ver_clave) 
        '''
            togleed es una mejor opcion para los checkbox
            
        '''
        #------------- fin Contraseña----------------------------

        #---------------- Botones ------------------------------
        btn_login.setText("Ingresar")
        btn_login.resize(100, 34)
        btn_login.move(100, 180)
        btn_login.clicked.connect(self.ingresar)

        btn_register.setText("Registrar")
        btn_register.resize(100, 34)
        btn_register.move(220, 180)
        btn_register.clicked.connect(self.registrar)

       

        #----------------- fin Botones -------------------------
    #------------------ Metodos ---------------------------
    def ver_clave(self,clicked):
        if clicked:
            self.input_pass.setEchoMode(
                QLineEdit.EchoMode.Normal
            )
        else:
            self.input_pass.setEchoMode(
                QLineEdit.EchoMode.Password
            )

    def ingresar(self):
        usuario = self.input_user.text()
        clave = self.input_pass.text()
        if usuario != 'jadmin':
            QMessageBox.warning(self, 'Usuario incorrecto', 
                'Este usuario no esta registrado',
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close)
        else:
            if clave == '12345':
                self.close()
                self.open_window()
            else:
                 QMessageBox.warning(self, 'Error', 
                    'Contraseña equivocada',
                    QMessageBox.StandardButton.Close,
                    QMessageBox.StandardButton.Close)


    def registrar(self):
        self.register_user = RegistrarUsuario()
        self.register_user.show()

    #--------------------pase de usuario---------------------
    def open_window(self):
        self.openW = indice()
        self.openW.show()

    #------------------- fin de Metodos --------------------


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wind = Login()
    sys.exit(app.exec())