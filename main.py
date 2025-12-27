import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QStackedWidget

from views.venda import VendaScreen
from views.cadastro import CadastroScreen
from views.consulta import ConsultaScreen

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NeoVendas - PyQt")
        self.resize(900, 600)

        # Taskbar
        self.taskbar = QWidget()
        task_layout = QHBoxLayout()
        self.taskbar.setLayout(task_layout)

        self.btn_venda = QPushButton("Vendas")
        self.btn_cadastro = QPushButton("Cadastrar Itens")
        self.btn_consulta = QPushButton("Consultar Itens")

        task_layout.addWidget(self.btn_venda)
        task_layout.addWidget(self.btn_cadastro)
        task_layout.addWidget(self.btn_consulta)

        # Área principal com QStackedWidget
        self.stack = QStackedWidget()

        # Criar telas
        self.venda_screen = VendaScreen()
        self.cadastro_screen = CadastroScreen()
        self.consulta_screen = ConsultaScreen()

        self.stack.addWidget(self.venda_screen)
        self.stack.addWidget(self.cadastro_screen)
        self.stack.addWidget(self.consulta_screen)

        # Layout principal
        container = QWidget()
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.taskbar)
        main_layout.addWidget(self.stack)
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # Conectar botões
        self.btn_venda.clicked.connect(lambda: self.stack.setCurrentWidget(self.venda_screen))
        self.btn_cadastro.clicked.connect(lambda: self.stack.setCurrentWidget(self.cadastro_screen))
        self.btn_consulta.clicked.connect(lambda: self.stack.setCurrentWidget(self.consulta_screen))

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
