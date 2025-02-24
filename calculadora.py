import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QTextEdit, QPushButton, QGridLayout )
import operator

operations = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv
}

class MainWindows(QWidget):
    def __init__(self):
        super().__init__()
        self.incializar_ui()
        self.valor_ini = ''
        self.valor_dos = ''
        self.operador = ''
        self.pointer_flag = '1'
        self.after_iqual = False
        self.after_operator = False

    def incializar_ui(self):
        self.setGeometry(100, 100, 300,200)
        self.setWindowTitle('Calculadora')
        self.generar_calculadora()
        self.show()

    def generar_calculadora(self):
        #--------------------------------variables
        self.pantalla = QTextEdit()
        self.pantalla.setDisabled(True)

        btn_1 = QPushButton("1")
        btn_2 = QPushButton("2")
        btn_3 = QPushButton("3")
        btn_4 = QPushButton("4")
        btn_5 = QPushButton("5")
        btn_6 = QPushButton("6")
        btn_7 = QPushButton("7")
        btn_8 = QPushButton("8")
        btn_9 = QPushButton("9")
        btn_0 = QPushButton("0")
        btn_00 = QPushButton("00")
        btn_punto = QPushButton(".")
        

        btn_mas = QPushButton("+")
        btn_menos = QPushButton("-")
        btn_por = QPushButton("*")
        btn_entre = QPushButton("/")
        
        btn_igual = QPushButton("=")
        btn_ce = QPushButton("CE")
        btn_borrar = QPushButton("C")


        self.main_grid = QGridLayout()

        #---------------------------------------------- Fila 0 y 1

        self.main_grid.addWidget(self.pantalla, 0, 0, 2, 4) #(x, y, expandir en x, expandir en y)

        #---------------------------------------------- Fila 2

        self.main_grid.addWidget(btn_ce, 2, 0, 1, 2)
        self.main_grid.addWidget(btn_borrar, 2, 2)
        self.main_grid.addWidget(btn_mas, 2, 3)

        #---------------------------------------------- Fila 3

        self.main_grid.addWidget(btn_7, 3, 0)
        self.main_grid.addWidget(btn_8, 3, 1)
        self.main_grid.addWidget(btn_9, 3, 2)
        self.main_grid.addWidget(btn_entre, 3, 3)
        #---------------------------------------------- Fila 4

        self.main_grid.addWidget(btn_4, 4, 0)
        self.main_grid.addWidget(btn_5, 4, 1)
        self.main_grid.addWidget(btn_6, 4, 2)
        self.main_grid.addWidget(btn_por, 4, 3)

        #---------------------------------------------- Fila 5

        self.main_grid.addWidget(btn_1, 5, 0)
        self.main_grid.addWidget(btn_2, 5, 1)
        self.main_grid.addWidget(btn_3, 5, 2)
        self.main_grid.addWidget(btn_menos, 5, 3)

        #---------------------------------------------- Fila 5

        self.main_grid.addWidget(btn_0, 6, 0)
        self.main_grid.addWidget(btn_00, 6, 1)
        self.main_grid.addWidget(btn_punto, 6, 2)
        self.main_grid.addWidget(btn_igual, 6, 3)


        self.setLayout(self.main_grid)

        #------------------------------------------connecciones

        btn_1.clicked.connect(self.ingresar_valor)
        btn_2.clicked.connect(self.ingresar_valor)
        btn_3.clicked.connect(self.ingresar_valor)
        btn_4.clicked.connect(self.ingresar_valor)
        btn_5.clicked.connect(self.ingresar_valor)
        btn_6.clicked.connect(self.ingresar_valor)
        btn_7.clicked.connect(self.ingresar_valor)
        btn_8.clicked.connect(self.ingresar_valor)
        btn_9.clicked.connect(self.ingresar_valor)
        btn_0.clicked.connect(self.ingresar_valor)
        btn_00.clicked.connect(self.ingresar_valor)
        btn_punto.clicked.connect(self.ingresar_valor)

        btn_mas.clicked.connect(self .operando) 
        btn_menos.clicked.connect(self .operando) 
        btn_por.clicked.connect(self .operando) 
        btn_entre.clicked.connect(self .operando) 
        
        btn_igual.clicked.connect(self .igualdad) 
        btn_ce.clicked.connect(self .reiniciar_valores) 
        btn_borrar.clicked.connect(self .borrar) 
        #-----------------------------------------------fin connecciones
        
    def ingresar_valor(self):
        btn_texto = self.sender().text() #tomar el texto del boton

        if self.after_iqual:
            self.valor_ini = ''
            self.pantalla.setText(self.valor_ini)
            self.after_iqual = False
            self.pointer_flag = '1'

        if self.pointer_flag == '1':
            self.valor_ini += btn_texto
            self.pantalla.setText(self.valor_ini)

        else:
            self.valor_dos += btn_texto 
            print(self.valor_dos)
            self.pantalla.setText(self.pantalla.toPlainText() + btn_texto)
            

    def operando(self):
        btn_text = self.sender().text()
        self.operador = btn_text
        self.pointer_flag = '2'

        if self.after_operator == True:
            self.igualdad()
            self.pantalla.setText(str(self.valor_ini) + ' ' + self.operador + ' ')
            self.after_operator = False
        else:
            self.pantalla.setText(self.pantalla.toPlainText() + ' ' + self.operador + ' ')

        self.after_operator = True
        self.after_iqual = False



    def borrar(self):
        if self.after_iqual:
            self.reiniciar_valores()

        if self.pointer_flag == '1':
            self.valor_ini = self.valor_ini[:-1]
            self.pantalla.setText(self.valor_ini)

        else:
            self.valor_dos = self.valor_dos[:-1]
            self.pantalla.setText(self.valor_dos)  


    def reiniciar_valores(self):
        self.valor_ini = ''
        self.valor_dos = ''
        self.operador = ''
        self.pointer_flag = '1'
        self.after_iqual = False
        self.after_operator = False
        self.pantalla.setText("")


    def igualdad(self):
        num_1 = self.valor_ini
        num_2 = self.valor_dos
        signo = self.operador

        print(f'numero 1 = {num_1}\n numero 2 = {num_2}\n signo = {signo}')

        resultado = operations[signo](float(num_1), float(num_2))
        self.pantalla.setText(str(resultado))

        self.valor_ini = resultado
        self.valor_dos = ''
        self.after_iqual = True
        self.after_operator = False



if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindows()
    sys.exit(app.exec()) 