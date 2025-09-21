from collections import Counter
from models.livro import Livro
from storage.historico import salvar_historico
from utils.io import obter_input_num


class EmprestimoService:
    lista_de_livros = []

    @classmethod
    def emprestar(cls, cliente, livro: Livro, quantidade):
        if livro.disponivel:
            for _ in range(quantidade):
                livro.emprestado()
                cls.lista_de_livros.append((cliente, livro))
            return True
        return False

    @classmethod
    def emprestado_lista(cls):
        return cls.lista_de_livros

    @classmethod
    def devolver(cls, livro: Livro, quantidade):
        if livro in cls.lista_de_livros:
            for _ in range(quantidade):
                livro.devolvido()
                cls.lista_de_livros.remove(livro)
            return True
        return False


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
    print('*'*100)
    print(" LIVROS DISPONÍVEIS ".center(100))
    print('*'*100)
    if livros is not None:
        for i, livro in enumerate(livros):
            estoque = f"Estoque [{livro.estoque}]" if livro.estoque > 0 else 'Sem estoque'
            status = "Disponivel" if livro.disponivel else "Indisponivel"
            print(f"[{i:02d}] {livro} - {estoque} - {status}")
    print('*'*100)


def mostrar_tela_dos_livros():
    livros = obter_lista_livros()
    exibir_menu_livros(livros)
    return len(livros), livros


def exbir_livros_disponiveis(livros):
    print('*'*100)
    print(" LIVROS DISPONÍVEIS ".center(100))
    print('*'*100)
    for i, livro in enumerate(livros):
        print(f"{i} - {livro}")
    print('*'*100)


def escolher_cliente(cliente):
    if cliente is None:
        print("Nenhum cliente cadastrado!")
        return None

    clientes = cliente.lista_cliente()

    if len(clientes) > 1:
        print("Escolha o cliente:")
        for i, client in enumerate(clientes):
            print(f"[{i:02d}] - {client}")

        indice = obter_input_num(
            prompt='Opção',
            minino=0,
            maximo=len(clientes) - 1
        )
        return clientes[indice]
    return clientes[0]


# Pegar emprestado o livro
def emprestar_livro(cliente=None):
    cliente_escolhido = escolher_cliente(cliente)

    print(f"Empréstimo para cliente: {cliente_escolhido}")
    print('Escolha um livro')

    livros_disponiveis = obter_livros_disponiveis()

    if not livros_disponiveis:
        print("Nenhum livro disponível para empréstimo")
        return None

    exbir_livros_disponiveis(livros_disponiveis)

    escolha = obter_input_num(
        prompt='Escolha a opção',
        minino=0,
        maximo=len(livros_disponiveis) - 1
    )

    livro_escolhido = livros_disponiveis[escolha]
    emprestar = EmprestimoService()

    print(f"Livro: {livro_escolhido.titulo} ({livro_escolhido.estoque}x)")
    quantidade = obter_input_num('Qual a quantidade desejada?', minino=1, maximo=livro_escolhido.estoque)
    if emprestar.emprestar(cliente_escolhido, livro_escolhido, quantidade):
        print(f"Livro '{livro_escolhido.titulo}' emprestado com sucesso para {cliente_escolhido}!")
        salvar_historico(str(cliente_escolhido), livro_escolhido, 'Emprestado')
    else:
        print("Erro: Livro já está emprestado")
        return None
    return cliente_escolhido


def devolver_livro(emprestado: EmprestimoService, cliente=None):
    cliente_escolhido = escolher_cliente(cliente)

    livros_emprestados = emprestado

    if not livros_emprestados.lista_de_livros:
        print(f"Cliente {cliente_escolhido} não tem livro(s) emprestados")
        return None

    print(f"Devolvendo pelo cliente: {cliente_escolhido}")
    print("Qual livro deseja devolver?")

    livros_do_cliente = [livro for cliente, livro in livros_emprestados.lista_de_livros if cliente == cliente_escolhido]

    contagem = Counter(livros_do_cliente)

    if len(contagem.items()) > 1:
        for i, (books, qtd) in enumerate(contagem.items()):
            print(f"[{i:02d}] - {books} ({qtd}x)")

        escolha = obter_input_num(
            prompt='Escolha a opção',
            minino=0,
            maximo=len(livros_emprestados.lista_de_livros) - 1
        )
        livro_escolhido = list(contagem.keys())[escolha]
    else:
        livro_escolhido = list(contagem.keys())[0]

    print(f"Livro: {livro_escolhido.titulo} ({livro_escolhido.estoque}x)")
    quantidade = obter_input_num('Qual a quantidade desejada devolver?', minino=1, maximo=len(contagem.values()))
    if livros_emprestados.devolver(livro_escolhido, quantidade):
        print(f"Livro '{livro_escolhido.titulo}' devolvido com sucesso!")
        salvar_historico(str(cliente_escolhido), livro_escolhido, 'Devolvido')
        return None
    else:
        print("Erro ao devolver livro")
        return None
