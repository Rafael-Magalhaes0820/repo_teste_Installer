from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from database import get_products

class ConsultaScreen(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.layout = layout
        self.setLayout(layout)
        self.load_products()

    def load_products(self):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

        produtos = get_products()
        for p in produtos:
            id_, nome, preco, estoque = p
            label = QLabel(f"ID: {id_} — {nome} — R$ {preco:.2f} — Estoque: {estoque}")
            self.layout.addWidget(label)
