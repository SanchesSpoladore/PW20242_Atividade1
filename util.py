import sqlite3

def obter_conexao():
    return sqlite3.connect('produtos.db')
