import os
from utils.io import obter_input_num
from models.cliente import cadastrar_cliente
from services.emprestimo import mostrar_tela_dos_livros, emprestar_livro, devolver_livro, EmprestimoService


def limpar():
    os.system("cls" if os.name == "nt" else "clear")


class Sistema:
    def __init__(self):
        self.cliente_atual = None
        self.emprestimo = EmprestimoService()

    def opcao_escolhida(self, opcao):
        limpar()
        match opcao:
            case 1: mostrar_tela_dos_livros()
            case 2: self.cliente_atual = cadastrar_cliente()
            case 3:
                if self.cliente_atual is None:
                    print("Nenhum cliente cadastrado!\n")
                else:
                    self.cliente_atual = emprestar_livro(self.cliente_atual)
            case 4:
                if self.cliente_atual is None:
                    print("Nenhum cliente cadastrado!\n")
                else:
                    devolver_livro(self.emprestimo, self.cliente_atual)
            case _: print("Não encontrado!!!")


    # Menu
    def menu(self):
        while True:
            opcoes = [
                'Listar livros',
                'Cadastrar cliente',
                'Emprestar livro',
                'Devolver livro',
                'Sair'
            ]

            print('*'*50)
            print(' MENU '.center(50))
            print('*'*50)
            for i, opcao in enumerate(opcoes, 1):
                print(f"[{i:02d}] {opcao}")

            obter_opcao = int(obter_input_num(prompt='Escolha a opção', minino=1, maximo=len(opcoes)))
            if obter_opcao == 5:
                break

            self.opcao_escolhida(obter_opcao)


if __name__ == '__main__':
    sistema = Sistema()
    sistema.menu()
