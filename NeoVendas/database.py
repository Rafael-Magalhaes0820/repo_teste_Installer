import sqlite3
from datetime import datetime

DB_NAME = "database.db"

# Conecta e cria tabelas
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            preco REAL,
            estoque INTEGER
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto_id INTEGER,
            quantidade INTEGER,
            total REAL,
            data TEXT
        )
    """)
    conn.commit()
    conn.close()

# Adicionar produto
def add_product(nome, preco, estoque):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)", 
                   (nome, preco, estoque))
    conn.commit()
    conn.close()

# Listar produtos
def get_products():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Registrar venda
def sell_product(produto_id, quantidade):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT estoque, preco FROM produtos WHERE id = ?", (produto_id,))
    produto = cursor.fetchone()
    if not produto:
        conn.close()
        return "Produto não encontrado"
    estoque, preco = produto
    if estoque < quantidade:
        conn.close()
        return "Estoque insuficiente"
    
    total = preco * quantidade
    cursor.execute("INSERT INTO vendas (produto_id, quantidade, total, data) VALUES (?, ?, ?, ?)",
                   (produto_id, quantidade, total, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    cursor.execute("UPDATE produtos SET estoque = estoque - ? WHERE id = ?", (quantidade, produto_id))
    conn.commit()
    conn.close()
    return "ok"

# Inicializa o banco quando o módulo é importado
init_db()
