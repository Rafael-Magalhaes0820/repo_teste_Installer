from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from database import add_product

class CadastroScreen(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.input_nome = QLineEdit()
        self.input_nome.setPlaceholderText("Nome do produto")
        self.input_preco = QLineEdit()
        self.input_preco.setPlaceholderText("Preço")
        self.input_estoque = QLineEdit()
        self.input_estoque.setPlaceholderText("Estoque")

        self.btn_add = QPushButton("Cadastrar")
        self.btn_add.clicked.connect(self.add_product)

        layout.addWidget(self.input_nome)
        layout.addWidget(self.input_preco)
        layout.addWidget(self.input_estoque)
        layout.addWidget(self.btn_add)

        self.setLayout(layout)

    def add_product(self):
        nome = self.input_nome.text()
        try:
            preco = float(self.input_preco.text())
            estoque = int(self.input_estoque.text())
        except:
            QMessageBox.warning(self, "Erro", "Preço ou estoque inválido")
            return
        add_product(nome, preco, estoque)
        QMessageBox.information(self, "Sucesso", "Produto cadastrado!")
        self.input_nome.clear()
        self.input_preco.clear()
        self.input_estoque.clear()
