from models.pessoa import Pessoa
from models.livro import Livro
from collections import Counter


class Cliente(Pessoa):
    lista_de_cliente = []
    novo_lista_livro = []

    def __init__(self, nome, sobrenome):
        super().__init__(nome, sobrenome)

        self.lista_de_livros = []
        Cliente.lista_de_cliente.append(self)

    def emprestado_lista(self):
        return self.lista_de_livros

    @classmethod
    def lista_cliente(cls):
        return cls.lista_de_cliente

    @classmethod
    def lista_cliente_nomes(cls):
        return [str(cliente) for cliente in cls.lista_de_cliente]

    def emprestar(self, livro: Livro):
        if livro.emprestado():
            livro.cliente_atual = self
            self.lista_de_livros.append(livro)
            return True
        return False

    def devolver(self, livro: Livro):
        if livro in self.lista_de_livros:
            livro.cliente_atual = None
            livro.devolvido()
            self.lista_de_livros.remove(livro)
            return True
        return False

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
