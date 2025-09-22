from models.pessoa import Pessoa
from utils.io import obter_input_text


class Cliente(Pessoa):
    lista_de_cliente = []

    def __init__(self, nome, sobrenome):
        super().__init__(nome, sobrenome)
        self.is_active = True
        Cliente.lista_de_cliente.append(self)

    @classmethod
    def lista_cliente(cls):
        return cls.lista_de_cliente


def cadastrar_cliente():
    print('*'*50)
    print('Cadastro de cliente'.center(50))
    print('*'*50)
    nome = obter_input_text(prompt='Nome')
    sobrenome = obter_input_text(prompt='Sobrenome')
    cliente = Cliente(nome, sobrenome)
    print(f"Cliente {cliente.nome_completo} cadastrado com sucesso!\n")
    return cliente
