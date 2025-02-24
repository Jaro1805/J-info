import sys
from PyQt6.QtWidgets import (QApplication, QLineEdit, QLabel, QPushButton, QWidget, QDialog, QMessageBox, QCheckBox)
from PyQt6.QtGui import (QFont, QImage)

class RegistrarUsuario(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.registrar_datos()

    def registrar_datos(self):
        self.setGeometry(100, 100, 450, 400)
        self.setFixedHeight(450)
        self.setFixedWidth(400)
        self.setWindowTitle("Formulario de Registro")
        #--------------------------------------------- Variables
        label_user = QLabel(self)
        label_name = QLabel(self)
        label_lastname = QLabel(self)
        label_mail = QLabel(self)
        label_pass = QLabel(self)
        label_val_pass = QLabel(self)
        btn_crear = QPushButton(self)
        btn_cancel = QPushButton(self)
        title = QLabel(self)

        self.input_mail = QLineEdit(self)
        self.input_pass = QLineEdit(self)
        self.input_val_pass = QLineEdit(self)
        self.check_pass = QCheckBox(self)
        self.input_user = QLineEdit(self)
        self.input_name = QLineEdit(self)
        self.input_lastname = QLineEdit(self)

        #---------------------------------------------  titulo
        title.setText('REGISTRATE')
        title.setFont(QFont('Arial Black', 16))
        title.move(135, 10)

        #--------------------------------------------- Usuario
        label_user.setText("Usuario:")
        label_user.setFont(QFont('Arial', 10))
        label_user.move(20, 74)
        
        self.input_user.resize(250, 24)
        self.input_user.move(110, 70)


        #--------------------------------------------- Nombre  de Usuario
        label_name.setText("Nombre:")
        label_name.setFont(QFont('Arial', 10))
        label_name.move(20, 114)

        self.input_name.resize(250, 24)
        self.input_name.move(110, 110)


        #--------------------------------------------- Apellido  de Usuario
        label_lastname.setText("Apellido:")
        label_lastname.setFont(QFont('Arial', 10))
        label_lastname.move(20, 154)

        self.input_lastname.resize(250, 24)
        self.input_lastname.move(110, 150)

        #--------------------------------------------- Correo
        label_mail.setText("Correo:")
        label_mail.setFont(QFont('Arial', 10))
        label_mail.move(20, 194)

        
        self.input_mail.resize(250, 24)
        self.input_mail.move(110, 190)


        #--------------------------------------------- Contraseña
        label_pass.setText("Contraseña:")
        label_pass.setFont(QFont('Arial', 10))
        label_pass.move(20, 234)

        
        self.input_pass.resize(250, 24)
        self.input_pass.move(110, 230)
        self.input_pass.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        #--------------------------------------------- Contraseña
        label_val_pass.setText("Confirmación:")
        label_val_pass.setFont(QFont('Arial', 10))
        label_val_pass.move(20, 274)

        
        self.input_val_pass.resize(250, 24)
        self.input_val_pass.move(110, 270)
        self.input_val_pass.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        
        self.check_pass.setText("Ver Clave")
        self.check_pass.move(110, 310)
        self.check_pass.toggled.connect(self.ver_pass_and_val)

        #--------------------------------------------- Botones

        btn_crear.setText("Guardar")
        btn_crear.resize(100, 34)
        btn_crear.move(110, 350)
        btn_crear.clicked.connect(self.guardar_registro)


        btn_cancel.setText("Cancelar")
        btn_cancel.resize(100, 34)
        btn_cancel.move(230, 350)
        btn_cancel.clicked.connect(self.cancelar_registro)
        


    #registrar_datos

    def ver_pass_and_val(self, clicked):
        if clicked:
            self.input_pass.setEchoMode(
                QLineEdit.EchoMode.Normal
            )
            self.input_val_pass.setEchoMode(
                QLineEdit.EchoMode.Normal
            )
        else:
            self.input_pass.setEchoMode(
                QLineEdit.EchoMode.Password
            )
            self.input_val_pass.setEchoMode(
                QLineEdit.EchoMode.Password
            )
    
    def guardar_registro(self):
        usuario = self.input_user.text()
        nombre = self.input_name.text()
        apellido = self.input_lastname.text()
        correo = self.input_mail.text()
        clave = self.input_pass.text()
        val_clave = self.input_val_pass.text()
        
        if usuario == '' or  nombre == '' or apellido == '' or clave == '' or val_clave == '':
            QMessageBox.warning(self, 'ERROR DE REGISTRO',
                                'Por favor no deje campos vacios',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
            
        elif clave != val_clave:
            QMessageBox.warning(self, 'INCONINCIDENCIA',
                                'La clave debe ser igual a la validacion',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
        
        elif '@' not in correo:
            QMessageBox.warning(self, 'CORREO INVALIDO',
                                f'Por favor ingrese un correo valido {correo}',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
            
        else:
            #Curso PyQt6 - Creando login parte II. Video 03 para realizar los registro en un .txt
            try:
                QMessageBox.information(self, 'LISTO',
                                    'Usuario creado de forma correcta',
                                    QMessageBox.StandardButton.Ok,
                                    QMessageBox.StandardButton.Ok)
                self.close()
            except:
                QMessageBox.warning(self, 'ERROR',
                                'Error en base de dato, vuelva a intentarlo',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
    def cancelar_registro(self):
        self.close()
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = RegistrarUsuario()
    ventana.show()
    sys.exit(app.exec())