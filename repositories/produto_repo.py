from util import obter_conexao
from sql.produto_sql import SQL_CRIAR_TABELA, SQL_INSERIR
from models.produto_model import Produto

def criar_tabela():
    conn = obter_conexao()
    cursor = conn.cursor()
    cursor.execute(SQL_CRIAR_TABELA)
    conn.commit()
    conn.close()

def inserir(produto: Produto):
    conn = obter_conexao()
    cursor = conn.cursor()
    cursor.execute(SQL_INSERIR, (produto.nome, produto.descricao, produto.estoque, produto.preco, produto.categoria))
    conn.commit()
    conn.close()

def obter_todos():
    conn = obter_conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, descricao, estoque, preco, categoria FROM produto")
    produtos = cursor.fetchall()
    conn.close()
    return [Produto(id=row[0], nome=row[1], descricao=row[2], estoque=row[3], preco=row[4], categoria=row[5]) for row in produtos]
