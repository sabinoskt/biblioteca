import os
from utils.io import obter_input_num
from services.emprestimo import mostrar_tela_dos_livros, cadastrar_cliente, emprestar_livro, devolver_livro

cliente_atual = None


def opcao_escolhida(opcao):
    os.system("cls" if os.name == "nt" else "clear")
    global cliente_atual

    match opcao:
        case 1: mostrar_tela_dos_livros()
        case 2: cliente_atual = cadastrar_cliente()
        case 3: cliente_atual = emprestar_livro(cliente_atual)
        case 4: devolver_livro(cliente_atual)
        case _: print("Não encontrado!!!")


# Menu
def menu():
    while True:
        opcoes = [
            '[1] - Listar livros',
            '[2] - Cadastrar cliente',
            '[3] - Emprestar livro',
            '[4] - Devolver livro',
            '[5] - Sair'
        ]

        for i in opcoes:
            print(i)

        entrada = int(obter_input_num(prompt='Escolha a opção', minino=1, maximo=len(opcoes)))
        if entrada == 5:
            break
        opcao_escolhida(entrada)


if __name__ == '__main__':

    menu()
