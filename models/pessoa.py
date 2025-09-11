class Pessoa:
    def __init__(self, nome: str, sobrenome: str) -> None:
        self.nome = nome
        self.sobrenome = sobrenome

    def __str__(self):
        return f"Nome: {self.nome} {self.sobrenome}"
