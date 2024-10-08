from dataclasses import dataclass

@dataclass
class Produto:
    id: int
    nome: str
    descricao: str
    estoque: int
    preco: float
    categoria: str
