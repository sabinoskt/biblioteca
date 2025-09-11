class Livro:
    def __init__(self, titulo: str, autor: str, ano: int, estoque: int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.estoque = estoque
        self.disponivel = True
        self.cliente_atual = None

    def __str__(self):
        return f"Título: {self.titulo} Autor: {self.autor} Ano: {self.ano}"

    # def __iter__(self):
    #     return self

    def emprestado(self):
        if self.disponivel and self.estoque > 0:
            self.estoque -= 1
            if self.estoque == 0:
                self.disponivel = False
            return True
        return False

    def devolvido(self):
        self.disponivel = True
        self.cliente_atual = None
        self.estoque += 1
