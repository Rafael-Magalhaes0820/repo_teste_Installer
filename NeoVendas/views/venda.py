from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QMessageBox, QInputDialog

from database import get_products, sell_product

class VendaScreen(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.input_search = QLineEdit()
        self.input_search.setPlaceholderText("Nome ou ID do produto")
        self.btn_search = QPushButton("Pesquisar")
        self.btn_search.clicked.connect(self.search_product)

        search_layout = QHBoxLayout()
        search_layout.addWidget(self.input_search)
        search_layout.addWidget(self.btn_search)

        layout.addLayout(search_layout)

        self.products_area = QVBoxLayout()
        layout.addLayout(self.products_area)

        self.setLayout(layout)
        self.load_products()

    def load_products(self, produtos=None):
        # limpa tela
        for i in reversed(range(self.products_area.count())):
            self.products_area.itemAt(i).widget().setParent(None)

        if produtos is None:
            produtos = get_products()

        for p in produtos:
            id_, nome, preco, estoque = p
            btn_vender = QPushButton(f"Vender (ID: {id_})")
            btn_vender.clicked.connect(lambda checked, pid=id_: self.sell(pid))
            label = QLabel(f"{nome} — R$ {preco:.2f} — Estoque: {estoque}")
            container = QHBoxLayout()
            container.addWidget(label)
            container.addWidget(btn_vender)
            w = QWidget()
            w.setLayout(container)
            self.products_area.addWidget(w)

    def search_product(self):
        termo = self.input_search.text().lower()
        all_products = get_products()
        filtered = [p for p in all_products if termo in str(p[0]) or termo in p[1].lower()]
        self.load_products(filtered)

    def sell(self, produto_id):
        qtd, ok = QInputDialog.getInt(self, "Quantidade", "Informe a quantidade:", 1, 1)
        if ok:
            result = sell_product(produto_id, qtd)
            if result != "ok":
                QMessageBox.warning(self, "Erro", result)
            self.load_products()
