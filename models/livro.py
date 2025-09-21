class Livro:
    def __init__(self, titulo: str, autor: str, ano: int, estoque: int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.estoque = estoque
        self.cliente_atual = None

    def __str__(self):
        return f"Título: {self.titulo} Autor: {self.autor} Ano: {self.ano}"

    def __repr__(self):
        return str(self)

    @property
    def disponivel(self):
        return self.estoque > 0

    def emprestado(self):
        self.estoque -= 1
        return True


    def devolvido(self):
        self.cliente_atual = None
        self.estoque += 1
