class Pessoa:
    def __init__(self, nome: str, sobrenome: str) -> None:
        self.nome = nome
        self.sobrenome = sobrenome

    @property
    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"

    def __str__(self):
        return self.nome_completo
