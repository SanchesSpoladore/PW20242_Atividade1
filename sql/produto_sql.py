SQL_CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS produto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    descricao TEXT,
    estoque INTEGER,
    preco REAL,
    categoria TEXT
);
"""

SQL_INSERIR = """
INSERT INTO produto (nome, descricao, estoque, preco, categoria)
VALUES (?, ?, ?, ?, ?);
"""

SQL_EXCLUIR = """
DELETE FROM produto WHERE id = ?;
"""
