from collections import Counter
from models.livro import Livro
from models.cliente import Cliente
from storage.historico import salvar_historico
from utils.io import obter_input_num, obter_input_text

LIVROS_DISPONIVEIS = [
    Livro("1984", "George Orwell", 1949, 3),
    Livro("Cem Anos de Solidão", "Gabriel García Márquez", 1967, 3),
    Livro("O Cortiço", "Aluísio Azevedo", 1890, 3),
    Livro("Sapiens", "Yuval Noah Harari", 2011, 3),
    Livro("Dom Casmurro", "Machado de Assis", 1899, 3),
]


def obter_lista_livros():
    return LIVROS_DISPONIVEIS


def obter_livros_disponiveis():
    return [livro for livro in LIVROS_DISPONIVEIS if livro.disponivel]


def exibir_menu_livros(livros=None):
    print(20 * '-' + " LIVROS " + 20 * '-' + '\n')
    if livros is not None:
        for i, livro in enumerate(livros):
            estoque = f"Estoque [{livro.estoque}]" if livro.estoque > 0 else 'Sem estoque'
            status = "Disponivel" if livro.disponivel else "Indisponivel"
            print(f"{i} - {livro} - {estoque} - {status}")
    print('\n' + 22 * '-' + ' #### ' + 20 * '-' + '\n')


def mostrar_tela_dos_livros():
    livros = obter_lista_livros()
    exibir_menu_livros(livros)
    return len(livros), livros


def cadastrar_cliente():
    print('Cadastro de cliente')
    nome = obter_input_text(prompt='Nome')
    sobrenome = obter_input_text(prompt='Sobrenome')
    cliente = Cliente(nome, sobrenome)
    print(f"Cliente {nome} {sobrenome} cadastrado com sucesso!")
    return cliente


def escolher_cliente():
    clientes = Cliente.lista_cliente()

    if not clientes:
        print("Nenhum cliente cadastrado!")
        return None

    if len(clientes) == 1:
        return clientes[0]

    print("Escolha o cliente:")
    for i, cliente in enumerate(clientes):
        print(f"{i} - {cliente}")

    indice = obter_input_num(
        prompt='Opção',
        minino=0,
        maximo=len(clientes) - 1
    )

    return clientes[indice]


# Pegar emprestado o livro
def emprestar_livro(cliente_atual=None):
    if cliente_atual is None:
        cliente_escolhido = escolher_cliente()
        if cliente_escolhido is None:
            return None
    else:
        cliente_escolhido = escolher_cliente()

    print(f"Empréstimo para cliente: {cliente_escolhido}")
    print('Escolha um livro')

    livros_disponiveis = obter_livros_disponiveis()

    if not livros_disponiveis:
        print("Nenhum livro disponível para empréstimo")
        return None

    print(20 * '-' + " LIVROS DISPONÍVEIS " + 20 * '-' + '\n')
    for i, livro in enumerate(livros_disponiveis):
        print(f"{i} - {livro}")
    print('\n' + 22 * '-' + ' ### ' + 20 * '=' + '\n')

    escolha = obter_input_num(
        prompt='Escolha a opção',
        minino=0,
        maximo=len(livros_disponiveis) - 1
    )

    livro_escolhido = livros_disponiveis[escolha]
    status = 'Emprestado'

    is_disponivel = cliente_escolhido.emprestar(livro_escolhido)
    if is_disponivel:
        print(f"Livro '{livro_escolhido.titulo}' emprestado com sucesso para {cliente_escolhido}!")
        salvar_historico(str(cliente_escolhido), livro_escolhido, status)
        return cliente_escolhido
    else:
        print("Erro: Livro já está emprestado")
        return None


def devolver_livro(cliente_atual=None):
    if cliente_atual is None:
        cliente_escolhido = escolher_cliente()
        if cliente_escolhido is None:
            return None
    else:
        cliente_escolhido = escolher_cliente()

    livros_emprestados = cliente_escolhido.emprestado_lista()

    if not livros_emprestados:
        print(f"Cliente {cliente_escolhido} não tem livro(s) emprestados")
        return None

    print(f"Devolvendo pelo cliente: {cliente_escolhido}")
    print("Qual livro deseja devolver?")

    contagem = Counter(livros_emprestados)

    for i, (book, qtd) in enumerate(contagem.items()):
        print(f"{i} - {book} ({qtd}x)")

    escolha = obter_input_num(
        prompt='Escolha a opção',
        minino=0,
        maximo=len(livros_emprestados) - 1
    )

    livro_escolhido = livros_emprestados[escolha]
    status = 'Devolvido'

    sucesso = cliente_escolhido.devolver(livro_escolhido)
    if sucesso:
        print(f"Livro '{livro_escolhido.titulo}' devolvido com sucesso!")
        salvar_historico(str(cliente_escolhido), livro_escolhido, status)
    else:
        print("Erro ao devolver livro")
